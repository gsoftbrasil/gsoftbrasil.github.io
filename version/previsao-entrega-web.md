# Cronograma de migração do Wincash Desktop para Web

| Módulo                                                 | Previsão | Entrega | Observação | Rota | Ticket |
|--------------------------------------------------------|----------|---------|------------|------|----|
| 1. Cadastro                                            |-|-|-|
| 1.1 Fornecedores                                       |31/08/2026|28/08/2026||/produtos/fornecedores|12807|
| 1.2 Clientes                                           |-|-|-|
| 1.2.1 Cadastro de Clientes                             |24/06/2026|24/06/2026||/clientes/cadastro|
| 1.2.2 Grupo de Clientes                                |24/06/2026|24/06/2026||/clientes/grupos|
| 1.2.3 Categoria de Clientes                            |24/06/2026|24/06/2026||/clientes/categorias|
| 1.2.4 Gestão de Inadimplência                          |-|-|Não será desenvolvido|
| 1.3 Produtos                                           |-|-|-|
| 1.3.1 Cadastro de Produtos                             |10/04/2026|10/07/2026||/produtos/lista > ficha `/produtos/:id`|
| 1.3.2 Classificação                                    |-|-|-|
| 1.3.2.1 Setores / Grupos / Sub-Grupos / Linhas         |10/04/2026|10/07/2026||/produtos/configuracoes/classificacao/setores > placeholder; lookups em `/produtos/:id`|
| 1.3.2.2 Marca                                          |10/04/2026|10/07/2026||/produtos/configuracoes/classificacao/marcas > placeholder; lookup no cadastro|
| 1.3.2.3 Unidades de Medida                             |10/04/2026|10/07/2026||/produtos/configuracoes/classificacao/unidades > placeholder; lookup no cadastro|
| 1.3.2.4 Categorias                                     |10/04/2026|10/07/2026||/produtos/configuracoes/classificacao/categorias > placeholder; lookup no cadastro|
| 1.3.2.5 Classificação Mobile                           |31/12/2026||||12808|
| 1.3.2.6 Cores                                          |10/04/2026|10/07/2026||/produtos/cores|
| 1.3.3 Kits de Produtos (Subprodutos)                   |10/04/2026|10/07/2026||/produtos/configuracoes/kits > placeholder|
| 1.3.4 Buscar Produtos                                  |-|-|Não será desenvolvido|
| 1.3.5 Atualizar Produtos por Arquivo CSV               |-|-|Não será desenvolvido|
| 1.3.6 Exportar e Importar Produtos do CSV              |-|-|Não será desenvolvido|
| 1.3.7 Atualizar Tributação dos Produtos por CSV        |-|-|Não será desenvolvido|
| 1.4 Administrativo                                     |-|-|-|
| 1.4.1 Empresa                                          |-|-|Não será desenvolvido|
| 1.4.2 Terminais                                        |-|-|Não será desenvolvido|
| 1.4.3 Pessoal                                          |-|-|-|
| 1.4.3.1 Usuários                                       |05/03/2026|05/03/2026||/usuarios-privilegios|
| 1.4.3.2 Funcionários                                   |05/03/2026|05/03/2026|Em manutenção|/cadastro/funcionarios > canônico `/configuracoes-empresa/pessoal/funcionarios`|
| 1.4.3.3 Entregadores                                   |05/03/2026|05/03/2026||/cadastro/entregadores|
| 1.4.3.4 Contador                                       |05/03/2026|05/03/2026||/cadastro/contador|
| 1.4.3.5 Comissionamento                                |-|-|Não será desenvolvido|
| 1.4.4 Formas de Pagamento                              |30/10/2026||||12809|
| 1.4.5 Plano de Contas                                  |03/08/2026|03/08/2026||/cadastro/plano-contas|
| 1.4.6 Centro de Custos                                 |29/01/2026|29/01/2026||/financeiro/centrocustos|
| 1.4.7 Bancos/Contas-Correntes                          |31/08/2026||Redirect `/cadastro/bancos-contas-correntes` → `/financeiro/bancos-contas-correntes` sem Route||12810|
| 1.4.8 Cobrança                                         |-|-|-|
| 1.4.8.1 Cedente                                        |-|-|Não será desenvolvido|
| 1.4.9 ECFs                                             |-|-|Não será desenvolvido|
| 1.4.10 Fiscal                                          |-|-|-|
| 1.4.10.1 Regras Tributárias                            |31/12/2026||||12811|
| 1.4.10.2 ICMS / Tributos / Transp. / Convênios         |31/12/2026||||12812|
| 1.4.10.3 Operações de Entrada                          |31/12/2026||||12813|
| 1.4.11 Funções de Caixa                                |-|-|-|
| 1.4.11.1 Tickets                                       |-|-|Não será desenvolvido|
| 1.4.11.2 Cartões - TEF                                 |-|-|Não será desenvolvido|
| 1.4.11.3 Cartões - Operadoras                          |-|-|Não será desenvolvido|
| 1.4.11.4 Comandas                                      |31/12/2026||||12814|
| 1.4.11.5 Departamentos                                 |31/12/2026||||12815|
| 1.4.11.6 Operações Internas - Vendas                   |-|-|Não será desenvolvido|
| 1.4.11.7 Operações de Caixa - Formas de Pagto          |-|-|Não será desenvolvido|
| 1.4.11.8 Operações de Estoque                          |31/01/2027||||12816|
| 1.4.11.9 Enquete                                       |-|-|Não será desenvolvido|
| 1.4.12 Multi Lojas                                     |-|-|-|
| 1.4.12.1 Lojas                                         |20/08/2026|20/08/2026||/configuracoes-empresa/empresas|
| 1.4.12.2 Vincular Emitentes e Lojas                    |20/08/2026|20/08/2026||/configuracoes-empresa/emitentes-nfe|
| 1.4.13 Depósitos                                       |-|-|Não será desenvolvido|
| 1.4.14 Cadastro de Status de Entrega Simplificada      |-|-|Não será desenvolvido|
| 1.4.15 Módulos Adicionais                              |-|-|-|
| 1.4.15.1 Conexão Whatsapp                              |30/09/2026||||12817|
| 1.5 Favoritos                                          |25/02/2026|25/02/2026||/geral > seção Favoritos (estrela no menu)|
| 2. Financeiro                                          |-|-|-|
| 2.1 Movimentação Bancária - F9                         |11/06/2026|11/06/2026||/financeiro/movimentacao|
| 2.2 Tesouraria                                         |31/12/2026||||12818|
| 2.3 Contas a Receber                                   |27/04/2026|27/04/2026||/financeiro/contas-receber > abas Lista, Calendário, Baixa, Hist.|
| 2.4 Contas a Pagar - F10                               |27/04/2026|27/04/2026||/financeiro/contas-pagar > incl. recorrência e calendário|
| 2.5 Cobrança Ctrl+G                                    |-|-|-|
| 2.5.1 Gerar Boleto Bancário                            |05/08/2026|05/08/2026|Em manutenção|/financeiro/cobranca > geração de boleto|
| 2.5.2 Gerar Remessa Bancária                           |05/08/2026|05/08/2026|Em manutenção|/financeiro/cobranca > remessa CNAB|
| 2.6 Cheques                                            |-|-|-|
| 2.6.1 Cheques a Receber - F12                          |-|-|Não será desenvolvido|
| 2.6.2 Cheques a Pagar - F11                            |-|-|Não será desenvolvido|
| 2.7 Cartões                                            |-|-|Não será desenvolvido|
| 2.8 Cálculo de Juros                                   |31/12/2026||||12819|
| 2.9 Antecipação de Títulos                             |-|-|Não será desenvolvido|
| 2.9 Centro de Custos                                   |29/01/2026|29/01/2026||/financeiro/centrocustos|
| 2.10 Contas a Receber                                  |27/04/2026|27/04/2026||/financeiro/contas-receber > abas Lista, Calendário, Baixa, Hist.|
| 2.11 Entradas do Caixa                                 |-|-|Não será desenvolvido|
| 2.12 Relatórios                                        |-|-|-|
| 2.12.1 Contas a Receber                                |-|-|-|
| 2.12.1.1 Geral Completo                                |30/09/2026||||12820|
| 2.12.1.2 Período/Data Base                             |-|-|Não será desenvolvido|
| 2.12.1.3 Pendentes Geral                               |-|-|Não será desenvolvido|
| 2.12.1.4 Fechamento do Período                         |-|-|Não será desenvolvido|
| 2.12.1.5 Gestão Financeira                             |-|-|Não será desenvolvido|
| 2.12.1.6 Extrato                                       |-|-|Não será desenvolvido|
| 2.12.1.7 Itens a Receber                               |-|-|Não será desenvolvido|
| 2.12.1.8 Pagas                                         |-|-|Não será desenvolvido|
| 2.12.2 Alerta Financeiro                               |-|-|Não será desenvolvido|
| 2.12.3 Extrato Consolidado                             |30/09/2026||||12821|
| 2.12.4 Boletos Emitidos                                |-|-|Não será desenvolvido|
| 2.12.5 Movimentação Bancária                           |-|-|-|
| 2.12.5.1 Saldo Atual                                   |30/09/2026||||12822|
| 2.12.7 Cheques                                         |-|-|-|
| 2.12.7.1 Cheques a Receber                             |-|-|Não será desenvolvido|
| 2.12.8 Vendas Detalhadas de Cartões                    |30/11/2026||||12823|
| 2.12 Gsoft                                             |-|-|-|
| 2.12.1 Mensalidades                                    |-|-|-|
| 2.12.1.1 Gerar Mensalidades**                          |30/09/2026||||12824|
| 2.12.1.2 Consultar Mensalidades**                      |30/09/2026||||12825|
| 3. Vendas                                              |-|-|-|
| 3.1 Delivery Ctrl+D                                    |-|-|-|
| 3.1.1 Delivery                                         |-|-|Não será desenvolvido|
| 3.1.2 Controle de Entrega                              |-|-|Não será desenvolvido|
| 3.1.3 Relatório de Entrega                             |-|-|Não será desenvolvido|
| 3.2 Atacado Ctrl+A                                     |-|-|Não será desenvolvido|
| 3.3 Vendas Internas                                    |27/04/2026|27/04/2026|Sem rota no web atual (`/vendas/internas` removida)||
| 3.4 Balcão - F8                                        |31/08/2026|-|Em manutenção|
| 3.5 PDV Caixa - F6                                     |-|-|Não será desenvolvido|
| 3.6 Comissão de Vendas                                 |-|-|-|
| 3.6.1 Comissão Simples                                 |01/03/2027||||12826|
| 3.6.2 Comissão com Filtros                             |-|-|Não será desenvolvido|
| 3.7 Finalizar Operações de Venda                       |-|-|Não será desenvolvido|
| 3.8 Nota Fiscal de Serviços                            |27/07/2026|27/07/2026|Em manutenção|/fiscal/nfse > emitir `/fiscal/nfse/nova`; config `/fiscal/nfse/config`|
| 3.9 Vale-compras                                       |01/03/2027||||12827|
| 3.10 Permuta                                           |01/03/2027||||12828|
| 3.11 Ocorrência                                        |31/03/2027||||12829|
| 3.12 Locação                                           |31/03/2027||||12830|
| 3.13 Relatórios de Requisições                         |30/10/2026||||12831|
| 3.14 Histórico de Exclusões                            |-|-|Não será desenvolvido|
| 3.15 Buscar Vendas Ctrl+V                              |30/06/2026|30/06/2026||/vendas/consultavenda|
| 3.16 Buscar Requisições                                |30/11/2026||||12832|
| 4. Estoque                                             |-|-|-|
| 4.1 Nota Fiscal de Entrada - F7                        |10/06/2026|10/06/2026||/produtos/nota-fiscal-entrada|
| 4.2 Transferência (Dep. -> Loja)                       |31/12/2026|04/09/2026||/produtos/transferencia/dep-loja|12833|
| 4.3 Gerenciar Encomendas                               |-|-|Não será desenvolvido|
| 4.4 Controle de Entrega                                |31/01/2027||||12834|
| 4.5 Pedido de Compras                                  |10/04/2026|10/04/2026||/produtos/pedidos-compras|
| 4.6 Receber Mercadoria                                 |11/08/2026|11/08/2026||/produtos/pedidos-compras/:pedidoId/recebimento|
| 4.7 Compras por Fornecedor                             |31/01/2027||||12835|
| 4.8 Visualizar Compras por Produto                     |01/10/2026|Cancelado|Ticket Duplicado = 12845|/produtos/relatorios/compras-por-produto|
| 4.9 Pedido de Compras Web                              |-|-|Não será desenvolvido|
| 4.10 Coletar Dados                                     |-|-|Não será desenvolvido|
| 4.11 Ficha de Estoque                                  |-|-|Não será desenvolvido|
| 4.12 Lançamento Inventário                             |30/09/2026|||/produtos/inventario/lancamento|12836|
| 4.13 Consulta Inventário                               |30/09/2026|||/produtos/inventario/consulta|12837|
| 4.14 Operações de Estoque                              |30/09/2026||||12838|
| 4.15 Lançar Perdas                                     |30/09/2026||||12839|
| 4.16 Existem produtos abaixo / do estoque mínimo       |-|-|Não será desenvolvido|
| 5. Ordem de Serviços                                   |-|-|-|
| 5.1 Geral                                              |-|-|-|
| 5.1.1 Atendimento                                      |31/01/2027||||12840|
| 5.1.2 Agendamento e Manutenção                         |31/01/2027||||12841|
| 5.2 Relatórios                                         |-|-|-|
| 5.2.1 O.S Geral                                        |31/01/2027||||12842|
| 5.2.2 Detalhado por Cliente                            |-|-|Não será desenvolvido|
| 5.2.3 Relatório de Produtos e Serviços                 |-|-|Não será desenvolvido|
| 5.2.4 Comissão Múltipla por Item                       |26/02/2027||||12843|
| 6. Relatórios                                          |-|-|-|
| 6.1 Compras                                            |-|-|-|
| 6.1.1 Faturas                                          |-|-|Não será desenvolvido|
| 6.1.2 Previsão de Compras                              |04/09/2026|02/09/2026||/produtos/relatorios/previsao-compras|12844|
| 6.1.3 Compras por Produto                              |30/11/2026|10/09/2026||/produtos/relatorios/compras-por-produto|12845|
| 6.2 Produtos                                           |-|-|-|
| 6.2.1 Lista Geral                                      |30/09/2026|08/09/2026||/produtos/relatorios/geral|12846|
| 6.2.2 Produtos Vendidos                                |30/09/2026|08/09/2026||/produtos/relatorios/produtos-vendidos|12847|
| 6.2.3 Histórico do Estoque                             |-|-|Não será desenvolvido|
| 6.2.4 Giro de Estoque                                  |30/09/2026||||12848|
| 6.2.5 Sem Giro                                         |30/09/2026||||12849|
| 6.2.6 Lista Personalizada                              |-|-|Não será desenvolvido|
| 6.2.7 Por Fornecedor                                   |-|-|-|
| 6.2.7.1 Varejo                                         |-|-|Não será desenvolvido|
| 6.2.7.2 Atacado                                        |-|-|Não será desenvolvido|
| 6.2.7.3 Exportar XLS                                   |-|-|Não será desenvolvido|
| 6.2.8 Atacado                                          |-|-|-|
| 6.2.8.1 Lista Básica                                   |-|-|Não será desenvolvido|
| 6.2.8.2 Lista de Venda Externa                         |-|-|Não será desenvolvido|
| 6.2.8.3 Por Setor                                      |-|-|Não será desenvolvido|
| 6.2.9 Abaixo do Est. Mínimo                            |-|-|-|
| 6.2.9.1 Geral                                          |01/10/2026|10/09/2026||/produtos/relatorios/abaixo-est-minimo|12850|
| 6.2.9.2 Por Fornecedor                                 |-|-|Não será desenvolvido|
| 6.2.9.2.1 Loja                                         |-|-|Não será desenvolvido|
| 6.2.9.2.2 Depósito                                     |-|-|Não será desenvolvido|
| 6.2.10 Em Promoção                                     |31/12/2026||||12851|
| 6.2.11 Alterados                                       |31/12/2026|08/09/2026||/produtos/relatorios/alterados|12852|
| 6.2.12 Compostos                                       |09/10/2026||||12975|
| 6.2.13 Inventário                                      |-|-|-|
| 6.2.13.1 Balanço Estoque/Loja                          |28/08/2026|28/08/2026||/produtos/relatorios/balanco-estoque|12853|
| 6.2.13.2 Inventário - Modelo 1                         |-|-|Não será desenvolvido|
| 6.2.13.3 Inventário - Modelo 2                         |-|-|Não será desenvolvido|
| 6.2.13.4 Inventário Manual                             |-|-|Não será desenvolvido|
| 6.2.13.5 Inventário - Hist. Estoque                    |30/09/2026||||12854|
| 6.2.13.6 Inventário - Diferença                        |16/10/2026||||12976|
| 6.2.13.7 Inventário - Contábil                         |-|-|Não será desenvolvido|
| 6.2.14 Lista de Preços                                 |01/10/2026||||12977|
| 6.2.14.1 Lista Completa                                |-|-|Não será desenvolvido|
| 6.2.14.2 Tabela de Preços                              |-|-|Não será desenvolvido|
| 6.2.14.3 Por Setor                                     |-|-|Não será desenvolvido|
| 6.2.14.3.1 Varejo                                      |-|-|Não será desenvolvido|
| 6.2.14.3.2 Promocional                                 |-|-|Não será desenvolvido|
| 6.2.15 Relatório de Classificação de Produtos          |-|-|Não será desenvolvido|
| 6.2.16 Ajustes de produtos                             |01/10/2026|08/09/2026||/produtos/relatorios/ajustes-produtos|12978|
| 6.2.17 Controle de Lotes                               |-|-|-|
| 6.2.17.1 Clientes por Lote                             |25/02/2027||||12855|
| 6.2.17.2 Lotes por Cliente                             |25/02/2027||||12856|
| 6.2.17.3 Lotes por Produto                             |25/02/2027||||12857|
| 6.2.17.4 Lotes por Vencimento                          |25/02/2027||||12858|
| 6.2.18 Por Grade                                       |-|-|Não será desenvolvido|
| 6.2.19 Por Data de Validade                            |30/09/2026|03/09/2026||/produtos/relatorios/validade|12859|
| 6.2.20 Vendidos por Classificação Mercadológica        |-|-|Não será desenvolvido|
| 6.2.21 Lançamento de Perdas                            |30/09/2026|08/09/2026||/produtos/relatorios/lancamento-perdas|12860|
| 6.2.22 Produtos Vendidos por Fornecedor                |-|-|Não será desenvolvido|
| 6.2.23 Com fotos                                       |-|-|Não será desenvolvido|
| 6.2.24 Por Cor                                         |30/09/2026|08/09/2026||/produtos/relatorios/por-cor|12861|
| 6.2.25 Tabela de Preços Produtos                       |-|-|Não será desenvolvido|
| 6.2.26 Análise de Rentabilidade                        |31/12/2026||||12862|
| 6.2.27 Produtos - Classificação Fiscal                 |-|-|Não será desenvolvido|
| 6.3 Fornecedores                                       |-|-|Não será desenvolvido|
| 6.4 Clientes                                           |-|-|-|
| 6.4.1 Lista Geral                                      |31/03/2027|08/09/2026||/clientes/relatorios/lista-geral|12863|
| 6.4.2 Aniversariantes                                  |-|-|Não será desenvolvido|
| 6.4.3 Acima do Limite                                  |31/03/2027||||12864|
| 6.4.4 Volume de Vendas por Produto                     |-|-|Não será desenvolvido|
| 6.4.5 Curva ABC de Clientes                            |-|-|Não será desenvolvido|
| 6.4.6 Data base - Vencimento                           |-|-|Não será desenvolvido|
| 6.4.7 Alerta de Aniversariantes do Dia                 |-|-|Não será desenvolvido|
| 6.4.8 Por Data de Cadastro                             |-|-|Não será desenvolvido|
| 6.4.9 Que Não Compraram Entre o Período                |31/03/2027|10/09/2026||/clientes/relatorios/nao-compraram-periodo|12865|
| 6.4.10 Média de Atraso de Pagamento Por Cliente        |31/03/2027||||12866|
| 6.4.11 Média do Dia que Realiza Pedidos                |-|-|Não será desenvolvido|
| 6.4.12 Enquete                                         |-|-|Não será desenvolvido|
| 6.4.13 Enquete Detalhado                               |-|-|Não será desenvolvido|
| 6.4.14 Créditos dos Clientes                           |-|-|-|
| 6.4.14.1 Por Devoluções                                |31/03/2027||||12867|
| 6.4.14.2 Por Vale-Compras                              |31/03/2027||||12868|
| 6.4.15 Pesquisa NPS                                    |31/03/2027||||12869|
| 6.4.16 CashBack                                        |31/12/2026||||12870|
| 6.6 Operações de Estoque                               |30/09/2026||||12871|
| 6.7 Dem. de Vendas                                     |-|-|-|
| 6.7.1 Vendas Detalhado                                 |17/08/2026|17/08/2026||/vendas/relatorios/demonstrativo-vendas|
| 6.7.2 Vendas Detalhado Com Itens                       |04/09/2026||/vendas/relatorios/vendas-detalhado-com-itens|12872|
| 6.7.3 Vendas Detalhado Por Forma de Pagto e NFe        |-|-|Não será desenvolvido|
| 6.7.4 Análise Diária de Vendas por Produto             |30/11/2026||||12873|
| 6.7.5 Por Categoria Resumido                           |-|-|Não será desenvolvido|
| 6.7.6 Resumo de Vendas por PIS/COFINS                  |-|-|Não será desenvolvido|
| 6.7.7 Vendas por Produto/Serviço - Resumidas           |-|-|Não será desenvolvido|
| 6.7.8 Vendas por Produto/Serviço - Detalhadas          |-|-|Não será desenvolvido|
| 6.7.9 Vendas no Horário                                |30/11/2026||||12874|
| 6.7.10 Venda Bruta por Período                         |-|-|Não será desenvolvido|
| 6.7.11 Montante Vend/Orc Por Grupo                     |-|-|Não será desenvolvido|
| 6.7.12 Produtos Vendidos Na Promoção                   |30/11/2026||||12875|
| 6.7.13 Vendas Canceladas                               |30/11/2026||||12876|
| 6.7.14 Vendas com Devoluções                           |30/11/2026||||12877|
| 6.7.15 Itens Devolvidos                                |30/11/2026||||12878|
| 6.7.16 Vendas Detalhadas por Quantidade e Grade        |-|-|Não será desenvolvido|
| 6.7.17 Produtos Vendidos por Forma de Pagamento        |30/11/2026||||12879|
| 6.7.18 Orçamentos Perdidos - Motivos                   |30/11/2026|09/09/2026||/vendas/relatorios/orcamentos-perdidos|12880|
| 6.7.19 Orçamentos - Etapas                             |05/05/2026|05/05/2026||/vendas/orcamentos/fluxo > operação; relatório `/vendas/relatorios/orcamentos-fluxo`|
| 6.7.20 Vendas com Comissão Múltipla                    |-|-|Não será desenvolvido|
| 6.7.21 Vendas por Rota                                 |30/11/2026||||12881|
| 6.7.22 Média de Gastos por Cliente                     |-|-|Não será desenvolvido|
| 6.7.23 Relatório Anual de Vendas por Classificação     |30/11/2026|09/09/2026||/vendas/relatorios/anual-classificacao|12882|
| 6.7.24 Relatório Anual de Vendas por Vendedor          |30/11/2026||||12883|
| 6.7.25 Relatório Anual por Itens                       |30/11/2026||||12884|
| 6.7.26 Relatório de Vendas por Cliente e Fornecedor    |30/11/2026|10/09/2026||/vendas/relatorios/vendas-cliente-fornecedor|12885|
| 6.7.27 Relatório de Vendas Com Desconto                |30/11/2026||||12886|
| 6.7.28 Relatório de Vendas Semanal                     |30/11/2026||||12887|
| 6.8 GFood                                              |-|-|-|
| 6.8.1 Delivery / GFood                                 |-|-|Não será desenvolvido|
| 6.8.2 GFood - Itens cancelados por Data / Núm. Caixa   |-|-|Não será desenvolvido|
| 6.8.3 Produção dos Garçons                             |-|-|Não será desenvolvido|
| 6.8.4 Couvert                                          |-|-|Não será desenvolvido|
| 6.8.5 Comissão Garçom                                  |-|-|Não será desenvolvido|
| 6.8.6 Vendas Delivery                                  |-|-|Não será desenvolvido|
| 6.8.7 GFood - Atendimentos                             |-|-|Não será desenvolvido|
| 6.8.8 Produtos Vendidos                                |-|-|Não será desenvolvido|
| 6.9 Fiscal                                             |-|-|-|
| 6.9.1 CFe                                              |-|-|Não será desenvolvido|
| 6.9.2 ECF                                              |-|-|Não será desenvolvido|
| 6.9.3 ICMS - Pis/Cofins                                |-|-|Não será desenvolvido|
| 6.9.4 NFe de Venda                                     |-|-|Não será desenvolvido|
| 6.9.5 Sintegra                                         |-|-|Não será desenvolvido|
| 6.9.6 Produtos Vendidos                                |-|-|Não será desenvolvido|
| 6.9.7 Resumo Fiscal                                    |-|-|Não será desenvolvido|
| 6.9.8 Vendas sem cupom                                 |-|-|Não será desenvolvido|
| 6.10 Dem. de Caixa                                     |-|-|-|
| 6.10.1 Movimento de Caixa Detalhado                    |30/11/2026||||12888|
| 6.10.2 Movimento de Caixa por Categoria                |30/11/2026||||12889|
| 6.10.3 Saldo Atual dos Caixas Abertos                  |30/11/2026||||12890|
| 6.10.4 Resumo de Movimento de Caixa                    |30/11/2026||||12891|
| 6.10.5 Quebra de Caixa                                 |30/11/2026||||12892|
| 6.11 Dashboard                                         |-|-|Não será desenvolvido|
| 7. Utilitários                                         |-|-|-|
| 7.1 Comunicação Transmissão                            |-|-|-|
| 7.1.1 Balança                                          |31/12/2026|08/09/2026||/produtos/carga-balanca (Web em Produtos > Outros; Desktop Utilitários)|12893|
| 7.1.2 Verificador de Preços                            |-|-|Não será desenvolvido|
| 7.1.3 Impressora de Código de Barras                   |31/03/2027||||12894|
| 7.1.4 Etiquetas de Bobina                              |31/03/2027||||12895|
| 7.2 WinCash Analyzer                                   |-|-|Não será desenvolvido|
| 7.3 Calculadora                                        |-|-|Não será desenvolvido|
| 7.4 Agenda Telefônica                                  |-|-|Não será desenvolvido|
| 7.5 Backup                                             |-|-|Não será desenvolvido|
| 7.6 Painel                                             |-|-|-|
| 7.6.1 Configurações Regionais                          |-|-|Não será desenvolvido|
| 7.6.2 Opções de Acessibilidade                         |-|-|Não será desenvolvido|
| 7.6.3 Data e Hora                                      |-|-|Não será desenvolvido|
| 7.6.4 Conexões de Rede                                 |-|-|Não será desenvolvido|
| 7.6.5 Propriedades do Sistema                          |-|-|Não será desenvolvido|
| 7.6.6 Propriedades de Vídeo                            |-|-|Não será desenvolvido|
| 7.7 Configurações                                      |29/01/2026|29/01/2026||/configuracoes-empresa > auditoria transversal em cadastros/financeiro|
| 7.8 Integração                                         |-|-|-|
| 7.8.1 Sistema Parametriza - Sincronização              |-|-|Não será desenvolvido|
| 7.8.2 Exportar Cadastros - Criare Sales                |-|-|Não será desenvolvido|
| 7.8.3 Importar Pedidos - Criare Sales                  |-|-|Não será desenvolvido|
| 7.8.4 Exportar Produtos - GColetor                     |-|-|Não será desenvolvido|
| 7.8.5 Exportar dados - BI Machine                      |-|-|Não será desenvolvido|
| 7.8.6 Exportar vendas                                  |-|-|Não será desenvolvido|
| 8. Apoio à Decisão                                     |-|-|-|
| 8.1 Curva ABC                                          |-|-|-|
| 8.1.1 Curva ABC de Vendas                              |31/08/2026|28/08/2026||/relatorios/curva-abc/vendas|12896|
| 8.1.2 Curva ABC de Clientes/Grupo/Rota                 |31/08/2026|28/08/2026||/relatorios/curva-abc/clientes-grupo-rota|12897|
| 8.1.3 Curva ABC de Vendedores                          |31/08/2026|28/08/2026||/relatorios/curva-abc/vendedores|12898|
| 8.1.4 Cuva ABC de Perdas                               |31/08/2026|28/08/2026||/relatorios/curva-abc/perdas|12899|
| 8.2 Fluxo de Caixa                                     |31/08/2026||||12900|
| 8.3 DRE                                                |31/08/2026|||/relatorios/dre|12901|
| 8.4 Mapa de Vendas                                     |31/08/2026||||12902|
| 8.6 Painel de Metas                                    |31/12/2026|14/09/2026|/vendas/painel-metas|12903|
| 8.7 Auditoria                                          |-|-|-|
| 8.7.1 Auditor do Sistema                               |30/09/2026||||12904|
| 8.7.2 Estoque                                          |-|-|-|
| 8.7.2.1 Comparativo Cadastro x Histórico               |-|-|Não será desenvolvido|
| 8.7.3 Produtos                                         |16/10/2026|||12981|


# Legenda:
- `**`: Módulos internos da Gsoft
- `-`: Detalhado no submenu
