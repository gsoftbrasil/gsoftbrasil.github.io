# Exemplos — update-version-docs

Entrada (release/PR bruto) → bullet documentado. Tom: manual de usuário, português brasileiro.

---

## 1. Feature (3023.12 / PR 841)

**Release:** `v2026-06-19` — `## Wincash 3023.12`

**PR bruto:**
- Título: `Erique/wincash/feat/nfse nacional`
- Body: `Implementação no Wincash para Enviar post com payload de informação para emitir a NFSe.`

**Bullet final:**

```markdown
* ``PR 841``: Integração com **NFSe Nacional** — envio do payload para emissão via Gsoft API.
```

---

## 2. Fix WIP → próxima versão (3023.6 / PR 809)

**Release origem:** `v2026-05-22-a` — `## Wincash WIP` (sem build)

**PR bruto:**
- Título: `patrick/wincash/fix/12585/historico-estoque-codproduto-negativo`
- Commit: `Update SQL queries ... to use ABS function for CodProduto comparison`

**Próximo build:** `v2026-05-25` — `## Wincash` + `patrick/wincash/build/3023.6`

**Bullet final** (em `### 3023.6 (25/05/2026)`, não em entrada com data):

```markdown
* ``PR 809``: Correção no **relatório de histórico de estoque** quando o código do produto é negativo.
```

---

## 3. Agrupamento de releases intermediárias (3022.8)

**Situação:** PRs publicados em releases sem build (`v2026-04-28`, `v2026-04-13`) embarcados no build **3022.8** (`v2026-04-27`).

**PRs brutos:**
- 751/752: cliente Gsoft API — Access Violation
- 753/754: encoding Busca de Vendas e Reimpressão
- 686: impressão bobina — nome da impressora
- 690: exportação MGV6

**Seção final** (todos sob `### 3022.8 (27/04/2026)`):

```markdown
### 3022.8 (27/04/2026)
* ``PR 718``: Correção no relatório de produtos vendidos por classificação.
* ``PR 730`` / ``PR 731``: **Resumo de caixa** com detalhamento (fechamento de caixa).
* ``PR 745``: Cadastro de emitente ativo para NFC-e.
* ``PR 743``: Correção na devolução de consumidor final na saída.
* ``PR 751`` / ``PR 752``: Correções no cliente da Gsoft API (estabilidade e Access Violation).
* ``PR 753`` / ``PR 754``: Correções de **encoding** em Busca de Vendas e Reimpressão.
* ``PR 686``: Correção na impressão em bobina (nome da impressora).
* ``PR 690``: Correção na exportação MGV6.
```

---

## 4. Revert (3023.2 / PR 772)

**Release:** `v2026-05-06` — `## Wincash 3023.2`

**PR bruto:**
- Título: `Revert "erique/wincash/fix/melhoria_busca_requisicao (#772)"`

**Bullet final** (sem jargão "Revert", foco no efeito para o usuário):

```markdown
### 3023.2 (06/05/2026)
* Revertida a melhoria na busca de requisição (``PR 772``).
```

---

## 5. PR sem body — usar commits (3023.4 / PR 805)

**PR bruto:**
- Título: `gil/wincash-multicash-nfetop/fix/UpdateNumNFnaTitulos-BaixaParcialTransfereNumNF-PerformanceAuditor`
- Body: vazio

**Commits (resumo):**
- NumNF atualizado após transmissão de NFe
- NumNF retirado dos títulos na exclusão/cancelamento
- NumNF mantido na baixa parcial

**Bullet final:**

```markdown
* ``PR 805``: Atualização do **NumNF nos títulos** ao transmitir, cancelar ou excluir NF-e; mantém NumNF na baixa parcial; melhoria de performance no auditor.
```

---

## Anti-padrões (não publicar)

```markdown
<!-- Ruim: changelog de dev -->
* gil/wincash/feat/impressao-danfse by @gsoftdobrasil in #910

<!-- Ruim: entrada só com data -->
### (28/04/2026)
* ``PR 751``: ...

<!-- Ruim: PR de build -->
* ``PR 918``: patrick/wincash/build/3023.13
```
