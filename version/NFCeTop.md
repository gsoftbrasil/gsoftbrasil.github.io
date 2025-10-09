# NFCeTop 301

### 301.2
09/10/2025
* [PR] 9374 -  Feat/Fechar NFCeTop automaticamente by @fabiaalv3s in https://github.com/gsoftbrasil/ERP-GSOFT/pull/285
* [PR] Patrick/nfcetop/contingencia by @patrick9as in https://github.com/gsoftbrasil/ERP-GSOFT/pull/287
* [PR] patrick/nfcetop/301.2 by @patrick9as in https://github.com/gsoftbrasil/ERP-GSOFT/pull/288

___

# NFCeTop 300

### 300.3
17/09/2025
* O sistema não entra mais em modo de contingência em mensagens de erro.

### 300.2
03/09/2025
- Inutilização de números em massa no NFCeTop.

___

# NFCeTop 106

### 106.2
21/08/2025
- Criada configuração para não permitir que o NFCeTop vá para a bandeja do Windows.

### 106.1 
23/07/2025
Ticket 9260 - Ausência de troco no cupom
Agora, ao finalizar uma venda, os seguintes dados essenciais serão copiados para uma nova tabela chamada NFe_Titulos:
- Codigo, CodTitulo, CodVenda, CodCliente, Emissao, Vencimento, Valor, ValorRecebido, Recebimento, Desconto, NumDocto, CodFormaPagto e FormaPagto.
- O objetivo é preservar os dados originais da venda, evitando inconsistências durante a emissão do cupom fiscal. Anteriormente, em casos de recebimentos parciais, ocorria o erro "Ausência de troco na emissão do cupom", pois eram gerados múltiplos títulos com valores diferentes do valor original da venda. Com essa nova abordagem, os dados são fixados no momento do fechamento da venda, garantindo maior integridade e consistência na geração do cupom.
