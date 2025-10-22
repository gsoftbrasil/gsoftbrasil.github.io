# Wincash 3002
[Download](https://servidor.gsoft.com.br/wincash/3002/WinCash.exe)

### 3002.9 (21/10/2025)
* ``Ticket 9386``: Removida a mensagem “Alíquota de ICMS inválida!” que impedia o cadastro de produtos com alíquota de 12%, mesmo quando já existia uma alíquota de 18% configurada para a UF da empresa.

### 3002.8 (17/10/2025)
* ``Ticket 9382``: Removida a conversão de texto UTF8 para ANSI no método de resposta, evitando erros de tipo (“invalid typecast”). Ajustado validação de licença na API para maior estabilidade.
* ``PR 312``: Melhoria e correções gerais na integração com a plataforma NAU.

### 3002.7 (16/10/2025)
* ``Ticket 9381``: DRE - Otimização: removida uma junção desnecessária na consulta de vendas, melhorando o desempenho. Adicionado indicador de atividade e otimizada a impressão de vendas, tornando o processo mais claro e rápido.

* ``Ticket 9380``: Tela de inicialização (splash) agora esconde corretamente durante o carregamento.

* ``Ticket 9378``: Agora no relatório de contas a receber é possível filtrar por notas com e sem NFe.
  <img width="1033" height="748" alt="image" src="https://github.com/user-attachments/assets/333d7669-c837-4749-a62b-1b0cf432d46c" />

* ``Ticket 9377``: Campo de desconto e acréscimo da forma de pagamento funciona corretamente no fechamento da venda.

* ``PR 304``: NFCeTop verifica a cada 2 minutos se existe uma instância do NFCeTo rodando, caso não encontre o sistema é encerrado automaticamente. Além disso, foi implementado a tela de senha do dia ao clicar na aba Configuração.
* ``Ticket 9373``: Atualizado o campo da formação de preço de 'ICMS sobre Vendas %' para 'DAS %'. Padronização de acordo com o cadastro dos produtos.

### 3002.6 (13/10/2025)
* ``PR 296``: Implementação de funcionalidades do lucro real - multitributação no produto, regras cst 10 e 70, entrada de notas com vinculo correto às regras tributárias, cadastro fiscal mais seguro, correções de estabilidade em geral.  

### 3002.5 (10/10/2025)
* Agora é possível realizar o filtro do relatório de contas a pagar por NFe ou NF(nota não fiscal).
<img height="250" alt="image" src="https://github.com/user-attachments/assets/d822ae2d-b02f-49d3-831d-56b71da4d011" />

### 3002.4 (09/10/2025)
* ``Ticket 9373``: Multi Loja - A lógica de filtragem por loja na tela de vendas foi simplificada, tornando o carregamento das informações mais rápido e estável.
* ``Ticket 9305``: Ao vincular um produto novo a um produto já existente no cadastro durante o lançamento da nota fiscal de entrada, a barra de busca é preenchida automaticamento com codigo de barras da nota fiscal.

### 3002.3 (07/10/2025)
* ``PR 282``: Ajuste de classe ACBr.
* ``PR 283``: Ajustada a forma como o sistema busca as informações dos títulos da nota fiscal, deixando o processo mais rápido e estável e atualização ACBr.

___

# Wincash 3001

### 3001.12 (07/10/2025)
* ``PR 271``: Filtro de títulos recebidos considera flag para filtrar os inativos. O padrão traz apenas os ativos.
  
* ``Ticket 9357``: Movimentação bancária agora registra o detalhe da forma de pagamento baixada ou da venda realizada.
 <img width="1030" height="377" alt="image" src="https://github.com/user-attachments/assets/a2dd5d1e-3176-48dc-a5e6-23c07f03a0c5" />


* ``Ticket 9363``: Adicionado campo previsão na OS.
 <img width="750" height="343" alt="image" src="https://github.com/user-attachments/assets/decb2d17-82ed-4fa0-b783-cde41987e1ba" />


* ``PR 275``: Relatório de NFe agora permite a busca de numerações inutilizadas.
 <img width="1033" height="418" alt="image" src="https://github.com/user-attachments/assets/d3c15e02-3c12-499c-8cc2-1cdca9e6fab7" />


* ``Ticket 9371``: Melhora na inserção de títulos na NFe, evitando duplicatas ao adicionar registros já existentes.
* ``Ticket 9370``: Relatório de contas a receber geral agora exibe a coluna destino, em que mostra qual banco foi realizada a baixa.
   <img width="1034" height="742" alt="image" src="https://github.com/user-attachments/assets/7a1b8388-4e2f-4f8a-a1c7-52a6f82eaabf" />

### 3001.11 (25/09/2025)
* ``PR 267``: Implementação da lista de transmissão, adição dos contatos dos dependentes do cliente.
* ``PR 269/270`` Correções visuais na central do Whatsapp.

### 3001.10 (19/09/2025) 
* Correção importante nos parâmetros da Nota Promissória
  * **Emite nota promissória na venda a prazo**: Imprime a nota promissória padrão do sistema **sem validade jurídica**.
    * O comportamento do sistema muda caso o usuário selecione o Formato de Impressão **Bobina** ou **Carta**.
  * **Promissória protestável (restante) - bobina**: Imprime os títulos restantes a serem pagos na impressora de bobina.
  * **Promissória protestável (por título) - carta**: Imprime os títulos em formato de impressão A4.
<img width="975" height="360" alt="image" src="https://github.com/user-attachments/assets/87443e80-7b6c-4210-be6c-79b26f6dea63" />

### 3001.9 (19/09/2025)
* Nota Promissória agora imprime novamente direto na bobina.

### 3001.8 (17/09/2025)
* Download automático das dependências necessárias para o Wincash (WebView2Loader.dll e dll-papel-parede.zip).
* Locação: Correção no salvamento de observação.
* Corrigido erro na baixa de títulos por grupo

### 3001.7 (15/09/2025)
* Correção no avanço para a próxima página na impressão de requisição.
* Foi criado um relatório de Cashback disponível em: Relatórios > Clientes > Cashback
* Criado ralatório diário de vendas por produto e classificação mercadológica disponível em: Relatórios > Dem. de Vendas > Análise Diária de Vendas por Produto.

### 3001.6 (12/09/2025)
- Corrigido a busca de produtos por Código de Barras no PDV.

### 3001.5 (10/09/2025)
- Adicionado na locação o campo de Retenção que faz o calculo automático baseado na porcentagem informada.

### 3001.4 (10/09/2025)
- Remoção do parâmetro CodLoja ao buscar clientes.
- Na descrição no produto agora é possível manter caracteres especiais. 
  Para utilizar basta ativar a configuração em: Produtos > Geral > "Manter caractere especial". 

- Ao lançar um inventário o valor do estoque será baseado na tabela mc_produtoslojas de acordo com o terminal em que o usuário estiver logado.
- Descontinuado o padrão antigo de impressão da promissória.
  - Quando “Emitir nota promissória na venda a prazo” estiver ativado → imprime A4, 1 promissória por parcela.
  - Quando “Promissória protestável – bobina” estiver ativado → imprime bobina, 1 promissória única com valor total. 

- Agora é possível visualizar os caixas fechados por loja, quando o modo multi empresa está ativado. 

### 3001.3 (08/09/2025)
- Agora é realizado o lançamento na NFe_Titulos ao faturar uma requisição.

### 3001.2 (06/09/2025)
- Correção consulta de clientes quando Multi Lojas.

### 3001.1 (03/09/2025)
- Removido verificação do executável Notificacao_Wincash.
- Correção das requisições que vinham com ValorBruto = 0 e que ao serem importados no PDV geravam um acréscimo no fechamento da venda.
- Novo relatório de Análise de Rentabilidade. O recurso encontra-se em: Relatórios > Produtos > Análise de Rentabilidade.
- Novo filtro por empresa na nota fiscal de entrada.
- Adicionado campo para visualizar o ticket médio no relatório de venda bruta.
- Agora os itens da Dashboard de Produtos a vencer trará apenas os itens com data de validade válida.
- Corrigido relatório de Venda Bruta por Período, removido multi-lojas.
- Config para possibilitar exportação de relatórios em Excel no formato XLS.  
  Recurso econtra-se nas configurações do sistema na aba: Outros > 'Excel - exportar em formato XLS'.

- Corrigido a concatenação do slogan na impressão de vendas.
- Atualização nas criações de campos (GExcScripts).
- Nova configuração para não manter o desconto ao alterar uma requisição.
  O parâmetro encontra-se nas configurações do sistema em: Balcão Express > Não manter desconto ao alterar a requisição (3ª coluna).

- Papel de parede do balcão express agora é personalizável.
- Filtro do relatório Demonstrativo de Venda na opção por forma de pagamento ajustado.
- Agora é possível realizar a impressão do extrato de vale compras e também a impressão de crédito antecipado.
O recurso se encontra em Clientes > Histórico de Crédito > Vale-Compras.
  
  Modelo EXTRATO DE VALE COMPRAS:

  <img height="300" alt="image" src="https://github.com/user-attachments/assets/58b390cf-bf1a-43bb-a41c-68a6584c1a49" />

  Modelo CRÉDITO ANTECIPADO:
  
  <img height="300" alt="image" src="https://github.com/user-attachments/assets/25585256-7466-428f-8705-9c3bf624011c" />
 
  Para utilizar a impressão de Crédito Antecipado basta ir na aba Vendas > Vale-Compras. Aqui é possível realizar ambas impressões.
  <img height="300" alt="image" src="https://github.com/user-attachments/assets/cd3d9af3-6aec-4f12-9303-5bf8794f70b8" />

- Correção do erro no contas a receber de insert vazio quando clica no campo NumNFe e sai do campo com erro quando não tem nenhum registro de título aberto.

___

# Wincash 3000

### 3000.17 (29/08/2025)
- Ajusta filtro de multi empresas na consulta de contas recorrentes

### 3000.16 (28/08/2025)
- Impressão da requisição voltou a imprimir todas as folhas do documento sem a necessidade de ação do usuário.

### 3000.15 (26/08/2025)
- Exibir a cor dos produtos na nova exportação via Excel.
- Correção na alteração de requisição marcada como perdida.
- Criada configuração "Não consultar lote ao buscar produto".
- Agora o sistema não exibe mais a janela de lote se não houver estoque.
- Correção no erro "Access violation" ao salvar produto pelo atalho F7 quando o mesmo possui tabela de preços.
- Correção do erro ao salvar nota no manifesto pelo botão "Efetuar Entrada - F2" sem manifestar antes.
- Correção na mudança automática do relógio no sistema virtualizado.

### 3000.14 (25/08/2025)
- Alteração do rótulo ICMS para DAS quando a empresa é do Simples Nacional.
- Correção na formatação da impressão de Requisição.
- Criado parâmetro para habilitar o módulo Pet (em desenvolvimento).
- Correção no sistema novo de chave.
- Correção visual na Observação Personalizada.
- Adicionada funcionalidade da configuração "Exibir Desconto da Tabela de Preços" para a impressão da Requisição.
- Correção visual na impressão do orçamento.

### 3000.13 (21/08/2025)
- Novo recurso de para manter o Frete e/ou Substituição Tributária predefinidas no cadastro do produto ao invés de puxar os dados da nota do fornecedor.
- Refatoração na tela de lançamento de Observação Personalizada.
- Criado parâmetro para permitir que o usuário opte por utilizar a versão antiga da exportação para Excel.
- Correção de mensagem de erro na abertura do sistema.
- Correção no posicionamente dos dados do cliente ao enviar Orçamento via Whatsapp.
- Correção na impressão da nota promissória com validade jurídica.

### 3000.11 (19/08/2025)

**Adaptações para o modo Multi Empresa:**
- Relatório de Venda Bruta
- Relatório de Clientes

**Demais alterações:**
- Refatoração da impressão de nota promissória com validade jurídica.

### 3000.10 (19/08/2025)
- Novo relatório de Análise de Rentabilidade.
- Novo recurso de Observação Personalizada no Balcão Express.

### 3000.9 (15/08/2025)

**Adaptações para o modo Multi Empresa:**
- Filtro de cedente e remessa
- Contas a Pagar por Recorrência
- Vínculo entre formas de pagamento e contas bancárias

**Demais alterações:**
- Refatoração do Filtro Especial na tela de Busca de Vendas.
- Refatoração da Central de Comunicação (Whatsapp).

### 3000.8 (15/08/2025)

**Adaptações para o modo Multi Empresa:**
- Parcelamento de Contas a Pagar
- Histórico do estoque agora só exibe o da loja vinculada ao terminal do usuário.
- Nota Fiscal de Entrada: lançamento no estoque com o clique do botão direito do mouse.

### 3000.7 (14/08/2025)
- Correção no filtro de vendas permitindo que apareçam vendas com código negativo.
- Correção no lançamento de contas a pagar do modo Multi Empresa.
- Nova impressão de cupom ao gerar crédito de devolução.
- Locação: agora é possível selecionar o emitente para o cabeçalho da impressão.
- Ordem de serviço: o sistema agora permite o lançamento de itens com valor zerado.

### 3000.6 (13/08/2025)
- No modo Multi Empresa quando o usuário cria um cadastro de cliente puxando os dados a partir do CNPJ, agora o sistema vincula automaticamente o primeiro grupo da empresa que o usuário está logado.

### 3000.5 (13/08/2025)
- Ajustes visuais no Contas a Pagar por recorrência.
- Criada configuração "Exibir Desconto da Tabela de Preços" para que seja possível visualizar o desconto aplicado no Orçamento mesmo utilizando a configuração de Tabela de Preços.
- No módulo de Ordem de Serviço agora é possível alterar os campos Modelo e Identificação.
- Filtro de funcionários por empresa no modo Multi Empresa.

### 3000.4 (13/08/2025)

**Adaptações para o modo Multi Empresa:**
- Refatoração da tela de seleção de empresa
- Grupo de clientes
- Contas a pagar
- Nota Fiscal de entrada
- Relatório Demonstrativo de Vendas > Vendas Detalhado
- Tela de reimpressão de venda
- Contas bancárias
- Usuários

### 3000.3 (07/08/2025)
- Exportação de Excel para XLS, melhorando o desempenho e retirandoa a necessidade do cliente possuir uma licença do pacote Office.

**Demais alterações:**
- Configuração para o caminho padrão de salvamento do arquivo do Excel.

### 3000.2 (05/08/2025)
- Adaptações para sistema virtualizado.
