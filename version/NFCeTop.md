# NFCeTop 301
[Download](https://servidor.gsoft.com.br/NFCeTop/301/NFCeTop.exe)
### 301.2
09/10/2025
* ``Ticket 9374``: Criado parâmetro para fechar o NFCeTop automaticamente quando não houver uma instância do Wincash ativa.
* ``Ticket 287``: Aprimoramento do modo contingência.
* ``PR 288``: Corrigido filtro de notas pendentes ao excluir registros não utilizados na retransmissão do cupom.

___

# NFCeTop 300
[Download](https://servidor.gsoft.com.br/NFCeTop/300/NFCeTop.exe)
### 300.3
17/09/2025
* ``PR 257``: O sistema não entra mais em modo de contingência em mensagens de erro.

### 300.2
03/09/2025
- Inutilização de números em massa no NFCeTop.

___

# NFCeTop 106
[Download](https://servidor.gsoft.com.br/NFCeTop/106/NFCeTop.exe)

### 106.2
21/08/2025
- Criada configuração para não permitir que o NFCeTop vá para a bandeja do Windows.

### 106.1 
23/07/2025

``Ticket 9260``
- Agora, ao finalizar uma venda, os seguintes dados essenciais serão copiados para uma nova tabela chamada NFe_Titulos
  - Codigo, CodTitulo, CodVenda, CodCliente, Emissao, Vencimento, Valor, ValorRecebido, Recebimento, Desconto, NumDocto, CodFormaPagto e FormaPagto.
  - O objetivo é preservar os dados originais da venda, evitando inconsistências durante a emissão do cupom fiscal. Anteriormente, em casos de recebimentos parciais, ocorria o erro "Ausência de troco na emissão do cupom", pois eram gerados múltiplos títulos com valores diferentes do valor original da venda. Com essa nova abordagem, os dados são fixados no momento do fechamento da venda, garantindo maior integridade e consistência na geração do cupom.
