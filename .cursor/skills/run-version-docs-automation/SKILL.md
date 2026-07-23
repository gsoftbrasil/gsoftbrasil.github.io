---
name: run-version-docs-automation
description: >-
  Opera a automação local diária de version-docs (Node @cursor/sdk + gh):
  instalação, .env, Agendador Windows, pré-validação e troubleshooting
  (WinError 10038, CURSOR_API_KEY, worktree sujo, PR automation aberto).
  Use quando o usuário pedir para rodar/agendar a automação, configurar
  CURSOR_API_KEY, ou quando Cloud Automation falhar por falta de acesso ao ERP-GSOFT.
---

# Automação local version-docs

Fonte operacional completa: [`scripts/README.md`](../../../scripts/README.md).
Decisões de produto: [`.cursor/docs/version-docs-decisions.md`](../../docs/version-docs-decisions.md).
Regras de changelog: skill [`update-version-docs`](../update-version-docs/SKILL.md).

## Quando usar esta skill

- “Rode / agende a automação de versões”
- Erros: `WinError 10038`, `CURSOR_API_KEY`, worktree sujo, PR `automation/version-docs-*`
- Cloud Automation sem acesso a `gsoftbrasil/ERP-GSOFT`

## Stack (obrigatório)

| Peça | Valor |
|------|--------|
| Runtime | **Node.js 20+** (`@cursor/sdk`) — **não** Python |
| Runner | `scripts/update_version_docs.mjs` |
| Wrapper | `scripts/run_update_version_docs.ps1` |
| Agendar | `scripts/install_scheduled_task.ps1` (18:00 local) |
| Secrets | `.env` na raiz (`CURSOR_API_KEY`) — nunca commitado |

Python `cursor-sdk` neste repo foi **descontinuado** no Windows (`WinError 10038`).

## Fluxo rápido

```powershell
cd D:\GSOFT\PROJETOS_GIT\gsoftbrasil.github.io
npm install
Copy-Item .env.example .env   # se necessário; editar CURSOR_API_KEY
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_update_version_docs.ps1 -PreflightOnly
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_update_version_docs.ps1
# Agendar:
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_scheduled_task.ps1
```

Pré-requisitos da pré-validação: `main`, worktree limpo, `gh` com acesso a ERP-GSOFT e a este repo, sem PR aberto `automation/version-docs-*`.

## Cloud Automation vs local

| Caminho | Quando |
|---------|--------|
| **Local (padrão)** | Máquina com `gh` + `.env` + Node; Agendador Windows |
| Cloud Automation | Só se o ambiente multi-repo / GitHub App incluir **ERP-GSOFT** e este repo |

Cloud Agent só com `gsoftbrasil.github.io` **não** consegue listar releases do ERP-GSOFT privado.

## Códigos de saída

| Código | Significado |
|--------|-------------|
| 0 | OK (ou sem mudanças) |
| 1 | Pré-validação |
| 2 | Agente SDK |
| 3 | Git/PR |

Logs: `.cursor/automation-logs/`.

## O que o agente no chat deve fazer

1. Ler este SKILL + `scripts/README.md` se o pedido for operação/automação.
2. **Não** reimplementar o runner em Python.
3. Chat manual de changelog → skill `update-version-docs` / agente `version-docs` (sem commit salvo pedido).
4. Automação agendada: editar só via script Node (commit/PR pelo script).
