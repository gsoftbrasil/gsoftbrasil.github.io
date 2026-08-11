# Wincash Web

Esta página reúne as alterações do **Wincash Web** e da **Gsoft API** (serviço local de integração).
A atualização é automática — não há download manual.

### 11/08/2026
**Wincash Web**
* ``PR 1128``: Melhorias no módulo **Patrimônio** — cadastro de departamentos, código sequencial único e ajustes em transferências e movimentações.
* ``PR 1129``: Melhorias em **Contas a Pagar** — consulta de contas/fornecedor, confirmações por diálogo e data de pagamento somente leitura.
* ``PR 1130``: Correção do **saldo anterior** na movimentação bancária.
* ``PR 1160``: Correção na **data de pagamento** em Contas a Pagar (grava somente a data, sem hora).
* ``PR 1161``: Tipos de documento em **Contas a Pagar** alinhados ao desktop (DNH, BOL, CRT, DBT, NOT e OUT).
* ``PR 1162``: Filtros de data com **mês corrente** por padrão e memória do período escolhido (Contas a Receber/Pagar, movimentação bancária e pedido de compras).
* ``PR 1163``: Padronização do **Pedido de Compras** — alinhado ao desktop (tempo de entrega, sugestão, peso e consulta de produtos).

### 07/08/2026
**Wincash Web**
* ``PR 1121``: Novo módulo **Patrimônio** — cadastro de bens com foto, movimentações e histórico (comodato, empréstimo, transferência, manutenção, ajuste e baixa).

### 06/08/2026
**Wincash Web**
* ``PR 1096``: Melhorias no **lançamento de Contas a Pagar** — formulário com tipo/número da NF, usuário, data e centro de custo; descrição alinhada ao plano de contas; coluna Plano de contas com tooltip.
* ``PR 1103``: Correção na **barra de seleção** das listagens.
* ``PR 1106``: Acesso local ao **Wincash Web** via **túnel Gsoft** — a interface passa a ser servida pelo próprio túnel.
* ``PR 1107``: Padronização de **datas**; correções de saldo bancário, competência e centro de custos em Contas a Pagar.

**Gsoft API**
* ``PR 1104``: Correção de **referência repetida** na API.

### 05/08/2026
**Wincash Web**
* ``PR 1080``: Ampliação dos filtros avançados em **Contas a Receber** (região, categoria, forma de pagamento, cedente e período de recebimento); melhorias na listagem de clientes.
* ``PR 1090``: Módulo de **Cobrança** — consulta e geração de boletos, remessa e retorno CNAB, envio por e-mail e WhatsApp.
* ``PR 1091``: Melhorias no módulo **NFSe** — filtro por período, alíquota de ISS do emitente, correção do status cancelada indevido; remoção da exclusão local de registros.
* ``PR 1093``: Correção no tratamento de **datas** na emissão de NFSe.
* ``PR 1094``: Padronização dos filtros de **data** em Contas a Receber e Contas a Pagar; novos filtros em Contas a Pagar; busca por observação, valor e documento.
* ``PR 1097``: **Calendário** de vencimentos em Contas a Receber.

**Gsoft API**
* ``PR 1084``: Registro da **versão da Gsoft API** na inicialização, para acompanhamento de atualizações.

### 03/08/2026
**Wincash Web**
* ``PR 1066``: Melhorias visuais e de filtros em **Contas a Receber** — período por intervalo de datas, filtros situacionais e seleção de cliente.
* ``PR 1067``: **Segmentação e privilégios** de usuário — controle de acesso por módulo e configurações.
* ``PR 1069``: Cadastro de **Plano de Contas**, com hierarquia em cascata.
* ``PR 1070``: Reestruturação do **menu principal** — acesso por módulos (Financeiro, Produtos, Clientes, Vendas, Fiscal e Dashboard) e favoritos.
* ``PR 1075``: Novo módulo **Dashboard** com indicadores e analytics.

### 31/07/2026
**Wincash Web**
* ``PR 1057``: Relatório de **Saídas por Conta**, com resumo e detalhamento.
* ``PR 1062``: Melhorias no módulo de **NFSe** — seleção de itens de serviço, ações de SEFIN/configuração, registro de chave e exclusão de registros locais.

**Gsoft API**
* ``PR 1059`` / ``PR 1063``: Upload e correção de **fotos do cardápio digital** na API.

### 29/07/2026
**Wincash Web**
* ``PR 1054``: Melhoria na **pesquisa do menu** do Wincash Web.

### 28/07/2026
**Wincash Web**
* ``PR 1042``: Relatório **Curva ABC de Compras**, com gráficos e exportação para Excel/PDF.
* ``PR 1048``: Relatório de **Prazo Médio de Compras**, com gráficos e exportação para Excel/PDF.
* ``PR 1044``: Melhoria na sincronização de **tabelas de preço** — inclusão de margem e margem de lucro.
* ``PR 1045``: Melhorias no **cadastro de produtos** — natureza do produto, classificação mercadológica e ajustes de layout e campos.

### 27/07/2026
**Wincash Web**
* ``PR 1038``: Módulo de **NFSe** (padrão nacional) em Vendas — listagem, detalhe, emissão, cancelamento e DANFSe/PDF.
* ``PR 1041``: Correção na sincronização de **tabelas de preço** no cadastro de produtos (custo e margem).

**Gsoft API**
* ``PR 1039``: Acesso remoto via **túnel Gsoft**, substituindo o cliente WebSocket embutido.

### 25/07/2026
**Wincash Web**
* ``PR 1028``: Listagem de produtos com **cor do produto** na linha; ordenação das tabelas de preço por descrição.
* ``PR 1033``: Ajustes visuais e de navegação — atalhos, campos de data, cadastro de clientes (**Grupos**/regiões); remoção de itens de menu não utilizados.

### 24/07/2026
**Wincash Web**
* ``PR 1029``: **Contas a pagar recorrentes** — cadastro e gestão de recorrências na tela de Contas a Pagar.

**Gsoft API**
* ``PR 1031``: Cancelamento e consulta de **NFSe** no Portal Nacional.

### 20/07/2026
**Wincash Web**
* ``PR 1010``: Ampliação do **cadastro de produtos** — opções de tipo, tabelas de preço, estoque mínimo/máximo, exibição no PDV e formação de preços.
* ``PR 1018``: Melhorias visuais na tela de **nota fiscal de entrada** e manifesto (layout e responsividade).
* ``PR 1019``: Tela **Sobre** com versão do aplicativo e status da API.
* ``PR 1020``: Ajustes visuais na **listagem de produtos** (busca e layout).
* ``PR 1021``: Melhorias nas **listagens** de clientes e produtos — filtros de status, busca e layout dos filtros.

### 16/07/2026
**Wincash Web**
* ``PR 1007``: Melhorias no processamento de **notas fiscais e manifesto** — associação de produtos, validação de eventos e atualização de cache.
* ``PR 1009``: Persistência do rascunho de **formação de preços** na nota fiscal de entrada.
* ``PR 1011``: Formação de preços com **iFood** na nota fiscal de entrada.

### 15/07/2026
**Wincash Web**
* ``PR 1000``: Melhorias no **cadastro de produtos** — formação de preço, ajuste de estoque, código de barras e histórico de estoque.
* ``PR 999``: Campos do cadastro de clientes em **caixa alta**; correção no campo de CNPJ.
* ``PR 1002``: Cadastro de produtos no fluxo de **nota fiscal de entrada**, com validação de código de barras e categorias.
* ``PR 1005``: Melhorias na listagem de **notas do manifesto** (busca e filtro por data).

### 10/07/2026
**Gsoft API**
* ``PR 995``: Suporte a **fotos de produtos** na API.

### 08/07/2026
**Wincash Web**
* ``PR 985``: Suporte a **multi-emitente** no Wincash Web.
* ``PR 976``: Status de sincronização do **manifesto** e funções relacionadas.

### 02/07/2026
**Wincash Web**
* ``PR 957``: Novos filtros na listagem de **baixas** em Contas a Receber.
* ``PR 956``: Baixa de títulos em Contas a Receber com juros e descontos; seleção de múltiplos títulos.
* ``PR 955``: Novos filtros na página de **Contas a Receber**.

### 30/06/2026
**Wincash Web**
* ``PR 953``: Seleção de múltiplas linhas e filtros de situação em **Contas a Receber**.
* ``PR 951``: Simplificação da configuração de privilégios em **Contas a Pagar**.
* ``PR 949``: Aba de **calendário** em Contas a Pagar — títulos por data e totais.
* ``PR 945``: Melhorias na **baixa de títulos** em Contas a Pagar.
* ``PR 944``: Melhorias de **filtro e pesquisa** em Contas a Pagar.
* ``PR 921``: Botão **consultar vendas** na aba Vendas.

**Gsoft API**
* ``PR 915``: Integração com **WhatsApp** na Gsoft API.

### 24/06/2026
**Wincash Web**
* ``PR 867``: Tela de **cadastro de clientes** no Wincash Web.

**Gsoft API**
* ``PR 913``: Salvamento de **XML de DF-e** na Gsoft API.
* ``PR 911``: Correção no salvamento de **XML de NFSe**.

### 19/06/2026
**Gsoft API**
* ``PR 879``: Melhoria na emissão de **NF-e** — limpeza de reservas temporárias e melhor tratamento de erros e respostas da SEFAZ.
* ``PR 862`` / ``PR 840``: Estrutura inicial de emissão de **NFS-e** na API.

### 12/06/2026
**Wincash Web**
* ``PR 857``: Layout mais consistente nas listagens de Contas a Pagar, Contas a Receber e correlatas.
* ``PR 856``: Campo **data de entrada** na nota fiscal de entrada.
* ``PR 852``: Unidade de importação e sugestões de formação de preços na **nota fiscal de entrada**.

### 11/06/2026
**Wincash Web**
* ``PR 850``: Tela de **movimentação bancária**.
* ``PR 848``: Melhorias em **contas a receber**.

**Gsoft API**
* ``PR 853``: Melhorias na integração com **WhatsApp**.

### 10/06/2026
**Wincash Web**
* ``PR 824``: Módulo de **nota de entrada** no Wincash Web.

**Gsoft API**
* ``PR 843``: Maior estabilidade na emissão de **NFC-e** (conexão com a SEFAZ e novas tentativas em falha).
* ``PR 839``: Exibição mais clara das **mensagens de erro**.
* ``PR 838``: Correção na emissão de **NF-e** — evita reprocessar nota já existente.

### 02/06/2026
**Gsoft API**
* ``PR 828``: Melhoria na conexão em tempo real (**WebSocket**): estabilidade e reconexão automática.
* ``PR 823``: Rota da API disponível e funcional para o cliente.

### 29/05/2026
**Gsoft API**
* ``PR 799``: Seleção de **ambiente** (produção/homologação) na emissão de NF-e.

### 15/05/2026
**Wincash Web**
* ``PR 795``: Reorganização da ordem dos itens do **menu** (incluindo Fluxo de Orçamentos em Vendas e Relatórios).
* ``PR 794``: Melhoria na verificação de **autorização** de acesso.
* ``PR 793``: Melhor contraste dos atalhos no **cabeçalho** das páginas.
* ``PR 792``: Menos ruído visual no histórico de movimentação.
* ``PR 781``: Validação de sessão e melhorias no login.
* ``PR 778``: Renovação automática da sessão e melhor carregamento de empresas após o login.

**Gsoft API**
* ``PR 783``: Seleção de **ambiente** (produção/homologação) na emissão de NF-e.
* ``PR 782``: Validação de sessão (token) na API.
* ``PR 779``: CNPJ da empresa incluído na sessão de autenticação.
* ``PR 776``: Preparação do fluxo de **cancelamento de NFC-e**.
* ``PR 775``: Correção do redirecionamento para as páginas web.

### 05/05/2026
**Wincash Web**
* ``PR 765``: Remoção do **webview** legado do Wincash Web.
* ``PR 764``: Fluxo de **orçamentos** no Wincash Web.
* ``PR 760``: Histórico de **estoque**.

### 28/04/2026
**Wincash Web**
* ``PR 747``: Mini tabela de estoque no cadastro de produtos — destaque por **quantidade** (em vez de locais).

### 27/04/2026
**Wincash Web**
* ``PR 742``: **Transferência de produtos** entre lojas.
* ``PR 740``: Títulos e filtros de colunas mais claros nas listagens.
* ``PR 738``: Correções de interface no **pedido de compras** (layout e campos).
* ``PR 734``: Mini tabela de estoque no cadastro de produtos — destaque por **quantidade**.
* ``PR 729``: Pedidos de compra — layout interno, calendário nas datas, busca aprimorada e fases do pedido.
* ``PR 728``: Novo layout de **pedidos de compra**.
* ``PR 726``: Botão **nova conta a receber**.
* ``PR 725``: Novo layout de **contas a receber**.
* ``PR 724``: Tela de **Contas a Pagar** com filtros.
* ``PR 713``: Melhorias no cabeçalho e botões do **cadastro de produtos**.
* ``PR 711``: Menu reorganizado e mais intuitivo.
* ``PR 710``: Correção na abertura do Wincash Web.
* ``PR 707`` / ``PR 699``: Melhorias no **menu principal**.
* ``PR 706``: Ordem de serviços realocada para a aba **Vendas**.
* ``PR 697`` / ``PR 696`` / ``PR 695`` / ``PR 694``: Menu reorganizado e mais intuitivo.
* ``PR 692``: **Cadastro de produtos**.

### 14/04/2026
**Wincash Web**
* ``PR 689``: Filtro de produtos por **fornecedor** no pedido de compras.

### 10/04/2026
**Wincash Web**
* ``PR 683``: Exclusão de registros no cadastro (backend).
* ``PR 681``: Correções visuais e de usabilidade no **cadastro de produtos**.
* ``PR 679``: Submenus no menu **Compras**.
* ``PR 664``: Cadastro de produtos disponível na API e no fluxo web.

### 08/04/2026
**Wincash Web**
* ``PR 672``: Sessão expirada redireciona corretamente para o **login**.

### 02/04/2026
**Wincash Web**
* ``PR 651``: Correção do título e do logo na aba do navegador.
* ``PR 647``: Remoção do frontend legado e organização do **Wincash Web**.

### 30/03/2026
**Wincash Web**
* ``PR 646``: Indicador de **carregamento** nas telas do Wincash Web.

### 09/03/2026
**Gsoft API**
* ``PR 595``: Melhorias de estabilidade no **WebSocket** (heartbeat, reconexão e watchdog).
* ``PR 585``: Reconexão automática quando a empresa perde o vínculo na conexão.

### 05/03/2026
**Wincash Web**
* ``PR 583``: Cadastro de **usuários, funcionários, entregadores e contador**.
* ``PR 582``: Indicador de **carregamento** nas telas do Wincash Web.

**Gsoft API**
* ``PR 584``: Cadastro de **usuários, funcionários, entregadores e contador** na API.

### 27/02/2026
**Wincash Web**
* ``PR 577``: Opções **salvar e descartar** em formulários do Wincash Web.

**Gsoft API**
* ``PR 543``: Salvamento dos logs em banco local.

### 25/02/2026
**Wincash Web**
* ``PR 554``: Atalhos de usuário no **painel** (favoritos e atalhos personalizados).
* ``PR 553`` / ``PR 552``: Busca e menu horizontal do **usuário** (favoritos).

**Gsoft API**
* ``PR 542``: API em tempo real (**WebSocket**) e documentação.

### 15/02/2026
**Gsoft API**
* ``PR 534``: Remoção do projeto legado da Gsoft API.

### 10/02/2026
**Wincash Web**
* ``PR 515``: Busca de **CEP** (ViaCEP).

### 29/01/2026
**Gsoft API**
* ``PR 493``: Melhoria na validação de **certificado SSL** e bibliotecas da Gsoft API.
