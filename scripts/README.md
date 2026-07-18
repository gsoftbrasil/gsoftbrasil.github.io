# Automação local — version-docs

Atualiza diariamente `version/Wincash.md`, `NFeTop.md`, `NFCeTop.md` e `WincashWeb.md` usando **Cursor SDK (Node, runtime local)** + **GitHub CLI (`gh`)** autenticado nesta máquina. Se houver mudanças válidas, cria branch e abre **pull request** para `main`.

> Migrado de Python → Node por `WinError 10038` no `cursor-sdk` Python no Windows.

## Arquitetura

1. Agendador de Tarefas (18:00) chama `run_update_version_docs.ps1`
2. Wrapper chama `update_version_docs.mjs` via Node
3. Script valida Git/`gh`/API key e chama o agente local (`@cursor/sdk`)
4. Agente edita só `version/`
5. Script cria branch `automation/version-docs-YYYYMMDD-HHMMSS`, commit, push e PR

## Pré-requisitos

- Node.js 20+
- `gh` autenticado com acesso a:
  - `gsoftbrasil/ERP-GSOFT` (ler releases/PRs)
  - `gsoftbrasil/gsoftbrasil.github.io` (push + abrir PR)
- `CURSOR_API_KEY` no `.env` (Dashboard Cursor → Integrations / API Keys)
- Repo em `main` com worktree limpo no horário da execução

### Autenticar gh

```powershell
& "C:\Program Files\GitHub CLI\gh.exe" auth login
& "C:\Program Files\GitHub CLI\gh.exe" auth status
& "C:\Program Files\GitHub CLI\gh.exe" repo view gsoftbrasil/ERP-GSOFT
```

### Definir CURSOR_API_KEY

**Recomendado:** arquivo `.env` na raiz do repo (não versionado).

```powershell
Copy-Item .env.example .env
notepad .env
# CURSOR_API_KEY=cursor_sua_chave_aqui
```

O script carrega `.env` automaticamente. Variáveis de ambiente já definidas no sistema têm **prioridade** sobre o arquivo.

**Nunca** coloque a key no repositório, no `.ps1` ou na definição da tarefa.

## Instalação

```powershell
cd D:\GSOFT\PROJETOS_GIT\gsoftbrasil.github.io
npm install
Copy-Item .env.example .env   # se ainda não tiver
# Edite .env com sua CURSOR_API_KEY
```

## Execução manual

Pré-validação (não chama o agente):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_update_version_docs.ps1 -PreflightOnly
```

Ou direto:

```powershell
npm run version-docs:preflight
# ou
node .\scripts\update_version_docs.mjs --preflight-only
```

Fluxo completo:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_update_version_docs.ps1
# ou
npm run version-docs
```

Modelo (opcional):

```powershell
$env:CURSOR_MODEL = "composer-2.5"
node .\scripts\update_version_docs.mjs --model composer-2.5
```

Padrão: `CURSOR_MODEL` no `.env` ou `auto`.

## Agendar (18:00 horário local)

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_scheduled_task.ps1
```

Comandos úteis:

```powershell
Get-ScheduledTask -TaskName Gsoft-VersionDocs-Daily
Start-ScheduledTask -TaskName Gsoft-VersionDocs-Daily
Unregister-ScheduledTask -TaskName Gsoft-VersionDocs-Daily -Confirm:$false
```

## Códigos de saída

| Código | Significado |
|--------|-------------|
| 0 | OK (incluindo “sem mudanças”) |
| 1 | Pré-validação falhou |
| 2 | Falha do agente Cursor SDK |
| 3 | Falha em git commit/push/PR |

## Logs

`.cursor/automation-logs/` (ignorado pelo Git).

## Comportamento de segurança

- Só altera `version/*.md`
- Se já existe PR `automation/version-docs-*` aberto, a execução para
- Não faz merge automático nem force-push
- Agente **não** faz commit — o script Node cuida do PR

## Recuperação de falhas

| Sintoma | Ação |
|---------|------|
| `CURSOR_API_KEY não definida` | Crie `.env` a partir de `.env.example` |
| `gh não autenticado` / 404 ERP-GSOFT | `gh auth login` |
| `Worktree sujo` | Commit/stash antes de rodar |
| `Já existe PR aberto` | Merge ou feche o PR da automação |
| `@cursor/sdk não instalado` | `npm install` |
| Agente falhou | Ver logs em `.cursor/automation-logs/` |

## Arquivos

| Arquivo | Papel |
|---------|-------|
| `update_version_docs.mjs` | Runner (pré-validação, agente, PR) |
| `run_update_version_docs.ps1` | Wrapper + logs |
| `install_scheduled_task.ps1` | Instala tarefa diária |
| `../package.json` | Dependência `@cursor/sdk` |

O antigo `update_version_docs.py` / `requirements.txt` foram descontinuados (bug Windows no SDK Python).
