# Referência — update-version-docs

## Repositórios e arquivos

| Papel | Valor |
|-------|-------|
| Fonte (releases/PRs) | `gsoftbrasil/ERP-GSOFT` |
| Destino Wincash | `version/Wincash.md` |
| Destino NFeTop | `version/NFeTop.md` |
| Destino NFCeTop | `version/NFCeTop.md` |
| Destino Wincash Web | `version/WincashWeb.md` |

WincashWeb.md: documenta **Wincash Web** e **Gsoft API** juntos, por **versão numerada da release**, sem URL de download.

## URLs de download

Substituir `{linha}` pelo número major (3023, 323, 305, etc.):

| Produto | URL |
|---------|-----|
| Wincash | `https://servidor.gsoft.com.br/wincash/{linha}/Wincash.exe` |
| NFeTop | `https://servidor.gsoft.com.br/NFeTop/{linha}/NFeTop.exe` |
| NFCeTop | `https://servidor.gsoft.com.br/NFCeTop/{linha}/NFCeTop.exe` |

NFCeTop.md: incluir nota de que NFCeTop e NFCeMonitor são documentados juntos na mesma linha.

## Padrão de tags de release

| Período | Formato | Exemplo |
|---------|---------|---------|
| Atual (a partir de ago/2026) | `AAAA-MM-DD-HHmm` — **sem** prefixo `v` | `2026-08-05-1824` |
| Intermediário (legado) | `vAAAA-MM-DD` (sufixo `-a` ocasional) | `v2026-06-24`, `v2026-05-22-a` |
| Antigo | número de build | `3010.15`, `3005.1` |

Tags antigas **não são renomeadas** — só releases novas usam `AAAA-MM-DD-HHmm`. O `HHmm` distingue várias releases no mesmo dia (substitui o sufixo `-a`).

Corpo da release usa seções `## Wincash 3023.13`, `## NFeTop 323.2`, `## Wincash WIP`, etc.

## Detecção de build no corpo da release

Regex úteis (case insensitive):

- Wincash: `Wincash\s+(\d+\.\d+(?:\.\d+)?)`
- NFeTop: `NFeTop\s+(\d+\.\d+(?:\.\d+)?)`
- NFCeTop: `NFCeTop\s+(\d+\.\d+(?:\.\d+)?)`
- Builds agrupados: `3020\.1-320\.1` (Wincash + NFeTop na mesma release)
- Wincash Web: `Wincash\s+Web\s+(\d+\.\d+(?:\.\d+)?)`
- Gsoft API: `Gsoft\s*Api(?:GUI)?\s+(\d+(?:\.\d+)?(?:\.\d+)?)` (ignorar seção `GsoftApiGUI` — produto distinto)
- WIP: `Wincash\s+Web.*WIP`, `Gsoft\s*Api.*WIP`, ou seção sem número
- Mislabel: `## Wincash 1.0.64` com PRs web → tratar como **Wincash Web 1.0.64**

Extrair números de PR dos links: `pull/(\d+)`

## Filtros por produto

### Wincash.md (desktop)

**Incluir** branch/título contendo: `wincash/` (case insensitive)

**Excluir** (não documentar no Wincash.md):

- `wincash-web`, `wincashweb`, `wincash-web/`
- `mobile`, `launcher`, `totem`, `pdvoff`, `pdv-off`
- `multicash` (salvo se PR explicitamente impacta Wincash — avaliar commits)
- `build/`, `Build Wincash`
- `doc/`, `docs/`
- `cursor/`

### NFeTop.md

**Incluir:** `nfetop/`

**Excluir:** `wincash`, `nfcetop`, `nfcetopmonitor`, `mdfetop`, `build/`, `Build NFeTop`

### NFCeTop.md

**Incluir:** `nfcetop/`, `nfcemonitor/`, `nfcetopmonitor/`

**Excluir:** `wincash`, `nfetop`, `mdfetop`, `build/`

Quando a release separar NFCeTop e NFCeMonitor, usar:

```markdown
### 305.7 (17/02/2026)
**NFCeTop**
* ``PR 523``: ...

### NFCeMonitor (01/02/2026)
* ``PR 503``: ...
```

### WincashWeb.md (Wincash Web + Gsoft API)

**Incluir Wincash Web:** `wincash-web`, `wincashweb`, `wincash-web/`, `patrick/web`

**Incluir Gsoft API:** `gsoftapi`, `gsoft-api`, `gsoft api`, `GsoftApi`

**Na seção `## Wincash Web` / `## WincashWeb` da release:** incluir também PRs `wincash/` (ex.: Balcão Web, multiempresa) — não são desktop puro.

**Excluir:**

- `wincash-web-mobile`, `mobile`, `launcher`, `totem`, `pdvoff`, `pdv-off`, `gsoftapigui`
- PRs desktop `wincash/` **fora** de seção Web na release — ficam no Wincash.md
- `build/`, `Build Gsoft API`, `Build Wincash Web`
- `wincash`, `nfetop`, `nfcetop`, `mdfetop`, `multicash`
- `doc/`, `docs/`, `cursor/`

Cabeçalho por publicação numerada (junto por release):

```markdown
### 1.0.70 / 100.1 (09/09/2026)
**Wincash Web**
* ``PR 1584``: ...

**Gsoft API**
* ``PR 1564``: ...
```

**Atribuição por versão** (mesma regra WIP dos demais produtos):

1. Percorrer releases da mais antiga à mais recente (backfill) ou posteriores à última versão documentada (incremental).
2. Filas **independentes** para Web e API; WIP → próxima versão numerada **daquele produto**.
3. Um `###` por build numerado; mesma tag com Web + API: `### {web} / {api} (DD/MM/YYYY)`.
4. Só API na tag: `### Gsoft API {versão} (DD/MM/YYYY)`.
5. Data = `publishedAt` da release em que o número foi publicado.
6. Várias tags no mesmo dia **não** se mesclam.
7. Cada PR documentado uma vez.
8. Saltos conhecidos (ex.: Web `1.0.64` → `1.0.70`, API `50.5` → `100.1`) — só na skill, **não** no `.md` público.

## PRs a ignorar sempre

- Título contém `build/` ou começa com `Build Wincash`, `Build NFeTop`, `Build Gsoft API`, `Build Wincash Web`, etc.
- Título contém `cursor/`, `skill`
- Título contém `doc/` ou `docs/` (documentação interna, não release note)
- PRs de merge/chore sem impacto ao usuário (`chore/`, `merge-`)

## Comandos gh (preferidos)

Listar releases (mais recentes primeiro):

```powershell
gh release list --repo gsoftbrasil/ERP-GSOFT --limit 80
```

Ver release (corpo com PRs) — usar o nome exato da tag (`gh release list`):

```powershell
gh release view 2026-08-05-1824 --repo gsoftbrasil/ERP-GSOFT
gh release view v2026-06-24 --repo gsoftbrasil/ERP-GSOFT
```

Detalhes do PR (preferir REST se `gh pr view` falhar por escopo de token):

```powershell
gh api repos/gsoftbrasil/ERP-GSOFT/pulls/841 --jq '{title:.title,body:.body}'
gh api repos/gsoftbrasil/ERP-GSOFT/pulls/841/commits --jq '.[].commit.message'
```

Data de publicação (ISO → DD/MM/YYYY):

```powershell
gh release view 2026-08-05-1824 --repo gsoftbrasil/ERP-GSOFT --json publishedAt
```

Windows sem PATH: `"C:\Program Files\GitHub CLI\gh.exe"`.

## Atribuição de versão (WIP → próxima)

Algoritmo:

1. Percorrer releases da mais antiga não documentada até a alvo, em ordem cronológica.
2. Se a seção cita build explícito (`## Wincash 3023.6`), associar PRs filtrados a `3023.6`.
3. Se a seção é `## Wincash WIP` ou `## Wincash` sem número, enfileirar PRs.
4. Na próxima release com build numerado, consumir a fila junto com os PRs daquela release.
5. Usar a data `publishedAt` da release onde o build foi **publicado** (não da release WIP intermediária).

Exemplos validados:

| PR | Release origem | Versão documentada |
|----|----------------|-------------------|
| 809 | `v2026-05-22-a` (Wincash WIP) | 3023.6 (`v2026-05-25`) |
| 751–754, 686, 690 | `v2026-04-28`, `v2026-04-13` (sem build) | 3022.8 |
| 800 | `v2026-05-19` (3023.3) | 3023.3 (mesmo build, release posterior à 3023.3 inicial) |

## Saltos de numeração conhecidos

Documentar nota quando aplicável (não inventar versões intermediárias):

- Wincash: 3010.16 → 3010.18 (sem 3010.17); 3010 → 3020; 3023.4 → 3023.6 (sem 3023.5); **3023.17 ausente** (build interno; documentar PRs relevantes em 3023.18)
- NFeTop: 301.17 → 305; 306 → 320

## Deduplicação Wincash.md ↔ WincashWeb.md

| Critério | Destino |
|----------|---------|
| Branch/título `wincash/` **sem** `-web` (ex.: integração NFC-e/NFSe via API no desktop) | `version/Wincash.md` |
| `wincash-web`, `wincashweb`, `gsoftapi`, `gsoft-api`, `GsoftApi` | `version/WincashWeb.md` |

- Um PR = um arquivo. Antes de inserir, buscar o número do PR nos dois `.md`.
- Exemplo: PR 841 desktop NFSe → Wincash; PR 862/913 gsoftapi → WincashWeb.

## Fallback sem `gh` autenticado

Ordem:

1. Tentar `gh release list` / `gh release view` / `gh api` (com `GH_TOKEN` ou `gh auth login`).
2. Se 401, 404 (“Could not resolve to a Repository”) ou “not logged in”:
   - `git ls-remote --tags https://github.com/gsoftbrasil/ERP-GSOFT.git`
   - Clone bare parcial (ex.: `git clone --bare --filter=blob:none`) e ler mensagens de tag / histórico `develop` com `git log --format` e `git tag --contains`
   - Data do cabeçalho: `creatordate` da tag ou `publishedAt` equivalente; formato `DD/MM/YYYY`
3. Detalhar PRs pelo título do merge `(#N)` + body do commit quando a API REST não estiver disponível.
4. No resumo final, informar que usou fallback git.

## Nova linha major

Ao detectar build `3024.x` ou tag que indique nova linha:

```markdown
# Wincash 3024
[Download](https://servidor.gsoft.com.br/wincash/3024/Wincash.exe)

### 3024.1 (DD/MM/YYYY)
* ``PR XXX``: ...
```

Inserir **acima** da seção da linha anterior. Separar com `___`.
