# Self-hosted runner — version-docs

Como rodar a automação `version-docs` via **GitHub Actions** nesta máquina Windows (sem depender de GitHub-hosted).

O workflow fica em [`.github/workflows/version-docs.yml`](../.github/workflows/version-docs.yml). Ele é disparado por:

| Trigger | Origem |
|---------|--------|
| `repository_dispatch` (`version-docs`) | Release publicada no `ERP-GSOFT` |
| `workflow_dispatch` | Botão **Run workflow** neste repo |
| `schedule` (21:00 UTC ≈ 18:00 BRT) | Backup diário |

Labels do job: `self-hosted`, `Windows`, `gsoft-docs`.

## Pré-requisitos na máquina

Já usados pelo fluxo local (`scripts/README.md`):

- Node.js 20+
- Git
- GitHub CLI (`gh`) autenticado com acesso a:
  - `gsoftbrasil/ERP-GSOFT` (ler releases/PRs)
  - `gsoftbrasil/gsoftbrasil.github.io` (push + abrir PR)
- Conta/máquina com permissão de admin (para instalar o serviço do runner)

## 1. Registrar o runner (uma vez)

1. No GitHub: **gsoftbrasil/gsoftbrasil.github.io** → **Settings** → **Actions** → **Runners** → **New self-hosted runner** → **Windows** → **x64**.
2. Anote o token de registro (expira em ~1 h).
3. Na máquina (PowerShell **como Administrador**):

```powershell
# Pasta sugerida (fora do clone de trabalho diário)
New-Item -ItemType Directory -Force -Path "D:\GSOFT\actions-runner\gsoftbrasil.github.io" | Out-Null
cd D:\GSOFT\actions-runner\gsoftbrasil.github.io

# Baixe o pacote indicado na página do GitHub (versão muda). Exemplo:
# Invoke-WebRequest -Uri "https://github.com/actions/runner/releases/download/v2.XXX.X/actions-runner-win-x64-2.XXX.X.zip" -OutFile actions-runner.zip
# Expand-Archive -Path actions-runner.zip -DestinationPath .

.\config.cmd --url https://github.com/gsoftbrasil/gsoftbrasil.github.io --token COLE_O_TOKEN_AQUI --labels "windows,gsoft-docs" --name "dev-manager-gsoft-docs" --work "_work"
```

Observações:

- A label `self-hosted` é adicionada automaticamente.
- Use as labels **`windows`** e **`gsoft-docs`** (o workflow filtra por elas; o runner também recebe `Windows` conforme o SO).
- **Não** use o clone diário `D:\GSOFT\PROJETOS_GIT\gsoftbrasil.github.io` como pasta do runner — o Actions faz checkout próprio em `_work`.

## 2. Rodar como serviço Windows

Ainda na pasta do runner, como Administrador:

```powershell
.\svc.cmd install
.\svc.cmd start
.\svc.cmd status
```

O serviço costuma se chamar algo como `actions.runner.gsoftbrasil-gsoftbrasil.github.io.*`.

Comandos úteis:

```powershell
.\svc.cmd stop
.\svc.cmd uninstall   # só se for remover o runner
```

Enquanto o serviço estiver **Running**, jobs com `runs-on: [self-hosted, Windows, gsoft-docs]` podem ser atendidos.

## 3. Secrets no GitHub (repo github.io)

**Settings** → **Secrets and variables** → **Actions**:

| Secret | Obrigatório? | Uso |
|--------|--------------|-----|
| `CURSOR_API_KEY` | **Sim** | Mesma chave do `.env` local (Dashboard Cursor → API Keys) |
| `VERSION_DOCS_GH_TOKEN` | Recomendado | PAT com acesso a `ERP-GSOFT` **e** a este repo (ler releases + push/PR). Se **omitido**, o job remove o `GITHUB_TOKEN` do Actions e usa o `gh auth` já feito nesta máquina |

**Nunca** committe `CURSOR_API_KEY`, PAT ou `.env`.

### `.env` local vs secret

| Onde | Quando vale |
|------|-------------|
| `.env` na pasta do clone diário | Agendador Windows / `npm run version-docs` manual |
| Secret `CURSOR_API_KEY` no GitHub | Job do Actions (checkout em `_work` — **não** lê o `.env` do clone diário) |

Pode manter os dois alinhados (mesma key); o secret do GitHub é o que o workflow usa.

## 4. Secret no ERP-GSOFT (dispatch)

No repo **gsoftbrasil/ERP-GSOFT**:

| Secret | Uso |
|--------|-----|
| `DOCS_DISPATCH_TOKEN` | PAT (classic `repo` ou fine-grained com **Contents: Read** + permissão para disparar Actions / `repo` no `gsoftbrasil.github.io`) usado pelo workflow `version-docs-dispatch` em `on: release: published` |

O `GITHUB_TOKEN` padrão do ERP **não** consegue fazer `repository_dispatch` em outro repositório.

## 5. Testar

1. Confirme o runner **Idle** em Settings → Actions → Runners.
2. Neste repo: **Actions** → **version-docs** → **Run workflow** → marque `preflight_only` na primeira vez.
3. Se o preflight passar, rode de novo sem `preflight_only`.
4. (Opcional) Publique uma release de teste no ERP ou use `gh` para simular o dispatch:

```powershell
gh api repos/gsoftbrasil/gsoftbrasil.github.io/dispatches -f event_type=version-docs
```

## 6. Relação com o Agendador Windows

O Agendador (`install_scheduled_task.ps1`) e o `schedule` do Actions são **redundantes** de propósito (backup). Se ambos rodarem no mesmo horário, o `concurrency.group: version-docs` no workflow evita dois jobs Actions em paralelo; ainda assim, o Agendador local e o Actions podem conflitar se ambos tentarem abrir PR `automation/version-docs-*` — o script aborta se já existir PR aberto.

Recomendação: após o runner estável, desative a tarefa agendada local **ou** mantenha só uma das rotinas diárias.

## Troubleshooting rápido

| Sintoma | O que checar |
|---------|----------------|
| Job queued forever | Serviço do runner parado; labels diferentes do workflow |
| `CURSOR_API_KEY` ausente | Secret no **github.io**, não no ERP |
| Sem acesso ao ERP-GSOFT | `VERSION_DOCS_GH_TOKEN` ou `gh auth login` na máquina do runner |
| Worktree sujo / branch ≠ main | O workflow já faz `reset --hard origin/main` no checkout do Actions |
| PR automation já aberto | Merge/feche o PR antes de novo run |
| Dispatch do ERP falha | Secret `DOCS_DISPATCH_TOKEN` no ERP-GSOFT |

## Pasta resumida

```text
D:\GSOFT\actions-runner\gsoftbrasil.github.io\   ← runner + serviço
D:\GSOFT\PROJETOS_GIT\gsoftbrasil.github.io\     ← clone diário / Agendador (opcional)
```
