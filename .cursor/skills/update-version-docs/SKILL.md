---
name: update-version-docs
description: >-
  Atualiza version/Wincash.md, NFeTop.md, NFCeTop.md e WincashWeb.md com base
  em releases e PRs do gsoftbrasil/ERP-GSOFT. Use quando o usuário pedir para
  documentar versões, atualizar changelog, releases, PRs, completar subversões
  (ex.: Wincash 3023.13, NFeTop 323, Wincash Web 1.0.70 / Gsoft API 100.1) ou reescrever bullets
  em inglês/jargão de dev para português de usuário final.
---

# Atualizar documentação de versões

Atualiza os changelogs em `version/` deste repositório a partir das releases e PRs do **gsoftbrasil/ERP-GSOFT**.

Consulte [reference.md](reference.md) para config por produto, filtros de branch e comandos detalhados.
Consulte [examples.md](examples.md) para exemplos de redação.

## Pré-requisitos

- Repositório fonte: `gsoftbrasil/ERP-GSOFT`
- Preferir `gh` autenticado (`gh auth login` ou `GH_TOKEN`)
- Windows sem `gh` no PATH: `C:\Program Files\GitHub CLI\gh.exe`
- Se `gh` falhar (401/404): usar **fallback git** (ver reference.md)

## Prompt padrão (`/version-docs`)

Ao ser invocado (produto omitido ou “atualize tudo”):

1. Confirmar produto(s) ou assumir os quatro arquivos em `version/`
2. Atualizar desde a última entrada documentada até a **última release publicada**
3. Entregar resumo: versões adicionadas, PRs documentados, saltos observados, WIP pendente (se houver)

## Fluxo

1. **Ler** o arquivo alvo (`version/Wincash.md`, `NFeTop.md`, `NFCeTop.md` ou `WincashWeb.md`) e identificar a última versão documentada.
2. **Listar releases** desde essa versão — preferir `gh`; se falhar, fallback git (reference.md).
3. **Ver corpo** de cada release relevante.
4. **Filtrar PRs** do produto alvo (ver reference.md); ignorar build-only e outros produtos.
5. **Atribuir subversão** conforme regra de versionamento (WincashWeb: versão numerada por produto — ver abaixo).
6. **Detalhar PRs** via API REST (body vazio é comum — usar commits) ou via mensagens de commit no fallback git.
7. **Redigir bullets** em linguagem de usuário (ver examples.md).
8. **Inserir** no `.md` (mais recente primeiro) e **revisar** checklist final.

## Deduplicação Wincash ↔ WincashWeb

| Branch / título | Arquivo |
|-----------------|---------|
| `wincash/` (desktop, mesmo citando Gsoft API) | só `version/Wincash.md` |
| `wincash-web` / `wincashweb` / `gsoftapi` / `gsoft-api` | só `version/WincashWeb.md` |

**Nunca** listar o mesmo número de PR nos dois arquivos.

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
| `version/WincashWeb.md` | Wincash Web + Gsoft API | Versão numerada da release (`1.0.70`, `100.1`); sem URL de download |

Detalhes de filtros em [reference.md](reference.md).

## WincashWeb.md — versões de release

Mesma regra dos demais produtos: **só documentar o que saiu em build numerado** nas releases do ERP-GSOFT.

Fluxo:

1. **Ler** `version/WincashWeb.md` e identificar a última versão documentada de **Wincash Web** e/ou **Gsoft API**.
2. **Listar releases** posteriores e filtrar PRs (ver reference.md).
3. **Classificar** cada PR em **Wincash Web** ou **Gsoft API** (seções `## Wincash Web` / `## WincashWeb` / `## Gsoft API` na release também contam; PRs em `wincash/` dentro de seção Web entram no Web).
4. Releases **WIP** ou sem número (`## Wincash Web WIP`, `## Gsoft API` sem versão): enfileirar por produto; na **próxima** release com versão numerada daquele produto, documentar a fila + PRs da release.
5. **Inserir** um bloco por publicação numerada (mais recente primeiro), com subseções **Wincash Web** e **Gsoft API** quando a mesma tag trouxer os dois.
6. Cada PR documentado **uma única vez**.

Formato do cabeçalho (junto por release):

```markdown
# Wincash Web

Esta página reúne as alterações do **Wincash Web** e da **Gsoft API** (serviço local de integração).
A atualização é automática — não há download manual.

### 1.0.70 / 100.1 (09/09/2026)
**Wincash Web**
* ``PR 1584``: ...

**Gsoft API**
* ``PR 1564``: ...

### 1.0.63 (02/09/2026)
**Wincash Web**
* ``PR 1506``: ...

### Gsoft API 50.5 (02/09/2026)
**Gsoft API**
* ``PR 1513``: ...
```

- Os dois na mesma tag: `### {web} / {api} (DD/MM/YYYY)` — Web à esquerda.
- Só Web: `### 1.0.63 (DD/MM/YYYY)`.
- Só API: `### Gsoft API 50.5 (DD/MM/YYYY)` (prefixo evita confundir com Web).
- Várias tags no mesmo dia **não** se mesclam — um `###` por build numerado.
- Data = `publishedAt` da release em que o número foi publicado.
- **Não** publicar notas de salto de numeração nem processo interno no `.md` público.

## Redação

- Prioridade: body do PR → mensagens de commit → título da branch
- Tom: manual de usuário, **português brasileiro** — **não** changelog de dev
- Antes de editar: buscar PRs já listados no `.md` para não duplicar

**Nunca publicar:**

| Proibido | Motivo |
|----------|--------|
| Título/body colado em inglês (`Add`/`Fix`/`Update`/`Remove`/`Refactor`/`Improve`/`UI fix`/`What's Changed`) | Usuário final lê PT |
| Texto truncado com `...` | Bullet incompleto; reescrever frase fechada |
| Nomes de arquivo/código (`.ts`, `.dpr`, `menuData`, `GsoftApiGUI`) | Jargão de dev |
| Nome de branch (`patrick/wincash/...`) ou `@autor` | Changelog interno |
| Limpeza interna sem impacto (espaços, classname, import não usado) | Omitir o PR |

Se a fonte estiver em inglês ou for título técnico: **reescrever** o benefício para o usuário (consultar commits/`gh` se o body estiver vazio ou truncado).
Pedido explícito (“limpa inglês”, “reescreve jargão”): varrer o `.md` alvo, corrigir só bullets ruins, manter datas/`PR N`/estrutura.

## Casos especiais

- **Saltos de numeração** conhecidos (não inventar intermediárias; manter nota se já existir):
  - Wincash: 3010.16→3010.18; 3010→3020; 3023.4→3023.6 (sem 3023.5); **3023.17 ausente** (PR interno embarcado em 3023.18)
  - NFeTop: 301.17→305; 306→320
- **Nova linha major** (ex.: Wincash 3024): adicionar `# Wincash 3024` + link de download no topo; confirmar URL do servidor se incerto
- **Release conjunta** (`3020.1-320.1`): documentar só o produto do arquivo em edição
- Decisões de produto/automação: [`.cursor/docs/version-docs-decisions.md`](../../docs/version-docs-decisions.md)
- Automação agendada (Node): skill `run-version-docs-automation` e [`scripts/README.md`](../../../scripts/README.md)

## Checklist final

**Wincash / NFeTop / NFCeTop:**

- [ ] Só PRs do produto correto
- [ ] Sem entradas só com data
- [ ] Datas conferidas com `publishedAt`
- [ ] Sequência de subversões coerente
- [ ] Nenhum PR de build listado como item
- [ ] Texto em PT-BR de usuário final (sem inglês colado, sem `...`, sem `.ts`/`.dpr`)

**WincashWeb.md:**

- [ ] Só PRs de Wincash Web e Gsoft API (não mobile, não desktop puro)
- [ ] Cabeçalhos com versão numerada (`### 1.0.70 / 100.1 (DD/MM/YYYY)` ou `### Gsoft API 50.5 (...)`); nunca só data
- [ ] WIP enfileirado → próxima versão numerada do produto (filas Web e API independentes)
- [ ] Datas conferidas com `publishedAt`
- [ ] Nenhum PR de build listado como item
- [ ] PRs de integração desktop não duplicados (permanecem no Wincash.md)
- [ ] Intro explica que Gsoft API está incluída; sem URL de download
- [ ] Texto em PT-BR de usuário final — sem tabelas/colunas, libs, falhas internas, processo de engenharia
