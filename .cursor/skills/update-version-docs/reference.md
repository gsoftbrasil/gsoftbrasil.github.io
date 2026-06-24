# Referência — update-version-docs

## Repositórios e arquivos

| Papel | Valor |
|-------|-------|
| Fonte (releases/PRs) | `gsoftbrasil/ERP-GSOFT` |
| Destino Wincash | `version/Wincash.md` |
| Destino NFeTop | `version/NFeTop.md` |
| Destino NFCeTop | `version/NFCeTop.md` |

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
| Recente | `v2026-MM-DD` (sufixo `-a` ocasional) | `v2026-06-24`, `v2026-05-22-a` |
| Antigo | número de build | `3010.15`, `3005.1` |

Corpo da release usa seções `## Wincash 3023.13`, `## NFeTop 323.2`, `## Wincash WIP`, etc.

## Detecção de build no corpo da release

Regex úteis (case insensitive):

- Wincash: `Wincash\s+(\d+\.\d+(?:\.\d+)?)`
- NFeTop: `NFeTop\s+(\d+\.\d+(?:\.\d+)?)`
- NFCeTop: `NFCeTop\s+(\d+\.\d+(?:\.\d+)?)`
- Builds agrupados: `3020\.1-320\.1` (Wincash + NFeTop na mesma release)

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

## PRs a ignorar sempre

- Título contém `build/` ou começa com `Build Wincash`, `Build NFeTop`, etc.
- Título contém `cursor/`, `skill`
- Título contém `doc/` ou `docs/` (documentação interna, não release note)
- PRs de merge/chore sem impacto ao usuário (`chore/`, `merge-`)

## Comandos gh

Listar releases (mais recentes primeiro):

```powershell
gh release list --repo gsoftbrasil/ERP-GSOFT --limit 80
```

Ver release (corpo com PRs):

```powershell
gh release view v2026-06-24 --repo gsoftbrasil/ERP-GSOFT
```

Detalhes do PR (preferir REST se `gh pr view` falhar por escopo de token):

```powershell
gh api repos/gsoftbrasil/ERP-GSOFT/pulls/841 --jq '{title:.title,body:.body}'
gh api repos/gsoftbrasil/ERP-GSOFT/pulls/841/commits --jq '.[].commit.message'
```

Data de publicação (ISO → DD/MM/YYYY):

```powershell
gh release view v2026-06-24 --repo gsoftbrasil/ERP-GSOFT --json publishedAt
```

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

- Wincash: 3010.16 → 3010.18 (sem 3010.17); 3010 → 3020; 3023.4 → 3023.6 (sem 3023.5)
- NFeTop: 301.17 → 305; 306 → 320

## Nova linha major

Ao detectar build `3024.x` ou tag que indique nova linha:

```markdown
# Wincash 3024
[Download](https://servidor.gsoft.com.br/wincash/3024/Wincash.exe)

### 3024.1 (DD/MM/YYYY)
* ``PR XXX``: ...
```

Inserir **acima** da seção da linha anterior. Separar com `___`.
