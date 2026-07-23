# Decisões — documentação de versões Gsoft

Registro estável do “porquê”. Regras operacionais: skills `update-version-docs` e `run-version-docs-automation`.

## Produtos e arquivos

| Arquivo | Escopo | Identificador |
|---------|--------|---------------|
| `version/Wincash.md` | Wincash desktop | Subversão (`3023.20`) + data de publicação |
| `version/NFeTop.md` | NFeTop | Subversão |
| `version/NFCeTop.md` | NFCeTop + NFCeMonitor | Subversão / subseções |
| `version/WincashWeb.md` | Wincash Web + **Gsoft API** | **Só data** (`### DD/MM/YYYY`); sem URL de download |

- Nome da página Web prioriza “Wincash Web” para o leitor; intro do arquivo deixa claro que a Gsoft API entra no mesmo changelog.
- Integração **desktop** que consome a API permanece no `Wincash.md`; mudanças na API/front web vão no `WincashWeb.md` (sem duplicar PR).

## Versionamento

> Se o recurso não saiu em uma versão específica, é porque ele vai sair na próxima.

- Wincash / NFeTop / NFCeTop: nunca cabeçalho só com data; WIP → próxima subversão numerada.
- WincashWeb: WIP fica na **data da release WIP** (não há build numerado).

## Automação

- Caminho padrão: **Node** (`@cursor/sdk`) + `gh` local + Agendador Windows (`scripts/`).
- Secrets em `.env` (`CURSOR_API_KEY`); nunca no repo.
- **Python SDK** (`cursor-sdk`) descontinuado neste repositório no Windows (`WinError 10038`).
- **Cursor Cloud Automation** sozinha no repo `gsoftbrasil.github.io` falha sem acesso ao `ERP-GSOFT` privado; exige multi-repo / GitHub App com os dois repos, ou permanece no fluxo local.

## Fonte de verdade

- Releases/PRs: `gsoftbrasil/ERP-GSOFT`
- Preferir `gh`; sem auth, fallback `git ls-remote` / tags (ver `update-version-docs/reference.md`)

## Mapa do monorepo (contexto interno)

- Pastas e destinos de produto: `ERP-GSOFT/README.md` (repo privado `gsoftbrasil/ERP-GSOFT`) — Wincash, WincashWebMobile, NFeTop, NFCeTop, PDVOff, etc.
- **Ainda fora** de `version/` neste site (não documentar na automação até decisão explícita): PDVOff, mobile, MDFeTop, Cardápio Digital, GFood, GAF, GSPED, Launcher, Multicash.
- Automação atual continua **somente** nos quatro arquivos da tabela acima.
