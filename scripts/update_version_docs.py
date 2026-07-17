#!/usr/bin/env python3
"""Atualiza documentação de versões via Cursor SDK local + gh, e abre PR se houver mudanças."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VERSION_FILES = (
    "version/Wincash.md",
    "version/NFeTop.md",
    "version/NFCeTop.md",
    "version/WincashWeb.md",
)
SOURCE_REPO = "gsoftbrasil/ERP-GSOFT"
DEST_REPO = "gsoftbrasil/gsoftbrasil.github.io"
PR_HEAD_PREFIX = "automation/version-docs-"
DEFAULT_MODEL = "auto"

EXIT_OK = 0
EXIT_NO_CHANGES = 0
EXIT_PREFLIGHT = 1
EXIT_AGENT = 2
EXIT_GIT_PR = 3


class PreflightError(RuntimeError):
    pass


class GitPrError(RuntimeError):
    pass


def log(msg: str) -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{stamp}] {msg}", flush=True)


def find_gh() -> str:
    path = shutil.which("gh")
    if path:
        return path
    candidate = Path(r"C:\Program Files\GitHub CLI\gh.exe")
    if candidate.is_file():
        return str(candidate)
    raise PreflightError("gh não encontrado no PATH nem em C:\\Program Files\\GitHub CLI\\gh.exe")


def run(
    args: list[str],
    *,
    cwd: Path | None = None,
    check: bool = True,
    capture: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    merged = os.environ.copy()
    if env:
        merged.update(env)
    result = subprocess.run(
        args,
        cwd=str(cwd or REPO_ROOT),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=capture,
        env=merged,
    )
    if check and result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        detail = stderr or stdout or f"exit {result.returncode}"
        raise RuntimeError(f"Falha em {' '.join(args)}: {detail}")
    return result


def require_clean_main() -> None:
    branch = run(["git", "branch", "--show-current"]).stdout.strip()
    if branch != "main":
        raise PreflightError(f"Branch atual é '{branch}'; esperado 'main'")

    status = run(["git", "status", "--porcelain"]).stdout
    if status.strip():
        raise PreflightError(
            "Worktree sujo. Faça commit/stash das alterações locais antes de rodar a automação."
        )


def require_cursor_key() -> str:
    key = (os.environ.get("CURSOR_API_KEY") or "").strip()
    if not key:
        raise PreflightError(
            "CURSOR_API_KEY não definida. Configure variável de ambiente do usuário Windows."
        )
    return key


def require_gh_access(gh: str) -> None:
    auth = run([gh, "auth", "status"], check=False)
    if auth.returncode != 0:
        raise PreflightError(
            "gh não autenticado. Execute: gh auth login\n"
            f"{(auth.stderr or auth.stdout or '').strip()}"
        )

    view = run([gh, "repo", "view", SOURCE_REPO, "--json", "nameWithOwner"], check=False)
    if view.returncode != 0:
        raise PreflightError(
            f"Sem acesso a {SOURCE_REPO}. Libere o token/gh para o repo privado.\n"
            f"{(view.stderr or view.stdout or '').strip()}"
        )


def open_automation_prs(gh: str) -> list[dict]:
    result = run(
        [
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
        ]
    )
    items = json.loads(result.stdout or "[]")
    return [p for p in items if str(p.get("headRefName", "")).startswith(PR_HEAD_PREFIX)]


def preflight(gh: str, *, skip_agent: bool) -> None:
    log("Pré-validação...")
    if not skip_agent:
        require_cursor_key()
    require_clean_main()
    require_gh_access(gh)

    open_prs = open_automation_prs(gh)
    if open_prs:
        urls = ", ".join(p.get("url", f"#{p.get('number')}") for p in open_prs)
        raise PreflightError(
            "Já existe PR aberto da automação. Mescle ou feche antes de rodar de novo: "
            + urls
        )

    log("Pré-validação OK.")


def build_prompt() -> str:
    return f"""Você é o especialista version-docs deste repositório.

Antes de qualquer outra coisa:
1. Leia e siga `.cursor/agents/version-docs.md`
2. Leia e siga `.cursor/skills/update-version-docs/SKILL.md`
3. Consulte `.cursor/skills/update-version-docs/reference.md` e `examples.md` conforme necessário

Tarefa (automação diária local):
- Atualize `version/Wincash.md`, `version/NFeTop.md`, `version/NFCeTop.md` e `version/WincashWeb.md`
  a partir das releases do repositório fonte `{SOURCE_REPO}`
- Use o `gh` local já autenticado neste ambiente
- No Windows, se `gh` não estiver no PATH: `C:\\Program Files\\GitHub CLI\\gh.exe`
- Edite **somente** arquivos em `version/`
- **NÃO** faça commit, push, merge nem abra PR (o script externo cuida disso)
- Se não houver release/PR novo para documentar: não altere nada
- Ao final, responda em português com resumo: arquivos alterados, versões/datas adicionadas, PRs documentados, saltos observados; ou diga que não houve mudanças
"""


def run_agent(model: str) -> str:
    from cursor_sdk import Agent, AgentOptions, LocalAgentOptions

    try:
        from cursor_sdk import CursorAgentError as _CursorAgentError
    except ImportError:  # pragma: no cover

        class _CursorAgentError(Exception):
            pass

    api_key = require_cursor_key()
    log(f"Iniciando Cursor SDK local (model={model})...")
    try:
        result = Agent.prompt(
            build_prompt(),
            AgentOptions(
                api_key=api_key,
                model=model,
                local=LocalAgentOptions(cwd=str(REPO_ROOT)),
            ),
        )
    except _CursorAgentError as exc:
        message = getattr(exc, "message", str(exc))
        retryable = getattr(exc, "is_retryable", getattr(exc, "retryable", "?"))
        raise RuntimeError(
            f"Falha ao iniciar agente: {message} (retryable={retryable})"
        ) from exc

    status = getattr(result, "status", None)
    text = getattr(result, "result", None) or ""
    run_id = getattr(result, "id", "")
    log(f"Agente finalizado: status={status} run_id={run_id}")
    if status == "error":
        raise RuntimeError(f"Agente terminou com erro (run_id={run_id})")
    return str(text)


def changed_paths() -> list[str]:
    result = run(["git", "status", "--porcelain"])
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        # porcelain: XY PATH or XY ORIG -> PATH
        entry = line[3:]
        if " -> " in entry:
            entry = entry.split(" -> ", 1)[1]
        paths.append(entry.replace("\\", "/"))
    return paths


def assert_only_version_changes(paths: list[str]) -> None:
    bad = [p for p in paths if not p.startswith("version/")]
    if bad:
        raise GitPrError(
            "Mudanças fora de version/ detectadas; abortando sem commit: "
            + ", ".join(bad)
        )


def create_branch_commit_push_pr(gh: str, agent_summary: str) -> str:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    branch = f"{PR_HEAD_PREFIX}{stamp}"
    title = f"docs(version): atualização automática {datetime.now().strftime('%d/%m/%Y')}"

    log(f"Criando branch {branch}...")
    run(["git", "checkout", "-b", branch])

    try:
        run(["git", "add", "--", *VERSION_FILES])
        staged = run(["git", "diff", "--cached", "--name-only"]).stdout.strip()
        if not staged:
            run(["git", "checkout", "main"], check=False)
            run(["git", "branch", "-D", branch], check=False)
            raise GitPrError("Nenhum arquivo version/*.md staged após git add")

        body_summary = agent_summary.strip() or "Atualização automática da documentação de versões."
        # Truncate for PR body safety
        if len(body_summary) > 3500:
            body_summary = body_summary[:3500] + "\n\n...(resumo truncado)"

        commit_msg = (
            f"{title}\n\n"
            "Atualização gerada pela automação local version-docs "
            "(Cursor SDK + gh)."
        )
        run(["git", "commit", "-m", commit_msg])
        run(["git", "push", "-u", "origin", branch])

        pr_body = f"""## Summary
Atualização automática da documentação em `version/` a partir das releases de `{SOURCE_REPO}`.

### Resultado do agente
{body_summary}

## Test plan
- [ ] Conferir apenas arquivos em `version/`
- [ ] Validar datas/subversões e PRs documentados
- [ ] Confirmar ausência de PRs de build / produtos fora do escopo
"""
        pr = run(
            [
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
                pr_body,
            ]
        )
        url = (pr.stdout or "").strip().splitlines()[-1] if pr.stdout else ""
        log(f"PR criado: {url}")
        return url
    except Exception:
        # Best-effort return to main for next manual run
        run(["git", "checkout", "main"], check=False)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Automação local version-docs")
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Só valida pré-requisitos (não chama o agente nem cria PR)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("CURSOR_MODEL", DEFAULT_MODEL),
        help=f"Modelo Cursor SDK (default: env CURSOR_MODEL ou {DEFAULT_MODEL})",
    )
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    args = parse_args()
    os.chdir(REPO_ROOT)
    log(f"Repo: {REPO_ROOT}")

    try:
        gh = find_gh()
        log(f"gh: {gh}")
        preflight(gh, skip_agent=args.preflight_only)

        if args.preflight_only:
            log("Pré-validação concluída (--preflight-only).")
            return EXIT_OK

        # Refresh main before agent edits
        run(["git", "fetch", "origin", "main"])
        run(["git", "pull", "--ff-only", "origin", "main"])

        summary = run_agent(args.model)

        paths = changed_paths()
        if not paths:
            log("Sem alterações em version/. Nada a publicar.")
            if summary.strip():
                print(summary)
            return EXIT_NO_CHANGES

        assert_only_version_changes(paths)
        log("Arquivos alterados: " + ", ".join(paths))
        url = create_branch_commit_push_pr(gh, summary)
        # Return to main so next scheduled run starts clean
        run(["git", "checkout", "main"], check=False)
        run(["git", "pull", "--ff-only", "origin", "main"], check=False)
        print(summary)
        log(f"Concluído. PR: {url}")
        return EXIT_OK

    except PreflightError as exc:
        log(f"PRÉ-VALIDAÇÃO FALHOU: {exc}")
        return EXIT_PREFLIGHT
    except GitPrError as exc:
        log(f"GIT/PR FALHOU: {exc}")
        return EXIT_GIT_PR
    except Exception as exc:
        # Distinguish agent vs unexpected by message prefix when possible
        msg = str(exc)
        if msg.startswith("Falha ao iniciar agente") or msg.startswith("Agente terminou"):
            log(f"AGENTE FALHOU: {exc}")
            return EXIT_AGENT
        log(f"ERRO: {exc}")
        return EXIT_AGENT


if __name__ == "__main__":
    sys.exit(main())
