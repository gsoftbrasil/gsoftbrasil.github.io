# Wincash 3005
[Download](https://servidor.gsoft.com.br/wincash/3004/Wincash.exe)

### 3005.1 (11/12/2025)
* ``Ticket 9443``: Agora é possível visualizar no auditor do sistema quando uma operação de estoque é inserida, processada, desprocessada e excluída.
  <img width="1540" height="274" alt="image" src="https://github.com/user-attachments/assets/40c8bf05-f441-4836-bc57-738708074887" />

* ``Ticket 9442``: Agora é possível adicionar ou editar observações nos Kits. Para isso, siga estes passos: Selecionar o Kit e pressione o Enter > Clique em Alterar para Incluir uma nova observação ou editar existencia. > Após ajustar o texto, cliquem e Gravar para salvar alterações.
  <img width="1073" height="787" alt="image" src="https://github.com/user-attachments/assets/19a57867-e06d-49d0-ae7f-a768570d8132" />

* ``Ticket 9440`` : Corrigida divergência no relatório “Análise de Motivo de Perdas”, que apresentava valores diferentes do relatório “Volume de Itens Perdidos”.

* ``PR 403`` : Relatório de Vendas Sem Cupom. Como acessar: Aba Relatorios > Fiscal > Vendas sem Cupom.
  <img width="1032" height="772" alt="image" src="https://github.com/user-attachments/assets/477cb176-a6f6-4885-9426-c82aa99c595e" />

* ``Ticket 9420``: Corrigido o cálculo de ICMS na formação de preço externa, garantindo que os produtos e suas tabelas de preço sejam atualizados com os valores corretos.
  <img width="1037" height="788" alt="image" src="https://github.com/user-attachments/assets/2ff3cd05-7350-4e71-a667-b6f2c657b539" />

* ``PR 393`` : Corrigido a performance do LogTracer para evitar erros e padronizar o modelo de escrita dos logs.


# Wincash 3004
[Download](https://servidor.gsoft.com.br/wincash/3004/Wincash.exe)

### 3004.1 (28/11/2025)
* ``PR 389``: Correção da tela de fluxo de orçamentos que não abria caso não tivesse nenhum fluxo criado ainda.

*  ``PR 390``: Agora no fluxo de orçamentos, o sistema busca o vendedor pelo campo correto, garantindo que nome e informações exibidas estejam consistentes com o cadastro. 
  
* ``PR 394``: removido filtro de paginação no fluxo de orçamentos.
  
* ``Ticket 9435``: Agora, no relatório de estoque, o sistema aceita busca parcial, permitindo localizar resultados mesmo com parte do texto.
Antes, o filtro exigia que a operação fosse digitada exatamente como registrada.
  
* ``Ticket 9433``: Agora é possível filtrar por data no relatório de Cashback, caso nenhuma data seja informada, o sistema trará todos os registros.
  
  <img width="830" height="699" alt="image" src="https://github.com/user-attachments/assets/96b69c62-7e6e-4a31-907a-8e5764b837ee" />

* ``Ticket 9436``: Agora o sistema permite definir um limite específico de paginação nas configurações do sistema em: Produtos > Geral > Limite paginação histórico estoque.
  Esse valor é utilizado na paginação do Histórico de Estoque, garantindo mais controle sobre a performance e a quantidade de registros exibidos por vez. Por padrão, o sistema já vem configurado com o limite de 50 registros, mas você pode ajustar esse número conforme a sua necessidade diretamente nas configurações.
  
* ``PR 400``: Removido um cursor que executava rotinas de banco ao iniciar o sistema. A mudança melhora o desempenho e evita operações não necessárias.

### 3003.8 (19/11/2025)
* ``PR 386``: Corrigida arquivo INI da Api. A seção utilizada no arquivo INI mudou de REDE para INTEGRACAO.

### 3003.7 (18/11/2025)
* ``Ticket 9423``: Curva ABC agora contempla novo filtro, para trazer apenas os produtos com vinculo ao devlivery.
  
  <img width="1061" height="706" alt="image" src="https://github.com/user-attachments/assets/f4521c6d-c759-47bb-976d-4fcc430f56db" />
 
* ``Ticket 9427``: Agora o sistema valida o nome e a razão social do cliente para não permitir '\'.
Feito para evitar erros na geração de boleto de :
Erro ao gerar Boleto!, Cannot create file "C:\GSOFT\Wincash\Boletos FA EQUIPAMENTOS E MATERIAIS DE SEGURANCA LTDA\FA EQUIPAM - CONSORCIO EDECONSIL\JCGONTIJO - 12 - 2025 - 1201.pdf". O sistema não pode encontrar o caminho especifico.
  
* ``Ticket 9430``: Os valores do relatório de vendas semanal em: Relatórios > Dem. de Vendas > Relatórios de vendas semanal. Agora refletem exatamente o total vendido em cada dia da semana, mesmo em períodos longos. Relatório mais confiável para análise e tomada de decisão.

* ``Ticket 9421``: Agora é possível filtrar os produtos com ou sem classificação fiscal a fim de facilitar a manutenabilidade através do relatório por Excel.
Para utilizar a funcionalidade é necessário ativar nas permissões do usuário em Relatórios > Produtos > Por Classificação Fiscal.
O Relatório se encontra na aba: Relatórios > Produtos > Produtos - Classificação Fiscal.

  <img width="990" height="629" alt="image" src="https://github.com/user-attachments/assets/e56a4887-400e-4781-b493-8d8b9eb95dbe" />

* ``PR 382``: Criada permissão de usuário na aba de vendas para permitir acesso ao fluxo de orçamentos

### 3003.6 (14/11/2025)
* ``PR 376``: Corrigida lógica da promissória para não exibir mensagem se o recurso não estiver habilitado.

### 3003.5 (12/11/2025)
* ``PR 368``: Agora o 'OK' da tela de aviso da licença funciona corretamente fechando a tela.
* ``PR 368``: Adicionado logs no manifesto.
* ``Ticket 9393``: Agora, ao desfazer uma nota de entrada como uso e consumo, o estoque não será ajustado. Lembre-se que para funcionar corretamente é necessário ativar o parâmetro nas configurações:

  <img width="474" height="411" alt="image" src="https://github.com/user-attachments/assets/f090c054-ff8b-4953-a881-451ff979444a" />


### 3003.4 (05/11/2025)
* ``Ticket 9411``: Corrigido erro de estouro aritmético ao imprimir orçamentos, ajustando os campos e cálculos do DataSet para garantir maior estabilidade e precisão nos valores.
* ``PR 351``: Log no NFCeTop passa a ser obrigatório para maior controle.
* ``PR 352``: Adicionado log para exclusão de cupons e reorganização do script, garantindo melhor rastreabilidade e manutenção do código.
* ``PR 338``: Adicionada integração com ActiveX para a thread de inutilização e implementação do salvamento automático do XML de inutilização no log, além de melhorias de limpeza de memória e organização do código para maior estabilidade.
* ``PR 348``: Refatoração do módulo Orçamentos Fluxo, com inclusão de interfaces e classes, para acesso a dados, aprimoramento do serviço e atualização dos registros de dependência.
* ``PR 353``: Criada config para definir se o apiClient está ativo ou não
* ``PR 355``: Implementadas melhorias na emissão da NFC-e, incluindo checagem automática na SEFAZ para evitar duplicidades, exclusão protegida apenas para cupons rejeitados, mensagens mais claras de erro de NCM e maior estabilidade em falhas de retorno, além da correção de acentuação em relatórios e telas.

### 3003.3 (04/11/2025)
* ``PR 349``: Correção Access Violation ao abrir o sistema.

### 3003.2 (03/11/2025)
* ``PR 344``: Correções e melhorias no módulo de orçamentos, incluindo ajuste no campo ApenasDiasUteis, busca filtrada apenas por orçamentos, centralização de threads e reprocessamento automático ao sair da tela de fluxo.
* ``PR 345``: correções em buscas e threads, ajustes nos campos de configuração da API e melhoria no reprocessamento automático ao sair da tela de fluxo.

### 3003.1 (03/11/2025)
* ``PR 336``: Correção do erro que fazia alguns itens ficarem com valores zerados durante o fechamento no balcão express.
  
### ``Ticket 9376``: Fluxo de Orçamentos : Agora você consegue controlar melhor o ciclo de vida dos seus orçamentos.
- Ao abrir um orçamento, ele entra automaticamente na **etapa de prioridade 1**.  
- Conforme os dias passam, o sistema **move o orçamento para as próximas etapas**, de acordo com a quantidade de dias definida em cada card.  
- Assim, você visualiza facilmente o que está em aberto, em contato, em negociação, SAC etc.
<img src="https://github.com/user-attachments/assets/c10180cf-8d13-45bb-99a3-c485525fc86b" width="700" />

---

## Como configurar o Fluxo de Orçamentos

1. Acesse:  
   **Buscar Requisição / Orçamentos > Orçamento > Opções > Gerenciar Fluxo de Orçamentos**
2. Crie as **etapas (cards)**.
3. Defina a **quantidade de dias** que cada orçamento pode permanecer em cada etapa.
4. Salve.  
   A partir disso, o sistema organizará automaticamente os orçamentos nessas colunas.

---

## Configuração da Gsoft API (obrigatória)

No sistema:

1. Vá em **Configuração do Sistema > Integração > Geral > Gsoft API**.
2. Configure:

   - **Path do executável**  
     Caminho completo do `GsoftApiGUI.exe`.

     Estrutura recomendada da pasta da API:
     - `C:\GSOFT\GsoftApi\GsoftApiGUI.exe`
     - `C:\GSOFT\GsoftApi\WebView\` (arquivos da interface)
     - `C:\GSOFT\GsoftApi\Logs\`
     - `C:\GSOFT\GsoftApi\config.ini`

   - **Porta**  
     Sugestão: `12100` (ou outra porta livre).

   - **Host**  
     Normalmente: `localhost`.

Após configurado, o **GsoftApiGUI.exe é iniciado junto com o sistema principal** e permanece **na bandeja do Windows**, garantindo a integração necessária para o Fluxo de Orçamentos.

<img src="https://github.com/user-attachments/assets/94a7e5b5-fa00-4f5c-9ded-f3ace402ffd8" width="700" />

---

## Relatório de Fluxo de Orçamentos

Para acompanhar os resultados:

1. Acesse:  
   **Relatórios > Dem. de Vendas > Orçamentos - Etapas**
2. Filtre por **período** e **etapa**.
3. Visualize:
   - Quantidade de orçamentos
   - Soma total
   - Ticket médio
   - Lista detalhada por código, emissão, cliente, vendedor, etapa e valor
4. Exporte os dados em **CSV** ou **PDF** quando necessário.
 
<img src="https://github.com/user-attachments/assets/f06778d5-0d50-4ed4-880a-c0dccf24428b" width="700"/>

---

* ``Ticket 9407``: Agora quando houver falha no envio será criada uma lista de transmissão com os números que não foram enviados com sucesso.
Além disso foi implementado o botão de excluir na lista de transmissão.
<img width="1280" height="408" alt="image" src="https://github.com/user-attachments/assets/8fa6b9e4-8e86-4893-8747-8406615a899a" />
<img width="1017" height="266" alt="image" src="https://github.com/user-attachments/assets/3b4e89b4-d42e-4c7d-ab4d-a9b93d2dfdbf" />

* ``PR 335``: Ajuste manual de estoque com proteção a números exorbitantes.
* ``PR 341``: integração da chamada da API na abertura do balcão e ajustes gerais de estabilidade e validação nas telas do sistema.

### 3002.12 (29/10/2025)
* ``PR 328``: Adicionado SIGEM ao projeto de desenvolvimento.
* ``Ticket 9399``: Agora é possível consultar OS através do modelo.
  <img width="767" height="422" alt="image" src="https://github.com/user-attachments/assets/ad590c0e-de82-4dc6-8c8c-2700ef18dada" />

* ``Ticket 9402``: Criado parâmetro para não permitir a busca do produto por Código de barras na NFe de Entrada.
  <img width="632" height="795" alt="image" src="https://github.com/user-attachments/assets/cbf48cb4-9649-46ed-96c4-97c96bcb2da1" />

* ``PR 331``: Ajuste do campo PrecoVenda de Float para Decimal(18,2).

### 3002.11 (27/10/2025)
* ``PR 321``: Correção no cálculo do PIS e da COFINS, ajustando as alíquotas para serem divididas por 100 (ex.: 3% → 0,03 e 0,65% → 0,0065), garantindo compatibilidade com o cálculo feito pelo SAT.

### ``Ticket 9387``: Desmembramento de Produtos: Este recurso permite realizar o **desmembramento de produtos** diretamente no módulo de **Operações de Estoque**, possibilitando dividir um produto principal em produtos derivados, controlando **quantidade**, **perda**, **aproveitamento** e **rendimento**.  

A funcionalidade também mantém um **histórico detalhado** de todas as operações realizadas, permitindo auditoria completa dos desmembramentos efetuados no sistema.  

---

#### ⚙️ Localização no Sistema  

**Caminho:**  
```
Estoque → Operações de Estoque → Desmembramento de Produto
```

A tela principal é dividida em **duas abas**:

- 🧾 **Desmembramento** — utilizada para cadastrar, alterar e processar os desmembramentos ativos.  
- 📜 **Histórico** — utilizada para consultar operações já processadas e desprocessar quando necessário.  

---

#### 🪶 Aba: Desmembramento  

Nesta aba, o usuário pode **incluir, editar e processar** o desmembramento de produtos.

### 🔢 Campos Principais  

| Campo | Descrição |
|-------|------------|
| **Margem de quebra** | Percentual de perda esperada |
| **Peso Final** | Quantidade resultante após a margem |
| **Produto a desmembrar** | Produto principal que será dividido |
| **Produto desmembrado** | Itens derivados após o desmembramento |
| **Tipo Quant.** | Define se a quantidade é percentual (%) ou absoluta |
| **Perda** | Indica se o item é perda no processo |
| **Botão “Processar”** | Finaliza e grava o desmembramento lançando no histórico do estoque de cada item |
| **Data** | Data da operação |

---

#### 📜 Aba: Histórico  

Permite visualizar todos os desmembramentos já processados e desprocessados.
Desmembramentos desprocessados ficam sem a flag no campo Ativo

##### 🔍 Recursos Disponíveis  

- **Filtro por período** (data inicial e final)  
- **Listagem de operações:**  
  - Código  
  - Ativo
  - Produto  
  - Descrição  
  - Unidade  
  - Data  
  - Quantidade e perda  
- **Itens vinculados:** exibe os produtos gerados no desmembramento  
- **Desprocessar:** reverte o desmembramento e restaura o produto original  

---

#### ✅ Regras e Validações  

- Impede cadastrar **mais de um desmembramento ativo** para o mesmo produto (`Ativo = 1`).  
- Bloqueia a gravação caso a **soma das quantidades dos itens** ultrapasse o **peso final**.  
- Recalcula automaticamente as **quantidades e percentuais** quando a margem ou o peso são alterados.  
- O campo **Perda** é utilizado no cálculo de rendimento e aproveitamento.  

---

#### 🔄 Processamento Automático  

Durante o processamento do desmembramento:  

1. O sistema calcula o **peso final** com base na margem de quebra.  
2. Os **itens derivados** têm suas quantidades e percentuais recalculados automaticamente.  
3. O **histórico é atualizado** com o registro completo da operação.

---

* ``PR 317``: Legenda com o significado das siglas no grid.
 <img width="1055" height="757" alt="image" src="https://github.com/user-attachments/assets/481a917a-217b-4089-bc8e-539cfdb70219" />

* ``PR 320``: Criada a classe uExcel para permitir exportar os relatórios do NFeTop para Excel. 
* ``Ticket 9384``: Validação no campo de quantidade no balcão express para não permitir valores incoerentes.
<img width="800" alt="image" src="https://github.com/user-attachments/assets/954701f4-331c-4ce9-9eea-fdeccb524cc8" />

* ``PR 323``: Ajustada validação no campo qtde no ajuste manual do estoque.

### 3002.10 (22/10/2025)
* ``Ticket 9386``: Ajustada a validação da alíquota de ICMS para permitir o uso de alíquotas diferentes da alíquota interna.
*  ``Ticket 9389``: Durante a emissão do cupom, se acontecer algum erro, o sistema marca automaticamente a operação como “Erro”. Assim, o cupom é salvo apenas como “Gerado” e não é vinculado à venda.
*  ``Ticket 9272``: Adicionado botão para apagar o NumCOO com validação de cupons transmitidos e senha do dia, além do aumento no tamanho dos campos nProt e NumCOO.
  <img width="1031" height="320" alt="image" src="https://github.com/user-attachments/assets/a65eb1f6-b6f7-4663-a343-2525b7586c03" />


### 3002.9 (21/10/2025)
* ``Ticket 9386``: Removida a mensagem “Alíquota de ICMS inválida!” que impedia o cadastro de produtos com alíquota de 12%, mesmo quando já existia uma alíquota de 18% configurada para a UF da empresa.

### 3002.8 (17/10/2025)
* ``Ticket 9382``: Removida a conversão de texto UTF8 para ANSI no método de resposta, evitando erros de tipo (“invalid typecast”). Ajustado validação de licença na API para maior estabilidade.
* ``PR 312``: Melhoria e correções gerais na integração com a plataforma NAU.

### 3002.7 (16/10/2025)
* ``Ticket 9381``: DRE - Otimização: removida uma junção desnecessária na consulta de vendas, melhorando o desempenho. Adicionado indicador de atividade e otimizada a impressão de vendas, tornando o processo mais claro e rápido.

* ``Ticket 9380``: Tela de inicialização (splash) agora esconde corretamente durante o carregamento.

* ``Ticket 9378``: Agora no relatório de contas a receber é possível filtrar por notas com e sem NFe.
  <img width="1033" height="748" alt="image" src="https://github.com/user-attachments/assets/d2949e56-35ad-4175-9a2c-69e2b65aa2a1" />

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
[Download](https://servidor.gsoft.com.br/wincash/3001/Wincash.exe)

### 3001.12 (07/10/2025)
* ``PR 271``: Filtro de títulos recebidos considera flag para filtrar os inativos. O padrão traz apenas os ativos.
  
* ``Ticket 9357``: Movimentação bancária agora registra o detalhe da forma de pagamento baixada ou da venda realizada.
 <img width="1030" height="377" alt="image" src="https://github.com/user-attachments/assets/5223db1a-ffdd-44ac-84c8-ef1f482704f5" />


* ``Ticket 9363``: Adicionado campo previsão na OS.
 <img width="750" height="343" alt="image" src="https://github.com/user-attachments/assets/178a6d1f-60f7-45df-b39f-cd52ecb5234b" />


* ``PR 275``: Relatório de NFe agora permite a busca de numerações inutilizadas.
 <img width="1033" height="418" alt="image" src="https://github.com/user-attachments/assets/73c045fc-559b-42a2-ae39-a8e280b43a82" />


* ``Ticket 9371``: Melhora na inserção de títulos na NFe, evitando duplicatas ao adicionar registros já existentes.
* ``Ticket 9370``: Relatório de contas a receber geral agora exibe a coluna destino, em que mostra qual banco foi realizada a baixa.
   <img width="1034" height="742" alt="image" src="https://github.com/user-attachments/assets/03019c79-2a65-4579-a1d0-e0f0939f7b10" />

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
[Download](https://servidor.gsoft.com.br/wincash/3000/Wincash.exe)

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
