---
name: update-version-docs
description: >-
  Atualiza version/Wincash.md, NFeTop.md e NFCeTop.md com base em releases
  e PRs do gsoftbrasil/ERP-GSOFT. Use quando o usuário pedir para documentar
  versões, atualizar changelog, releases, PRs ou completar subversões
  (ex.: Wincash 3023.13, NFeTop 323).
---

# Atualizar documentação de versões

Atualiza os changelogs em `version/` deste repositório a partir das releases e PRs do **gsoftbrasil/ERP-GSOFT**.

Consulte [reference.md](reference.md) para config por produto, filtros de branch e comandos detalhados.
Consulte [examples.md](examples.md) para exemplos de redação.

## Pré-requisitos

- Repositório fonte: `gsoftbrasil/ERP-GSOFT`
- `gh` autenticado (`gh auth login` ou variável `GH_TOKEN`)
- Windows sem `gh` no PATH: usar `C:\Program Files\GitHub CLI\gh.exe`

## Fluxo

1. **Ler** o arquivo alvo (`version/Wincash.md`, `NFeTop.md` ou `NFCeTop.md`) e identificar a última subversão documentada.
2. **Listar releases** desde essa data: `gh release list --repo gsoftbrasil/ERP-GSOFT --limit 80`
3. **Ver corpo** de cada release relevante: `gh release view <tag> --repo gsoftbrasil/ERP-GSOFT`
4. **Filtrar PRs** do produto alvo (ver reference.md); ignorar build-only e outros produtos.
5. **Atribuir subversão** conforme regra de versionamento (abaixo).
6. **Detalhar PRs** via API REST (body vazio é comum — usar commits):
   ```powershell
   gh api repos/gsoftbrasil/ERP-GSOFT/pulls/<N> --jq '{title:.title,body:.body}'
   gh api repos/gsoftbrasil/ERP-GSOFT/pulls/<N>/commits --jq '.[].commit.message'
   ```
7. **Redigir bullets** em linguagem de usuário (ver examples.md).
8. **Inserir** no `.md` (subversão mais recente primeiro) e **revisar** checklist final.

## Regra de versionamento

> Se o recurso não saiu em uma versão específica, é porque ele vai sair na próxima.

Implicações:

- **Nunca** criar cabeçalhos `### (DD/MM/YYYY)` — sempre subversão numerada: `### 3023.6 (25/05/2026)`
- Release com `## Wincash WIP` (sem build) → PRs vão para a **próxima subversão numerada** nas releases seguintes
- PRs de releases intermediárias entre dois builds → documentar no build que **embarca** a mudança (ex.: PR 809 em 3023.6; PRs de 28/04 e 14/04 em 3022.8)
- Data no cabeçalho = data de **publicação** da release (`publishedAt`), formato `DD/MM/YYYY`
- Ao atualizar NFeTop/NFCeTop com entradas legadas `(DD/MM/YYYY)`, **migrar** PRs para a subversão numerada seguinte

## Formato markdown

```markdown
# Wincash 3023
[Download](https://servidor.gsoft.com.br/wincash/3023/Wincash.exe)

### 3023.13 (24/06/2026)
* ``PR 910``: Impressão do **DANFSe** (Documento Auxiliar da NFSe).
```

- Ordem: subversão **mais recente primeiro** dentro de cada linha major
- Separador `___` entre linhas major (`3023`, `3022`, …)
- Bullet: `` `PR XXX` `` + texto curto em português; termos de UI em **negrito**
- PRs do mesmo fix: ``PR 730`` / ``PR 731``

## O que incluir / ignorar

| Incluir | Ignorar |
|---------|---------|
| feat/fix do produto alvo | PRs `build/`, `Build Wincash`, `Build NFeTop` |
| Integrações desktop (ex.: NFC-e via Gsoft API no Wincash) | PRs de outros produtos no arquivo errado |
| Hotfixes com impacto ao usuário | `cursor/`, skills, ferramentas de dev |
| | PRs `doc/`, `docs/` (documentação interna) |

## Escopo por arquivo

| Arquivo | Produto | Observação |
|---------|---------|------------|
| `version/Wincash.md` | Wincash desktop | Excluir web, mobile, launcher, totem, pdvoff |
| `version/NFeTop.md` | NFeTop | Excluir wincash, nfcetop, mdfetop |
| `version/NFCeTop.md` | NFCeTop + NFCeMonitor | Subseções **NFCeTop** / **NFCeMonitor** quando a release traz os dois |

Detalhes de filtros em [reference.md](reference.md).

## Redação

- Prioridade: body do PR → mensagens de commit → título da branch
- Tom: manual de usuário, **não** changelog de dev (sem nomes de branch, sem "What's Changed")
- Antes de editar: buscar PRs já listados no `.md` para não duplicar

## Casos especiais

- **Saltos de numeração** (301.17→305, 306→320, 3023.5 ausente): manter nota explicativa se já existir; não inventar subversões
- **Nova linha major** (ex.: Wincash 3024): adicionar `# Wincash 3024` + link de download no topo; confirmar URL do servidor se incerto
- **Release conjunta** (`3020.1-320.1`): documentar só o produto do arquivo em edição

## Checklist final

- [ ] Só PRs do produto correto
- [ ] Sem entradas só com data
- [ ] Datas conferidas com `publishedAt`
- [ ] Sequência de subversões coerente
- [ ] Nenhum PR de build listado como item
- [ ] Texto entendível para usuário final (não desenvolvedor)
