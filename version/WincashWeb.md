# Wincash Web

Esta página reúne as alterações do **Wincash Web** e da **Gsoft API** (serviço local de integração).
A atualização é automática — não há download manual.

### 1.0.76 / 105.3 (21/09/2026)
**Wincash Web**
* ``PR 1638``: O **balcão** e o ajuste de estoque passam a respeitar a configuração **Permitir estoque negativo**.
* ``PR 1640``: Exibição de **markup e margem** no balcão, com os custos da formação de preço.
* ``PR 1641``: Melhorias na interface do **balcão** — rodapé, total no tema escuro e busca (F7) com painel de itens.
* ``PR 1577``: Relatório de **vendas por horário**.
* ``PR 1617``: Módulo de **operações de estoque** — transferências entre lojas e movimento simples.
* ``PR 1576``: Relatório de **vendas por rota**.
* ``PR 1643``: Relatório de **giro de estoque**.
* ``PR 1650``: Atualização visual do **design system** das telas.
* ``PR 1645``: Relatório de **inventário — diferença**.
* ``PR 1649``: Na **Curva ABC de vendas**, filtro por subgrupo e consulta de fornecedor.
* ``PR 1651``: Correção na **NF de entrada** — aviso claro quando o serviço fiscal está indisponível; melhor tratamento do NCM.
* ``PR 1653``: Relatório de **inventário — histórico de estoque**.
**Gsoft API**
* ``PR 1654``: Correção na emissão de **NFC-e** — evita loop e melhora a mensagem de rejeição da Sefaz.

### Gsoft API 105.2 (21/09/2026)
**Gsoft API**
* ``PR 1639``: Correção na atualização em segundo plano do **código da loja** — evita travar a API na inicialização.

### 1.0.75 / 105.1 (15/09/2026)
**Wincash Web**
* ``PR 1631``: Relatório de produtos **sem giro**.
* ``PR 1618``: Módulo **Lançar Perdas** — registro e processamento de perdas de estoque.
* ``PR 1634``: Correção no **Inventário** — as consultas voltam a funcionar corretamente.

### 1.0.73 / 103.1 (14/09/2026)
**Wincash Web**
* ``PR 1594``: Relatório de **orçamentos perdidos**.
* ``PR 1595``: Relatório **anual de vendas por classificação**.
* ``PR 1605``: Relatório de **compras por produto**.
* ``PR 1609``: Relatório de clientes que **não compraram no período**.
* ``PR 1612``: Relatório de **vendas por cliente e fornecedor**.
* ``PR 1555``: Relatório de produtos **abaixo do estoque mínimo**.
* ``PR 1553``: Relatório de **vendas detalhado com itens**.
* ``PR 1616``: Cards e relatórios no menu passam a respeitar corretamente os **privilégios** do usuário.
* ``PR 1559``: **Painel de Metas** no módulo de Vendas.
* ``PR 1575``: Consulta do **Auditor do Sistema** nas configurações.
* ``PR 1619``: Correção do **logo do banco** na emissão de boletos.

### 1.0.72 / 102.1 (10/09/2026)
**Wincash Web**
* ``PR 1599``: Exibição da **cor do produto** no relatório de Previsão de Compras.
* ``PR 1601``: Seleção de **centro de custo** nas contas a pagar geradas pela NF de entrada.
* ``PR 1602``: Possibilidade de **inativar produtos** diretamente na lista de produtos.
* ``PR 1606``: Correção do **XML da NFS-e** que era gravado incompleto; suporte à geração do **DANFSe**.
* ``PR 1607``: Correção do **código do cliente** na emissão de NFS-e — usa o cliente do título quando necessário.
* ``PR 1610``: Textos longos truncados passam a exibir o conteúdo completo ao passar o mouse.
**Gsoft API**
* ``PR 1603``: Correção na baixa de Contas a Pagar de **recorrência** (loja do título).
* ``PR 1604``: Correção na **consulta de produtos** do Pedido de Compras com filtro por fornecedor.

### 1.0.71 / 101.2 (10/09/2026)
**Wincash Web**
* ``PR 1580``: Relatório de **produtos ajustados**.
* ``PR 1581``: Relatório **Lista Geral de clientes**.
**Gsoft API**
* ``PR 1593``: Correção na emissão fiscal e nos erros do **manifesto** DF-e.

### 1.0.70 / 100.1 (09/09/2026)
**Wincash Web**
* ``PR 1519`` / ``PR 1520``: **Inventário** no Wincash Web — lançamento e consulta com paridade ao desktop.
* ``PR 1522``: Gestão de **boletos** na Cobrança — abas, remessa em lote e alteração de títulos.
* ``PR 1523``: Atualização visual do **design system** das telas.
* ``PR 1524``: Correção da tela em branco na **Cobrança**.
* ``PR 1528``: Ajuste na organização dos **indicadores** e comunicados na página inicial.
* ``PR 1533``: Organização dos **custos de compra e de venda** na formação de preço da NF de entrada.
* ``PR 1536``: Consulta de **histórico de preços** no cadastro de produtos.
* ``PR 1537``: Transferência de produtos **entre departamentos da mesma loja**.
* ``PR 1543``: Relatório **Lista Geral** de produtos.
* ``PR 1544``: Relatório de produtos por **validade**.
* ``PR 1545``: Ajustes visuais em telas do Wincash Web.
* ``PR 1546``: Relatório de **produtos vendidos**.
* ``PR 1547``: Previsão do **tempo** na página inicial.
* ``PR 1550``: Integração com **balança** no cadastro de produtos.
* ``PR 1552``: Foto do produto no **Balcão Web** (grade e impressão).
* ``PR 1554``: Novo módulo **GAF** no Wincash Web.
* ``PR 1561``: Relatório **DRE** (Demonstrativo de Resultado) no Wincash Web.
* ``PR 1565``: Coluna de **recebimento** em Contas a Receber.
* ``PR 1566``: Correção da **recorrência** em Contas a Pagar por loja.
* ``PR 1568``: Relatório de produtos **por cor**.
* ``PR 1569``: Relatório de produtos **alterados**.
* ``PR 1573``: Relatório de **lançamento de perdas**.
* ``PR 1582``: Correção do relatório de **Prazo Médio de Pagamento** no escopo por empresa.
* ``PR 1583``: Correção de acesso e filtros no relatório **Curva ABC de Compras**.
* ``PR 1584``: Total geral na tela de **NF de entrada**.
**Gsoft API**
* ``PR 1564``: Correção na transferência de produtos **entre empresas**.

### 1.0.64 / 50.5 (02/09/2026)
**Wincash Web**
* ``PR 1509``: Melhorias em Contas a Pagar/Receber — filtros que persistem ao voltar; situação e totais de recebimento.
**Gsoft API**
* ``PR 1513``: Preenchimento automático de **loja** em registros sem loja na inicialização da API.

### 1.0.63 / 50.3 (02/09/2026)
**Wincash Web**
* ``PR 1506``: Correção do filtro por **loja** em Contas a Pagar e Contas a Receber.

### 1.0.62 / 50.2 (02/09/2026)
**Wincash Web**
* ``PR 1430``: Relatório **Curva ABC de Vendas**.
* ``PR 1431``: Relatório **Curva ABC de Clientes** (grupo/rota e inadimplência).
* ``PR 1432``: Relatório **Curva ABC de Vendedores**.
* ``PR 1433``: Relatório **Curva ABC de Perdas**.
* ``PR 1457``: Cadastro de **fornecedores** (incluindo CNPJ alfanumérico).
* ``PR 1461`` / ``PR 1466``: Continuação da **NF de entrada** — atualização de produtos, lançamento/exclusão de item manual e exclusão de nota em conferência.
* ``PR 1468``: **Consulta de produtos** paginada (busca e ordenação no servidor).
* ``PR 1469``: Continuação da **NF de entrada** — atualização de produtos, lançamento/exclusão de item manual e exclusão de nota em conferência.
* ``PR 1470``: Continuação do **Balcão Web** — navegação por teclado no fechamento, busca de pedidos/requisições e estoque da loja no resumo.
* ``PR 1476`` / ``PR 1477`` / ``PR 1478`` / ``PR 1479`` / ``PR 1480`` / ``PR 1481`` / ``PR 1482`` / ``PR 1483`` / ``PR 1484`` / ``PR 1485``: **Multiempresa** — escopo por loja/empresa em Contas a Pagar/Receber, movimentação bancária, cobrança, consulta consolidada, dashboard e grupos de empresas.
* ``PR 1486``: Continuação do **Balcão Web** — navegação por teclado no fechamento, busca de pedidos/requisições e estoque da loja no resumo.
* ``PR 1489`` / ``PR 1490`` / ``PR 1492`` / ``PR 1501`` / ``PR 1502``: Ajustes de **escopo multiempresa**, privilégios na interface e ativação do recurso.
* ``PR 1503``: Continuação do **Balcão Web** — navegação por teclado no fechamento, busca de pedidos/requisições e estoque da loja no resumo.
* ``PR 1504``: Relatório **Previsão de Compras**.

### 1.0.60 / 47.1 (28/08/2026)
**Wincash Web**
* ``PR 1429``: Continuação da **NF de entrada** — abas, formação de preço/custo e desfazer entrada com progresso.
* ``PR 1439``: Consulta de **plano de contas** em Contas a Pagar — inclui contas pai e botão Buscar (paridade com o desktop).
* ``PR 1440``: Correção no **estorno** de Contas a Pagar e na exclusão na movimentação bancária (vínculos corretos).
* ``PR 1441``: Continuação da **NF de entrada** — abas, formação de preço/custo e desfazer entrada com progresso.
* ``PR 1442``: Indicador **Top produtos comprados** alinhado às notas lançadas no desktop.
* ``PR 1446``: Relatório **Balanço de estoque** — filtros, totais, Excel e impressão.
* ``PR 1453``: Continuação da **NF de entrada** — abas, formação de preço/custo e desfazer entrada com progresso.
**Gsoft API**
* ``PR 1436``: Sincronização automática do **manifesto DF-e** (a cada 3 horas, fora da madrugada).
* ``PR 1444``: Correção no **parcelamento** de Contas a Pagar gerado a partir da NF de entrada.

### 1.0.58 / 46.1 (27/08/2026)
**Wincash Web**
* ``PR 1363``: Melhoria de desempenho nas fotos do **Patrimônio** — miniatura na lista e imagem completa só no zoom.
* ``PR 1365``: Fotos do **Patrimônio** gravadas em disco, com melhor desempenho.
* ``PR 1371``: Filtros por **categoria** e **departamento** na listagem de bens do Patrimônio.
* ``PR 1379`` / ``PR 1380``: Novo **Balcão Web** — lançamento de itens, fechamento (F9), formas e condições de pagamento, lookup de cliente e comprovante.
* ``PR 1383``: **Home** com launchpad de indicadores e comunicados.
* ``PR 1385``: Continuação do **Balcão Web** (fase P1) — crédito/cashback, acréscimo, entrega, tabela de preço, cadastro rápido de cliente e fechamento em etapas.
* ``PR 1386``: Correção de lentidão e travamentos em formulários.
* ``PR 1387`` / ``PR 1389``: Continuação do **Balcão Web** (fase P1) — crédito/cashback, acréscimo, entrega, tabela de preço, cadastro rápido de cliente e fechamento em etapas.
* ``PR 1394``: Intervalo do carrossel de comunicados ajustado para 12 segundos.
* ``PR 1395``: Imagem do comunicado sem corte na home.
* ``PR 1405``: Total de **crédito de devolução** no Demonstrativo de Vendas alinhado ao desktop.
* ``PR 1415``: Continuação do **Balcão Web** (fase P2) — baixa de estoque, desconto/acréscimo no F9 e finalização do pagamento.
* ``PR 1420``: Campo **tipo de ambiente** (produção/homologação) no cadastro de emitente de NF-e.
* ``PR 1421``: Reformulação da **NF de entrada** — preview, filtros, manifesto e formação de preço.

### Gsoft API 45.1 (25/08/2026)
**Gsoft API**
* ``PR 1375``: Cálculo de **IBS e CBS** na emissão de NF-e e NFC-e pela API.
* ``PR 1398``: Ordem manual de **produtos e complementos** no cardápio digital.

### 1.0.57 / 42.3 (21/08/2026)
**Wincash Web**
* ``PR 1354``: **Recorrência** em Contas a Pagar — geração e reposição do título ao pagar.
* ``PR 1356``: Destino **PDV/Banco** em Contas a Pagar alinhado ao desktop; correção no lookup sem código órfão.
* ``PR 1358``: Módulos **Patrimônio** e **iFood** passam a ser opcionais (contratáveis); ajustes em Contas a Pagar e menu Fiscal.
* ``PR 1360``: Relatório de **Prazo Médio de Pagamento** — valor a vencer, filtro por tipo de data e detalhe dos títulos da nota.

### 1.0.56 / 42.2 (20/08/2026)
**Wincash Web**
* ``PR 1347``: Correção na pré-visualização do **XML de NF de entrada** via túnel.

### 1.0.55 / 42.1 (20/08/2026)
**Wincash Web**
* ``PR 1326``: Cadastro de **lojas** nas configurações do Wincash Web.
* ``PR 1329``: Melhorias em **Consultar Vendas** — período na barra e listagem somente após buscar; reorganização dos cards de relatórios.
* ``PR 1345``: Cadastro de **emitentes de NF-e** e certificado no Wincash Web (evita pedir o arquivo a cada nota).

### Gsoft API 40.3 (20/08/2026)
**Gsoft API**
* ``PR 1330``: Impede duas instâncias do **túnel Gsoft** na mesma origem.
* ``PR 1335``: Impede uma segunda instância da **Gsoft API** na mesma pasta.

### 1.0.54 / 40.2 (19/08/2026)
**Wincash Web**
* ``PR 1324``: Correção na configuração financeira com envio correto da **loja**.
* ``PR 1325``: Correção do **crédito de devolução** no Demonstrativo de Vendas; lista só vendedores ativos.
**Gsoft API**
* ``PR 1322``: Encerramento controlado da API com identificação da origem.
* ``PR 1323``: Correção na listagem de **NF de entrada** quando a loja está nula ou zerada.

### 1.0.53 / 40.1 (19/08/2026)
**Wincash Web**
* ``PR 1274``: Relatório **Demonstrativo de Vendas** no Wincash Web (valores, CMV, markup, lucro e crédito).
* ``PR 1282``: Correção na atualização de privilégios do **Demonstrativo de Vendas**.
* ``PR 1285``: Correção no lançamento de **movimentação bancária** (privilégios e loja).
* ``PR 1290``: Correção de mensagem truncada e rolagem no **lançamento bancário** (plano de contas).
* ``PR 1291``: Correções na **movimentação bancária**.
* ``PR 1292``: Total do filtro no **rodapé** de Contas a Receber e Contas a Pagar (todos os títulos, não só a página).
* ``PR 1294``: Total do filtro no **rodapé** de Contas a Receber e Contas a Pagar (todos os títulos, não só a página).
* ``PR 1302``: Autenticação do **túnel Gsoft** por CNPJ e MAC.
* ``PR 1319``: Correção de **datas** e lookup de **vendedor** no Demonstrativo de Vendas.
* ``PR 1320``: Ações de produto (**Definir cor**, **Alterar preço**, **Inserir código de barras**) ocultas sem privilégio de edição.
**Gsoft API**
* ``PR 1293``: Suporte ao relatório de **Prazo Médio de Pagamento** na API.

### 1.0.51 (16/08/2026)
**Wincash Web**
* ``PR 1271``: **Privilégios por loja** — controle de acesso separado por unidade.

### 1.0.50 (14/08/2026)
**Wincash Web**
* ``PR 1128``: Melhorias no módulo **Patrimônio** — cadastro de departamentos, código sequencial único e ajustes em transferências e movimentações.
* ``PR 1129``: Melhorias em **Contas a Pagar** — consulta de contas/fornecedor, confirmações por diálogo e data de pagamento somente leitura.
* ``PR 1130``: Correção do **saldo anterior** na movimentação bancária.
* ``PR 1160``: Correção na **data de pagamento** em Contas a Pagar (grava somente a data, sem hora).
* ``PR 1161``: Tipos de documento em **Contas a Pagar** alinhados ao desktop (DNH, BOL, CRT, DBT, NOT e OUT).
* ``PR 1162``: Filtros de data com **mês corrente** por padrão e memória do período escolhido (Contas a Receber/Pagar, movimentação bancária e pedido de compras).
* ``PR 1163``: Padronização do **Pedido de Compras** — alinhado ao desktop (tempo de entrega, sugestão, peso e consulta de produtos).
* ``PR 1166``: Integração **FGF Tributária** — módulo contratável com base de produtos e sincronização com o parceiro.
* ``PR 1170``: Processamento automático da **FGF Tributária** — sincronização periódica e registro do último envio e da última aplicação.
* ``PR 1177``: **Auditoria** das alterações no Wincash Web (cadastros e financeiro) e **senha do dia** para acessar as configurações.

### 1.0.30 (07/08/2026)
**Wincash Web**
* ``PR 1121``: Novo módulo **Patrimônio** — cadastro de bens com foto, movimentações e histórico (comodato, empréstimo, transferência, manutenção, ajuste e baixa).

### 1.0.30 (06/08/2026)
**Wincash Web**
* ``PR 1107``: Padronização de **datas**; correções de saldo bancário, competência e centro de custos em Contas a Pagar.

### 1.0.28 / 21.1 (06/08/2026)
**Wincash Web**
* ``PR 1096``: Melhorias no **lançamento de Contas a Pagar** — formulário com tipo/número da NF, usuário, data e centro de custo; descrição alinhada ao plano de contas; coluna Plano de contas com tooltip.
* ``PR 1103``: Correção na **barra de seleção** das listagens.
* ``PR 1106``: Acesso local ao **Wincash Web** via **túnel Gsoft** — a interface passa a ser servida pelo próprio túnel.
**Gsoft API**
* ``PR 1104``: Correção de **referência repetida** na API.

### 1.0.25 / 20.1 (05/08/2026)
**Wincash Web**
* ``PR 1080``: Ampliação dos filtros avançados em **Contas a Receber** (região, categoria, forma de pagamento, cedente e período de recebimento); melhorias na listagem de clientes.
* ``PR 1090``: Módulo de **Cobrança** — consulta e geração de boletos, remessa e retorno CNAB, envio por e-mail e WhatsApp.
* ``PR 1091``: Melhorias no módulo **NFSe** — filtro por período, alíquota de ISS do emitente e correção do status cancelada indevido.
* ``PR 1093``: Correção no tratamento de **datas** na emissão de NFSe.
* ``PR 1094``: Padronização dos filtros de **data** em Contas a Receber e Contas a Pagar; novos filtros em Contas a Pagar; busca por observação, valor e documento.
* ``PR 1097``: **Calendário** de vencimentos em Contas a Receber.
**Gsoft API**
* ``PR 1084``: Registro da **versão da Gsoft API** na inicialização, para acompanhamento de atualizações.

### 1.0.17 / 16.1 (03/08/2026)
**Wincash Web**
* ``PR 1066``: Melhorias visuais e de filtros em **Contas a Receber** — período por intervalo de datas, filtros situacionais e seleção de cliente.
* ``PR 1067``: **Segmentação e privilégios** de usuário — controle de acesso por módulo e configurações.
* ``PR 1069``: Cadastro de **Plano de Contas**, com hierarquia em cascata.
* ``PR 1070``: Reestruturação do **menu principal** — acesso por módulos (Financeiro, Produtos, Clientes, Vendas, Fiscal e Dashboard) e favoritos.
* ``PR 1075``: Novo módulo **Dashboard** com indicadores e analytics.

### 1.0.8 / 11.1 (31/07/2026)
**Wincash Web**
* ``PR 1054``: Melhoria na **pesquisa do menu** do Wincash Web.
* ``PR 1057``: Relatório de **Saídas por Conta**, com resumo e detalhamento.
* ``PR 1062``: Melhorias no módulo de **NFSe** — seleção de itens de serviço, ações de SEFIN/configuração, registro de chave e exclusão de registros locais.
**Gsoft API**
* ``PR 1059`` / ``PR 1063``: Upload e correção de **fotos do cardápio digital** na API.

### 1.0.7 / 10.1 (28/07/2026)
**Wincash Web**
* ``PR 1038``: Módulo de **NFSe** (padrão nacional) em Vendas — listagem, detalhe, emissão, cancelamento e DANFSe/PDF.
* ``PR 1041``: Correção na sincronização de **tabelas de preço** no cadastro de produtos (custo e margem).
* ``PR 1042``: Relatório **Curva ABC de Compras**, com gráficos e exportação para Excel/PDF.
* ``PR 1044``: Melhoria na sincronização de **tabelas de preço** — inclusão de margem e margem de lucro.
* ``PR 1045``: Melhorias no **cadastro de produtos** — natureza do produto, classificação mercadológica e ajustes de layout e campos.
* ``PR 1048``: Relatório de **Prazo Médio de Compras**, com gráficos e exportação para Excel/PDF.
**Gsoft API**
* ``PR 1031``: Cancelamento e consulta de **NFSe** no Portal Nacional.
* ``PR 1039``: Acesso remoto via **túnel Gsoft** para integração com o Wincash Web.

### 1.0.6 (25/07/2026)
**Wincash Web**
* ``PR 1028``: Listagem de produtos com **cor do produto** na linha; ordenação das tabelas de preço por descrição.
* ``PR 1029``: **Contas a pagar recorrentes** — cadastro e gestão de recorrências na tela de Contas a Pagar.
* ``PR 1033``: Ajustes visuais e de navegação — atalhos, campos de data, cadastro de clientes (**Grupos**/regiões); remoção de itens de menu não utilizados.

### 1.0.4 / 9.1 (20/07/2026)
**Wincash Web**
* ``PR 577``: Opções **salvar e descartar** em formulários do Wincash Web.
* ``PR 646``: Indicador de **carregamento** nas telas do Wincash Web.
* ``PR 647``: Atualização da interface do **Wincash Web**.
* ``PR 713``: Melhorias no cabeçalho e botões do **cadastro de produtos**.
* ``PR 742``: **Transferência de produtos** entre lojas.
* ``PR 760``: Histórico de **estoque**.
* ``PR 765``: Melhorias na interface do **Wincash Web**.
* ``PR 651``: Correção do título e do logo na aba do navegador.
* ``PR 664``: **Cadastro de produtos** no Wincash Web.
* ``PR 672``: Sessão expirada redireciona corretamente para o **login**.
* ``PR 679``: Submenus no menu **Compras**.
* ``PR 681``: Correções visuais e de usabilidade no **cadastro de produtos**.
* ``PR 689``: Filtro de produtos por **fornecedor** no pedido de compras.
* ``PR 692``: **Cadastro de produtos**.
* ``PR 694`` / ``PR 695`` / ``PR 696`` / ``PR 697``: Menu reorganizado e mais intuitivo.
* ``PR 699``: Melhorias no **menu principal**.
* ``PR 706``: Ordem de serviços realocada para a aba **Vendas**.
* ``PR 707``: Melhorias no **menu principal**.
* ``PR 710``: Correção na abertura do Wincash Web.
* ``PR 711``: Menu reorganizado e mais intuitivo.
* ``PR 724``: Tela de **Contas a Pagar** com filtros.
* ``PR 725``: Novo layout de **contas a receber**.
* ``PR 726``: Botão **nova conta a receber**.
* ``PR 728``: Novo layout de **pedidos de compra**.
* ``PR 729``: Pedidos de compra — layout interno, calendário nas datas, busca aprimorada e fases do pedido.
* ``PR 734``: Mini tabela de estoque no cadastro de produtos — destaque por **quantidade**.
* ``PR 738``: Correções de interface no **pedido de compras** (layout e campos).
* ``PR 740``: Títulos e filtros de colunas mais claros nas listagens.
* ``PR 747``: Mini tabela de estoque no cadastro de produtos — destaque por **quantidade** (em vez de locais).
* ``PR 764``: Fluxo de **orçamentos** no Wincash Web.
* ``PR 778``: Renovação automática da sessão e melhor carregamento de empresas após o login.
* ``PR 781``: Validação de sessão e melhorias no login.
* ``PR 792``: Menos ruído visual no histórico de movimentação.
* ``PR 793``: Melhor contraste dos atalhos no **cabeçalho** das páginas.
* ``PR 794``: Melhoria na verificação de **autorização** de acesso.
* ``PR 795``: Reorganização da ordem dos itens do **menu** (incluindo Fluxo de Orçamentos em Vendas e Relatórios).
* ``PR 824``: Módulo de **nota de entrada** no Wincash Web.
* ``PR 848``: Melhorias em **contas a receber**.
* ``PR 850``: Tela de **movimentação bancária**.
* ``PR 852``: Unidade de importação e sugestões de formação de preços na **nota fiscal de entrada**.
* ``PR 856``: Campo **data de entrada** na nota fiscal de entrada.
* ``PR 857``: Layout mais consistente nas listagens de Contas a Pagar, Contas a Receber e correlatas.
* ``PR 867``: Tela de **cadastro de clientes** no Wincash Web.
* ``PR 921``: Botão **consultar vendas** na aba Vendas.
* ``PR 944``: Melhorias de **filtro e pesquisa** em Contas a Pagar.
* ``PR 945``: Melhorias na **baixa de títulos** em Contas a Pagar.
* ``PR 949``: Aba de **calendário** em Contas a Pagar — títulos por data e totais.
* ``PR 951``: Simplificação da configuração de privilégios em **Contas a Pagar**.
* ``PR 953``: Seleção de múltiplas linhas e filtros de situação em **Contas a Receber**.
* ``PR 955``: Novos filtros na página de **Contas a Receber**.
* ``PR 956``: Baixa de títulos em Contas a Receber com juros e descontos; seleção de múltiplos títulos.
* ``PR 957``: Novos filtros na listagem de **baixas** em Contas a Receber.
* ``PR 976``: Status de sincronização do **manifesto** e funções relacionadas.
* ``PR 985``: Suporte a **multi-emitente** no Wincash Web.
* ``PR 999``: Campos do cadastro de clientes em **caixa alta**; correção no campo de CNPJ.
* ``PR 1000``: Melhorias no **cadastro de produtos** — formação de preço, ajuste de estoque, código de barras e histórico de estoque.
* ``PR 1002``: Cadastro de produtos no fluxo de **nota fiscal de entrada**, com validação de código de barras e categorias.
* ``PR 1005``: Melhorias na listagem de **notas do manifesto** (busca e filtro por data).
* ``PR 1007``: Melhorias no processamento de **notas fiscais e manifesto** — associação de produtos, validação de eventos e atualização de cache.
* ``PR 1009``: Persistência do rascunho de **formação de preços** na nota fiscal de entrada.
* ``PR 1010``: Ampliação do **cadastro de produtos** — opções de tipo, tabelas de preço, estoque mínimo/máximo, exibição no PDV e formação de preços.
* ``PR 1011``: Formação de preços com **iFood** na nota fiscal de entrada.
* ``PR 1018``: Melhorias visuais na tela de **nota fiscal de entrada** e manifesto (layout e responsividade).
* ``PR 1019``: Tela **Sobre** com versão do aplicativo e status da API.
* ``PR 1020``: Ajustes visuais na **listagem de produtos** (busca e layout).
* ``PR 1021``: Melhorias nas **listagens** de clientes e produtos — filtros de status, busca e layout dos filtros.
**Gsoft API**
* ``PR 915``: Integração com **WhatsApp** na Gsoft API.
* ``PR 995``: Suporte a **fotos de produtos** na API.

### Gsoft API 8.1 (24/06/2026)
**Gsoft API**
* ``PR 838``: Correção na emissão de **NF-e** — evita reprocessar nota já existente.
* ``PR 839``: Exibição mais clara das **mensagens de erro**.
* ``PR 840``: Estrutura inicial de emissão de **NFS-e** na API.
* ``PR 843``: Maior estabilidade na emissão de **NFC-e** (conexão com a SEFAZ e novas tentativas em falha).
* ``PR 853``: Melhorias na integração com **WhatsApp**.
* ``PR 862``: Estrutura inicial de emissão de **NFS-e** na API.
* ``PR 879``: Melhoria na emissão de **NF-e** — limpeza de reservas temporárias e melhor tratamento de erros e respostas da SEFAZ.
* ``PR 911``: Correção no salvamento de **XML de NFSe**.
* ``PR 913``: Salvamento de **XML de DF-e** na Gsoft API.

### Gsoft API 6.7 (03/06/2026)
**Wincash Web**
* ``PR 515``: Busca de **CEP** (ViaCEP).
* ``PR 552`` / ``PR 553``: Busca e menu horizontal do **usuário** (favoritos).
* ``PR 554``: Atalhos de usuário no **painel** (favoritos e atalhos personalizados).
* ``PR 582``: Indicador de **carregamento** nas telas do Wincash Web.
* ``PR 583``: Cadastro de **usuários, funcionários, entregadores e contador**.
**Gsoft API**
* ``PR 493``: Melhoria na validação de **certificado digital** na API.
* ``PR 782``: Validação de sessão na API.
* ``PR 783``: Validação de sessão e seleção de **ambiente** (produção/homologação) na emissão de NF-e.
* ``PR 799``: Seleção de **ambiente** (produção/homologação) na emissão de NF-e.
* ``PR 823``: Integração da API com o Wincash Web.
* ``PR 828``: Melhoria na conexão em tempo real com o Wincash Web — maior estabilidade e reconexão automática.

### Gsoft API 6.5 (22/05/2026)
**Gsoft API**
* ``PR 542``: Conexão em tempo real entre Wincash Web e Gsoft API.
* ``PR 584``: Cadastro de **usuários, funcionários, entregadores e contador** na API.
* ``PR 585``: Reconexão automática quando a empresa perde o vínculo na conexão.
* ``PR 595``: Melhorias de estabilidade na conexão em tempo real com o Wincash Web.
* ``PR 775``: Correção do redirecionamento para as páginas web.
* ``PR 776``: Preparação do fluxo de **cancelamento de NFC-e**.
* ``PR 779``: CNPJ da empresa incluído na sessão de autenticação.
