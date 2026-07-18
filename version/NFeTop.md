# NFeTop 324
[Download](https://servidor.gsoft.com.br/NFeTop/324/NFeTop.exe)

A numeração do NFeTop passou da linha **323** para a **324** (publicação **324.2**; não há 324.1 nas releases).

### 324.2 (17/07/2026)
* ``PR 1013``: Correção do cálculo de **DIFAL** para consumidor final não contribuinte no **Espírito Santo** (cálculo por fora); melhorias no cadastro de alíquotas de ICMS.
* ``PR 958``: Correção na leitura do **certificado digital** — path e série passam a funcionar de forma independente.
* ``PR 863``: Painel de configuração da **NFSe Nacional** no NFeTop.

___

# NFeTop 323
[Download](https://servidor.gsoft.com.br/NFeTop/323/NFeTop.exe)

### 323.4 (29/05/2026)
* Revertida a validação da **Inscrição Estadual** por tipo de contribuinte do ICMS (``PR 825``).

### 323.3 (22/05/2026)
* ``PR 805``: Atualização do **NumNF nos títulos** ao transmitir, cancelar ou excluir NF-e; mantém NumNF na baixa parcial; melhoria de performance no auditor.
* ``PR 785``: Melhoria na **chave referenciada** de cupom fiscal (ECF/CF-e); bloqueio configurável para emissão de NF-e com cupons em contingência pendentes.

### 323.2 (19/05/2026)
* Publicação da versão **323.2** (build fiscal).

### 323.1 (15/05/2026)
* ``PR 766``: Validação do campo **Inscrição Estadual** conforme tipo de contribuinte do ICMS (ex.: não permite "ISENTO" para contribuinte de ICMS).
* ``PR 767``: Mensagem de erro mais clara quando a seleção de **CST** é inválida.
* ``PR 797``: Validação de CST usando a tabela virtual VtbValidaCST.
* ``PR 798``: Validação de **multitributação por NCM**.
* ``PR 768``: Correção na chave da **NFe_Cab** ao imprimir a **DANFE** (evita alteração indevida da chave).

___

# NFeTop 322
[Download](https://servidor.gsoft.com.br/NFeTop/322/NFeTop.exe)

### 322.1 (06/04/2026)
* Release conjunta com Wincash 3022.1 (build fiscal 322.1).

___

# NFeTop 321
[Download](https://servidor.gsoft.com.br/NFeTop/321/NFeTop.exe)

### 321.1 (02/04/2026)
* ``PR 658``: Implementação da **informação adicional ao Fisco** referente à LC 214/2025, quando qualquer item da nota possui CST de PIS e COFINS **06**.
* ``PR 640``: Correção da base de cálculo do **IBS e CBS**, utilizando o campo RTC_vBC em vez de Valor_Total_Liquido.

___

# NFeTop 320
[Download](https://servidor.gsoft.com.br/NFeTop/320/NFeTop.exe)

A numeração do NFeTop passou da linha **306** diretamente para a **320** (não há versões 307 a 319 publicadas nas releases).

### 320.2 (25/03/2026)
* ``PR 637``: Reforma tributária (RTC) — opção para **subtrair impostos da base de cálculo**.

### 320.1 (16/03/2026)
* Lançamento da linha **320** do NFeTop, em conjunto com Wincash 3020.1, NFCeTop 320 e MDFeTop 320 (``PR 610``).

___

# NFeTop 306
[Download](https://servidor.gsoft.com.br/NFeTop/306/NFeTop.exe)

### 306.8 (06/02/2026)
* ``PR 506``: Verificação para produtor rural: o sistema identifica se o cliente é produtor rural antes de preencher o Registro Estadual (IE), garantindo o tratamento correto na NF-e.
* ``PR 509``: Correção de frete duplicado na NF-e.

### 306.7 (29/01/2026)
* ``PR 486``: Correção na importação de venda com referência.
* ``PR 490``: Ajuste de configuração.
* ``PR 494``: Suporte ao indicador de consumidor final (código 202) na NF-e.

### 306.4 (23/01/2026)
* ``PR 461``: Correção no script de importação de documentos referenciados (empenho) na NF-e.
* ``PR 469``: Quando o produto não possui PIS ou COFINS informados, o sistema exibe tela para preenchimento antes da transmissão da NF-e.
* ``PR 481``: Correção na importação de venda.

### 306.3 (16/01/2026)
* ``PR 461``: Correção na importação de documentos referenciados (empenho) na NF-e.

___

# NFeTop 305
[Download](https://servidor.gsoft.com.br/NFeTop/305/NFeTop.exe)

A numeração do NFeTop passou da **301.17** diretamente para a linha **305** (não existem versões 302, 303 ou 304).

### 305.2 (11/12/2025)
* ``PR 398``: Reforma tributária — finalização da geração da NF-e validada no site do Governo.

___

# NFeTop 301
[Download](https://servidor.gsoft.com.br/NFeTop/301/NFeTop.exe)

### 301.17 (18/11/2025)
* ``Ticket 9425``: Agora o sistema valida se o cliente é PF ou PJ antes de atribuir a IE.  

### 301.16 (12/11/2025)
* ``Ticket 9414``: Corrigida a mensagem para retornar ao modo normal de emissão.  

### 301.15 (27/10/2025)
* Corrigida a exportação para Excel que deixou de funcionar desde a versão 300.

### 301.14 (07/09/2025)
* Melhorada a validação para não pular notas quando a série é diferente de 1.

### 301.13 (25/09/2025)
* As informações complementares agora apagam espaços em branco no início do texto.

### 301.11 (19/09/2025)
* Correção do erro "Connection is not defined" no cadastro de Informaçãos Adicionais e ICMS por Estados.

### 301.10 (17/09/2025)
* Correção na mensagem de erro ao tentar imprimir carta de correção.

### 301.9 (16/09/2025)
* Correção no cálculo do Imposto de Importação

### 301.8 (15/09/2025)
* Agora o NFeTop possui uma validação para evitar que o usuário pule a sequência das notas fiscais.

### 301.7 (10/09/2025)
- As informações complementares na NFE agora respeitam as quebras de linhas de acordo com o que o usuário digitar.

### 301.5 (03/09/2025)
- Refatoração no modo síncrono e pix (NFeTop).
- Correção de mensagem de erro ao transmitir a nota.

### 301.4 (01/09/2025)
- Refatoração para funcionar com o modo síncrono exigido pela SEFAZ.
- Adaptação do XML para popular a tag TpIntegra na forma de pagamento Pix.

___

# NFeTop 300

[Download](https://servidor.gsoft.com.br/NFeTop/300/NFeTop.exe)

### 300.2 (19/08/2025)
- Correção da conexão do NFeTop com o banco de dados.

### 300.1 (13/08/2025)
- Novo sistema de chave aplicado ao NFeTop.
