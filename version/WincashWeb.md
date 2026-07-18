# Wincash Web

Esta página reúne as alterações do **Wincash Web** e da **Gsoft API** (serviço local de integração).
A atualização é automática — não há download manual.

### 16/07/2026
**Wincash Web**
* ``PR 1007``: Melhorias no processamento de **notas fiscais e manifesto** — associação de produtos, validação de eventos e atualização de cache.
* ``PR 1009``: Persistência do rascunho de **formação de preços** na nota fiscal de entrada.
* ``PR 1011``: Formação de preços com **iFood** na nota fiscal de entrada.

### 15/07/2026
**Wincash Web**
* ``PR 1000``: Melhorias no **cadastro de produtos** — formação de preço, ajuste de estoque, código de barras e histórico de estoque.
* ``PR 999``: Normalização de campos do cadastro de clientes para **caixa alta**; correção no input de CNPJ.
* ``PR 1002``: Cadastro de produtos no fluxo de **nota fiscal de entrada**, com validação de código de barras e categorias.
* ``PR 1005``: Melhorias na listagem de **notas do manifesto** (performance, busca e filtro por data).

### 10/07/2026
**Gsoft API**
* ``PR 995``: Nova rota de **fotos de produtos** na API.

### 08/07/2026
**Wincash Web**
* ``PR 985``: Suporte a **multi-emitente** no Wincash Web.
* ``PR 976``: Adicionar endpoint de status de sincronização do manifesto e funcionalidades relacionadas

### 02/07/2026
**Wincash Web**
* ``PR 957``: Implementa novos filtros e lógica para a listagem de baixas em Contas a Receber
* ``PR 956``: Atualiza a lógica de baixa de títulos em Contas a Receber, implementando ajustes de juros e descontos. Refatora componentes para permitir a seleção de múltip...
* ``PR 955``: Implementa novos filtros e componentes para a página de Contas a Receber

### 30/06/2026
**Wincash Web**
* ``PR 953``: Implementa seleção de múltiplas linhas na tabela de Contas a Receber e refatora filtros de situação. Adiciona lógica para seleção de linhas com checkbox, per...
* ``PR 951``: Remover o gerenciamento de privilégios das entidades e serviços do ContasPagar, simplificando a configuração e a lógica da interface do usuário. Atualizar os...
* ``PR 949``: Implementa a aba de calendário na página de contas a pagar, permitindo visualização e gerenciamento de títulos por data. Adiciona componentes para exibir tot...
* ``PR 946``: Documentação de estoque no Wincash Web.
* ``PR 945``: Refatora componentes de ContasPagar para aprimorar a funcionalidade de baixa de títulos
* ``PR 944``: Reestrutura os componentes do ContasPagar para aprimorar as funcionalidades de filtragem e pesquisa
* ``PR 925``: Plano de **fechamento de caixa** no Wincash Web.
* ``PR 921``: Botão **consultar vendas** na aba Vendas.

**Gsoft API**
* ``PR 915``: Integração com **WhatsApp** na Gsoft API.

### 24/06/2026
**Wincash Web**
* ``PR 867``: Tela de **cadastro de clientes** no Wincash Web.

**Gsoft API**
* ``PR 913``: Salvamento de **XML de DF-e** na Gsoft API.
* ``PR 911``: Correção no salvamento de **XML de NFSe**.
* ``PR 909``: Melhorias em **Correcao serie nfse mockado**.
* ``PR 891``: Implementa a conexão por request e o uso do pool de conexões
* ``PR 887``: Melhorias em **Correcao log**.

### 19/06/2026
**Gsoft API**
* ``PR 879``: Add LimparTempReserva method and enhance Emitir logic for NFe processing
* ``PR 870``: Remoção de classe quadruplicada
* ``PR 862``: Implementa a estrutura inicial para emissão de NFS-e, incluindo contratos, serviços e repositórios. Adiciona rotas e handlers para a API, além de documentaçã...
* ``PR 840``: Implementa a estrutura inicial para emissão de NFS-e, incluindo contratos, serviços e repositórios. Adiciona rotas e handlers para a API, além de documentaçã...

### 12/06/2026
**Wincash Web**
* ``PR 857``: Refatora componentes de layout para utilizar ListPageShell em vez de Card, melhorando a consistência visual e a usabilidade nas páginas de Contas a Pagar, Co...
* ``PR 856``: Adiciona o campo 'DataEntrada' à estrutura de Nota Fiscal de Entrada e atualiza a lógica de manipulação e exibição. A consulta SQL foi ajustada para incluir...
* ``PR 852``: Implementa novas funcionalidades na gestão de notas fiscais de entrada, incluindo a adição de campos para unidade de importação e sugestões de formação. Atua...

### 11/06/2026
**Wincash Web**
* ``PR 850``: Tela de **movimentação bancária**.
* ``PR 848``: Melhorias em **contas a receber**.

**Gsoft API**
* ``PR 853``: Melhorias em **Whatsapp api**.

### 10/06/2026
**Wincash Web**
* ``PR 824``: Módulo de **nota de entrada** no Wincash Web.

**Gsoft API**
* ``PR 845``: Melhorias em **Organizacao pasta dlls**.
* ``PR 843``: Implementa warmup para SEFAZ NFC-e no startup e refatora lógica de emissão com tentativas de conexão. Adiciona tratamento de erros específicos para falhas de...
* ``PR 839``: Implementa a exibição da mensagem de erro
* ``PR 838``: Refactor NFe service to enhance idempotency check for existing notes. Updated logging and validation to ensure CodVenda is greater than 0 before checking for...
* ``PR 836``: Corrige o send do error handler que sempre enviava mensagens genéricas
* ``PR 835``: Altera o log de vários memos para um único memo com rolagem

### 02/06/2026
**Gsoft API**
* ``PR 828``: Update WebSocket client for improved liveness and reconnection handling
* ``PR 823``: Foi adicionado o Runner e o WsHandler para deixar a rota valida e funcionando para o cliente.

### 29/05/2026
**Wincash Web**
* ``PR 820``: Remoção de import não utilizado

**Gsoft API**
* ``PR 821``: Corrige performance do log
* ``PR 799``: Adiciona propriedade Tipo_Ambiente na classe EmitirNFe e atualiza lógica de validação e recuperação de dados. A propriedade permite especificar o ambiente (p...

### 15/05/2026
**Wincash Web**
* ``PR 795``: Refactor: reorder menu items in menuData.ts
* ``PR 794``: Refactor: aprimorar a função de verificação de autorização para suportar valores booleanos e strings
* ``PR 793``: PageHeader Shortcut contrastado com foreground, em vez de borda
* ``PR 792``: Redução da quantidade de informação no histórico de movimentação
* ``PR 781``: Implementa validação de token e melhorias no gerenciamento de autenticação
* ``PR 778``: Implementa lógica de refresh token e aprimora o carregamento de empresas no contexto de autenticação. Adiciona suporte para redirecionamento após login com t...

**Gsoft API**
* ``PR 783``: Adiciona propriedade Tipo_Ambiente na classe EmitirNFe e atualiza lógica de validação e recuperação de dados. A propriedade permite especificar o ambiente (p...
* ``PR 782``: Implementa novo endpoint POST /ValidaToken para validação de tokens JWT. Adiciona método ExecuteValidaToken na interface ILoginUsuarioRunner e na classe TLog...
* ``PR 779``: Implementa o salvamento do cnpj da empresa no claim do jwt
* ``PR 776``: Plano de cancelamento da nfce
* ``PR 775``: Corrige a lógica do redirecionamento para as páginas web

### 05/05/2026
**Wincash Web**
* ``PR 765``: Remove o webview da pasta
* ``PR 764``: Remove o webview da pasta
* ``PR 760``: Histórico de estoque v1

### 28/04/2026
**Wincash Web**
* ``PR 747``: Estava locais no highlight do cadastro de produtos, sendo que era pra ser quantidade para entender melhor a intenção da mini tabela de estoque

**Gsoft API**
* ``PR 751``: Modifica a localização dos arquivos que comunicam com o GsoftAPI de src para API

### 27/04/2026
**Wincash Web**
* ``PR 742``: Transferência de produtos + componentizações para escalabilidade
* ``PR 740``: Placeholder title intuitivo e ícone do VisibilityColumn filter trocado de ListFilter para Columns3
* ``PR 738``: Pedido de compras UI fix
* ``PR 734``: Estava locais no highlight do cadastro de produtos, sendo que era pra ser quantidade para entender melhor a intenção da mini tabela de estoque
* ``PR 729``: Pedidos de compra novo layout interno do pedido + DataInput com Popover com Calendar + Lookup Search Input (com variantes) + Fases no pedido de compra
* ``PR 728``: Pedidos de Compra Layout
* ``PR 726``: Botão Nova conta a receber
* ``PR 725``: Contas a receber layout novo
* ``PR 724``: Contas a Pagar, por enquanto tem apenas filtros
* ``PR 713``: Remove espaços em branco e classname desnecessário
* ``PR 712``: Correção de compontização
* ``PR 711``: Menu reorganizado e mais intuitivo, descentralizando o cadastro
* ``PR 710``: - Correção abertura do Wincash web
* ``PR 709``: DataTable Skeleton Props
* ``PR 708``: Layout colado no header componentizado
* ``PR 707``: Melhorias em **Megamenuuipathcard**.
* ``PR 706``: Ordem de servicos realocada para aba Vendas
* ``PR 705``: Micro-animacao e search componentizado
* ``PR 702``: Flecha no Mega Menu e alguns minor fixes
* ``PR 699``: Melhorias em **Megamenu**.
* ``PR 697``: Menu reorganizado e mais intuitivo, descentralizando o cadastro
* ``PR 696``: Menu reorganizado e mais intuitivo, descentralizando o cadastro
* ``PR 695``: Menu reorganizado e mais intuitivo, descentralizando o cadastro
* ``PR 694``: Menu reorganizado e mais intuitivo, descentralizando o cadastro
* ``PR 692``: Cadastro produtos

**Gsoft API**
* ``PR 719``: Refatora endpoint vincular-terminal colocando todo parseamento de json dentro do runner

### 14/04/2026
**Wincash Web**
* ``PR 689``: Filtro de produtos por **fornecedor** no pedido de compras.

**Gsoft API**
* ``PR 688``: Movendo cadastro/produtos para cadastros/produtos
* ``PR 685``: Corrige raise inválido não permitido pelo delphi

### 10/04/2026
**Wincash Web**
* ``PR 683``: Implementa a exclusão no backend
* ``PR 681``: Correções visuais no cadastro de produtos e experiência do usuário
* ``PR 679``: Implementa submenus no menu Compras
* ``PR 664``: Implementar Runner e Service de Cadastro de Produtos

**Gsoft API**
* ``PR 682``: Implementa a migration no GsoftApi

### 08/04/2026
**Wincash Web**
* ``PR 672``: Implementa correção do contexto de autorização fazendo com que ele passe a olhar para a validade do jwt e redirecionar para o login se expirada.

### 02/04/2026
**Wincash Web**
* ``PR 651``: Corrige o título e o logo na aba do navegador
* ``PR 650``: Nova skill para serializar json
* ``PR 649``: Remoção do .env do repositório
* ``PR 648``: Atualiza as dependências com vunerabilidade
* ``PR 647``: Remove o antigo frontend

### 30/03/2026
**Wincash Web**
* ``PR 646``: Indicador de **carregamento (loader)** nas telas do Wincash Web.

### 09/03/2026
**Gsoft API**
* ``PR 595``: Melhorias de estabilidade no **WebSocket** (heartbeat, reconexão e watchdog).
* ``PR 585``: Implementa verificação periódica de conexões no GsoftAPI.WsClient para reconexão automática se id_empresa não estiver na lista. Adiciona método para checar c...

### 05/03/2026
**Wincash Web**
* ``PR 583``: Implementação do cadastro de usuários, funcionários, entregadores e contador no padrão definitivo.
* ``PR 582``: Indicador de **carregamento (loader)** nas telas do Wincash Web.

**Gsoft API**
* ``PR 584``: Implementação do cadastro de usuários, funcionários, entregadores e contador no padrão definitivo.

### 27/02/2026
**Wincash Web**
* ``PR 577``: Opções **salvar e descartar** em formulários do Wincash Web.
* ``PR 572``: Alteração no sistema.

**Gsoft API**
* ``PR 543``: Implementa o salvamento dos logs no banco de dados SQLite

### 25/02/2026
**Wincash Web**
* ``PR 556``: Alteração no sistema.
* ``PR 554``: Add UsuarioShortcuts feature integration
* ``PR 553``: Search and User HorizontalMenu
* ``PR 552``: Search and User HorizontalMenu

**Gsoft API**
* ``PR 542``: Implementa a api websocket + documentação

### 15/02/2026
**Gsoft API**
* ``PR 534``: Remoção do projeto legado da Gsoft API.

### 10/02/2026
**Wincash Web**
* ``PR 515``: - Busca de CEP via API viaCEP

### 29/01/2026
**Gsoft API**
* ``PR 493``: Improve SSL certificate and library validation in GsoftApiGUI.dpr
