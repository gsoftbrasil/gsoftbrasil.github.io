# Automação local — version-docs

Atualiza diariamente `version/Wincash.md`, `NFeTop.md`, `NFCeTop.md` e `WincashWeb.md` usando **Cursor SDK (Python, runtime local)** + **GitHub CLI (`gh`)** autenticado nesta máquina. Se houver mudanças válidas, cria branch e abre **pull request** para `main`.

## Arquitetura

1. Agendador de Tarefas (18:00) chama `run_update_version_docs.ps1`
2. Wrapper chama `update_version_docs.py` (venv preferido)
3. Script valida Git/`gh`/API key e chama o agente local
4. Agente edita só `version/`
5. Script cria branch `automation/version-docs-YYYYMMDD-HHMMSS`, commit, push e PR

## Pré-requisitos

- Python 3.10+
- `gh` autenticado com acesso a:
  - `gsoftbrasil/ERP-GSOFT` (ler releases/PRs)
  - `gsoftbrasil/gsoftbrasil.github.io` (push + abrir PR)
- `CURSOR_API_KEY` (Dashboard Cursor → Integrations / API Keys)
- Repo em `main` com worktree limpo no horário da execução

### Autenticar gh

```powershell
& "C:\Program Files\GitHub CLI\gh.exe" auth login
& "C:\Program Files\GitHub CLI\gh.exe" auth status
& "C:\Program Files\GitHub CLI\gh.exe" repo view gsoftbrasil/ERP-GSOFT
```

### Definir CURSOR_API_KEY (usuário Windows)

```powershell
[System.Environment]::SetEnvironmentVariable("CURSOR_API_KEY", "cursor_...", "User")
# Reabra o terminal / faça logoff-login para tarefas agendadas herdarem
```

**Nunca** coloque a key no repositório, no `.ps1` ou na definição da tarefa.

## Instalação

Na raiz do repo:

```powershell
cd D:\GSOFT\PROJETOS_GIT\gsoftbrasil.github.io
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Execução manual

Pré-validação (não chama o agente):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_update_version_docs.ps1 -PreflightOnly
```

Ou direto:

```powershell
.\.venv\Scripts\python.exe .\scripts\update_version_docs.py --preflight-only
```

Fluxo completo:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_update_version_docs.ps1
```

Modelo (opcional):

```powershell
$env:CURSOR_MODEL = "composer-2.5"
# ou
.\.venv\Scripts\python.exe .\scripts\update_version_docs.py --model composer-2.5
```

Padrão: `CURSOR_MODEL` ou `auto`.

## Agendar (18:00 horário local)

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_scheduled_task.ps1
```

Opções:

```powershell
.\scripts\install_scheduled_task.ps1 -Time "18:00" -TaskName "Gsoft-VersionDocs-Daily"
```

Comandos úteis:

```powershell
Get-ScheduledTask -TaskName Gsoft-VersionDocs-Daily
Start-ScheduledTask -TaskName Gsoft-VersionDocs-Daily
Unregister-ScheduledTask -TaskName Gsoft-VersionDocs-Daily -Confirm:$false
```

A tarefa:

- roda como o usuário logado (Interactive)
- ignora nova execução se a anterior ainda estiver rodando
- **não** embute credenciais

## Códigos de saída

| Código | Significado |
|--------|-------------|
| 0 | OK (incluindo “sem mudanças”) |
| 1 | Pré-validação falhou (gh, branch, worktree, PR aberto, API key) |
| 2 | Falha do agente Cursor SDK |
| 3 | Falha em git commit/push/PR |

## Logs

Gerados em `.cursor/automation-logs/` (ignorado pelo Git).

## Comportamento de segurança

- Só altera `version/*.md`; mudanças fora disso abortam sem commit
- Se já existe PR aberto `automation/version-docs-*`, a execução para
- Não faz merge automático nem force-push
- Agente **não** faz commit — o script Python cuida do PR

## Recuperação de falhas

| Sintoma | Ação |
|---------|------|
| `CURSOR_API_KEY não definida` | Definir variável de usuário e reabrir sessão |
| `gh não autenticado` / 404 em ERP-GSOFT | `gh auth login` com conta que tem acesso ao repo privado |
| `Worktree sujo` | Commit/stash local antes de rodar |
| `Já existe PR aberto` | Merge ou fechar o PR `automation/version-docs-*` |
| Agente falhou | Ver `.cursor/automation-logs/*` e retry manual |
| Push/PR falhou | Conferir `gh auth` no destino e permissão de criar PR |

## Arquivos

| Arquivo | Papel |
|---------|-------|
| `update_version_docs.py` | Runner (pré-validação, agente, PR) |
| `run_update_version_docs.ps1` | Wrapper + logs |
| `install_scheduled_task.ps1` | Instala tarefa diária |
| `../requirements.txt` | Dependência `cursor-sdk` |
