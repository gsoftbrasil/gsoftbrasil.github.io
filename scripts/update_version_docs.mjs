#!/usr/bin/env node
/**
 * Atualiza documentação de versões via @cursor/sdk (local) + gh, e abre PR se houver mudanças.
 * Migrado de Python por WinError 10038 no cursor-sdk Python no Windows.
 */
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Agent, CursorAgentError } from "@cursor/sdk";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, "..");

const VERSION_FILES = [
  "version/Wincash.md",
  "version/NFeTop.md",
  "version/NFCeTop.md",
  "version/WincashWeb.md",
];
const SOURCE_REPO = "gsoftbrasil/ERP-GSOFT";
const DEST_REPO = "gsoftbrasil/gsoftbrasil.github.io";
const PR_HEAD_PREFIX = "automation/version-docs-";
const DEFAULT_MODEL = "auto";

const EXIT_OK = 0;
const EXIT_PREFLIGHT = 1;
const EXIT_AGENT = 2;
const EXIT_GIT_PR = 3;

class PreflightError extends Error {}
class GitPrError extends Error {}

function log(msg) {
  const stamp = new Date().toISOString().replace("T", " ").slice(0, 19);
  console.log(`[${stamp}] ${msg}`);
}

function loadDotenv(filePath = path.join(REPO_ROOT, ".env")) {
  if (!fs.existsSync(filePath)) return;
  const text = fs.readFileSync(filePath, "utf8");
  for (const raw of text.split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith("#") || !line.includes("=")) continue;
    const eq = line.indexOf("=");
    const key = line.slice(0, eq).trim();
    if (!key) continue;
    let val = line.slice(eq + 1).trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    if (process.env[key] === undefined) process.env[key] = val;
  }
}

function findGh() {
  const which = spawnSync(process.platform === "win32" ? "where" : "which", ["gh"], {
    encoding: "utf8",
  });
  const first = (which.stdout || "").split(/\r?\n/).map((s) => s.trim()).find(Boolean);
  if (first && fs.existsSync(first)) return first;
  const candidate = "C:\\Program Files\\GitHub CLI\\gh.exe";
  if (fs.existsSync(candidate)) return candidate;
  throw new PreflightError(
    "gh não encontrado no PATH nem em C:\\Program Files\\GitHub CLI\\gh.exe",
  );
}

function run(args, { check = true, cwd = REPO_ROOT } = {}) {
  const [cmd, ...rest] = args;
  const result = spawnSync(cmd, rest, {
    cwd,
    encoding: "utf8",
    env: process.env,
    shell: false,
  });
  if (check && result.status !== 0) {
    const detail =
      (result.stderr || "").trim() ||
      (result.stdout || "").trim() ||
      `exit ${result.status}`;
    throw new Error(`Falha em ${args.join(" ")}: ${detail}`);
  }
  return {
    status: result.status ?? 1,
    stdout: result.stdout || "",
    stderr: result.stderr || "",
  };
}

function requireCursorKey() {
  const key = (process.env.CURSOR_API_KEY || "").trim();
  if (!key) {
    throw new PreflightError(
      "CURSOR_API_KEY não definida. Crie `.env` na raiz (veja `.env.example`) " +
        "ou defina a variável de ambiente do usuário Windows.",
    );
  }
  return key;
}

function requireCleanMain() {
  const branch = run(["git", "branch", "--show-current"]).stdout.trim();
  if (branch !== "main") {
    throw new PreflightError(`Branch atual é '${branch}'; esperado 'main'`);
  }
  const status = run(["git", "status", "--porcelain"]).stdout;
  if (status.trim()) {
    throw new PreflightError(
      "Worktree sujo. Faça commit/stash das alterações locais antes de rodar a automação.",
    );
  }
}

function requireGhAccess(gh) {
  const auth = run([gh, "auth", "status"], { check: false });
  if (auth.status !== 0) {
    throw new PreflightError(
      "gh não autenticado. Execute: gh auth login\n" +
        (auth.stderr || auth.stdout || "").trim(),
    );
  }
  const view = run(
    [gh, "repo", "view", SOURCE_REPO, "--json", "nameWithOwner"],
    { check: false },
  );
  if (view.status !== 0) {
    throw new PreflightError(
      `Sem acesso a ${SOURCE_REPO}. Libere o token/gh para o repo privado.\n` +
        (view.stderr || view.stdout || "").trim(),
    );
  }
}

function openAutomationPrs(gh) {
  const result = run([
    gh,
    "pr",
    "list",
    "--repo",
    DEST_REPO,
    "--state",
    "open",
    "--json",
    "number,title,headRefName,url",
    "--limit",
    "50",
  ]);
  const items = JSON.parse(result.stdout || "[]");
  return items.filter((p) =>
    String(p.headRefName || "").startsWith(PR_HEAD_PREFIX),
  );
}

function preflight(gh, { skipAgent }) {
  log("Pré-validação...");
  if (!skipAgent) requireCursorKey();
  requireCleanMain();
  requireGhAccess(gh);
  const openPrs = openAutomationPrs(gh);
  if (openPrs.length) {
    const urls = openPrs
      .map((p) => p.url || `#${p.number}`)
      .join(", ");
    throw new PreflightError(
      "Já existe PR aberto da automação. Mescle ou feche antes de rodar de novo: " +
        urls,
    );
  }
  log("Pré-validação OK.");
}

function buildPrompt() {
  return `Você é o especialista version-docs deste repositório.

Antes de qualquer outra coisa:
1. Leia e siga \`.cursor/agents/version-docs.md\`
2. Leia e siga \`.cursor/skills/update-version-docs/SKILL.md\`
3. Consulte \`.cursor/skills/update-version-docs/reference.md\` e \`examples.md\` conforme necessário

Tarefa (automação diária local):
- Atualize \`version/Wincash.md\`, \`version/NFeTop.md\`, \`version/NFCeTop.md\` e \`version/WincashWeb.md\`
  a partir das releases do repositório fonte \`${SOURCE_REPO}\`
- Use o \`gh\` local já autenticado neste ambiente
- No Windows, se \`gh\` não estiver no PATH: \`C:\\\\Program Files\\\\GitHub CLI\\\\gh.exe\`
- Edite **somente** arquivos em \`version/\`
- **NÃO** faça commit, push, merge nem abra PR (o script externo cuida disso)
- Se não houver release/PR novo para documentar: não altere nada
- Ao final, responda em português com resumo: arquivos alterados, versões/datas adicionadas, PRs documentados, saltos observados; ou diga que não houve mudanças
`;
}

async function runAgent(model) {
  const apiKey = requireCursorKey();
  log(`Iniciando Cursor SDK local (model=${model})...`);
  try {
    const result = await Agent.prompt(buildPrompt(), {
      apiKey,
      model: { id: model },
      local: { cwd: REPO_ROOT },
    });
    const status = result.status;
    const text = result.result || "";
    const runId = result.id || "";
    log(`Agente finalizado: status=${status} run_id=${runId}`);
    if (status === "error") {
      throw new Error(`Agente terminou com erro (run_id=${runId})`);
    }
    return String(text);
  } catch (exc) {
    if (exc instanceof CursorAgentError) {
      throw new Error(
        `Falha ao iniciar agente: ${exc.message} (retryable=${exc.isRetryable})`,
      );
    }
    throw exc;
  }
}

function changedPaths() {
  const result = run(["git", "status", "--porcelain"]);
  const paths = [];
  for (const line of result.stdout.split(/\r?\n/)) {
    if (!line.trim()) continue;
    let entry = line.slice(3);
    if (entry.includes(" -> ")) entry = entry.split(" -> ").pop();
    paths.push(entry.replace(/\\/g, "/"));
  }
  return paths;
}

function assertOnlyVersionChanges(paths) {
  const bad = paths.filter((p) => !p.startsWith("version/"));
  if (bad.length) {
    throw new GitPrError(
      "Mudanças fora de version/ detectadas; abortando sem commit: " +
        bad.join(", "),
    );
  }
}

function pad(n) {
  return String(n).padStart(2, "0");
}

function stampNow() {
  const d = new Date();
  return (
    `${d.getFullYear()}${pad(d.getMonth() + 1)}${pad(d.getDate())}-` +
    `${pad(d.getHours())}${pad(d.getMinutes())}${pad(d.getSeconds())}`
  );
}

function dateBr() {
  const d = new Date();
  return `${pad(d.getDate())}/${pad(d.getMonth() + 1)}/${d.getFullYear()}`;
}

function createBranchCommitPushPr(gh, agentSummary) {
  const branch = `${PR_HEAD_PREFIX}${stampNow()}`;
  const title = `docs(version): atualização automática ${dateBr()}`;

  log(`Criando branch ${branch}...`);
  run(["git", "checkout", "-b", branch]);

  try {
    run(["git", "add", "--", ...VERSION_FILES]);
    const staged = run(["git", "diff", "--cached", "--name-only"]).stdout.trim();
    if (!staged) {
      run(["git", "checkout", "main"], { check: false });
      run(["git", "branch", "-D", branch], { check: false });
      throw new GitPrError("Nenhum arquivo version/*.md staged após git add");
    }

    let bodySummary =
      (agentSummary || "").trim() ||
      "Atualização automática da documentação de versões.";
    if (bodySummary.length > 3500) {
      bodySummary = bodySummary.slice(0, 3500) + "\n\n...(resumo truncado)";
    }

    const commitMsg =
      `${title}\n\n` +
      "Atualização gerada pela automação local version-docs " +
      "(Cursor SDK Node + gh).";
    run(["git", "commit", "-m", commitMsg]);
    run(["git", "push", "-u", "origin", branch]);

    const prBody = `## Summary
Atualização automática da documentação em \`version/\` a partir das releases de \`${SOURCE_REPO}\`.

### Resultado do agente
${bodySummary}

## Test plan
- [ ] Conferir apenas arquivos em \`version/\`
- [ ] Validar datas/subversões e PRs documentados
- [ ] Confirmar ausência de PRs de build / produtos fora do escopo
`;
    const pr = run([
      gh,
      "pr",
      "create",
      "--repo",
      DEST_REPO,
      "--base",
      "main",
      "--head",
      branch,
      "--title",
      title,
      "--body",
      prBody,
    ]);
    const lines = (pr.stdout || "").trim().split(/\r?\n/);
    const url = lines[lines.length - 1] || "";
    log(`PR criado: ${url}`);
    return url;
  } catch (err) {
    run(["git", "checkout", "main"], { check: false });
    throw err;
  }
}

function parseArgs(argv) {
  const out = {
    preflightOnly: false,
    model: process.env.CURSOR_MODEL || DEFAULT_MODEL,
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--preflight-only") out.preflightOnly = true;
    else if (a === "--model") {
      out.model = argv[++i] || DEFAULT_MODEL;
    }
  }
  return out;
}

async function main() {
  process.chdir(REPO_ROOT);
  loadDotenv();
  const args = parseArgs(process.argv.slice(2));
  log(`Repo: ${REPO_ROOT}`);
  if (fs.existsSync(path.join(REPO_ROOT, ".env"))) {
    log("Credenciais: .env carregado (env vars existentes têm prioridade)");
  }

  try {
    const gh = findGh();
    log(`gh: ${gh}`);
    preflight(gh, { skipAgent: args.preflightOnly });

    if (args.preflightOnly) {
      log("Pré-validação concluída (--preflight-only).");
      return EXIT_OK;
    }

    run(["git", "fetch", "origin", "main"]);
    run(["git", "pull", "--ff-only", "origin", "main"]);

    const summary = await runAgent(args.model);
    const paths = changedPaths();
    if (!paths.length) {
      log("Sem alterações em version/. Nada a publicar.");
      if (summary.trim()) console.log(summary);
      return EXIT_OK;
    }

    assertOnlyVersionChanges(paths);
    log("Arquivos alterados: " + paths.join(", "));
    const url = createBranchCommitPushPr(gh, summary);
    run(["git", "checkout", "main"], { check: false });
    run(["git", "pull", "--ff-only", "origin", "main"], { check: false });
    console.log(summary);
    log(`Concluído. PR: ${url}`);
    return EXIT_OK;
  } catch (exc) {
    if (exc instanceof PreflightError) {
      log(`PRÉ-VALIDAÇÃO FALHOU: ${exc.message}`);
      return EXIT_PREFLIGHT;
    }
    if (exc instanceof GitPrError) {
      log(`GIT/PR FALHOU: ${exc.message}`);
      return EXIT_GIT_PR;
    }
    const msg = String(exc && exc.message ? exc.message : exc);
    if (
      msg.startsWith("Falha ao iniciar agente") ||
      msg.startsWith("Agente terminou")
    ) {
      log(`AGENTE FALHOU: ${msg}`);
      return EXIT_AGENT;
    }
    log(`ERRO: ${msg}`);
    if (exc && exc.stack) console.error(exc.stack);
    return EXIT_AGENT;
  }
}

const code = await main();
process.exit(code);
