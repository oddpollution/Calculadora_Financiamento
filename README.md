# Calculadora_Financiamento
App desenvolvido em Python conectado diretamente ao Banco Central, para calcular os fluxos baseados nas taxas de juros por modalidade dos Bancos Brasileiros

# Resumo

O código evoca um estudo sobre a utilização de APIs, GUIs e cálculo no desenvolvimento de uma ferramenta de finanças pessoais não existente atualmente.
Pode-se encontrar algo similar no site do Banco da Caixa Econômica federal, no entanto há a limitação dessa simulação ser feita apenas lá, forçando o interessado em adquirir uma linha de crédito a se sujeitar em um processo cruel, burocrático e exaustivo.


O código em questão busca exemplificar como pode-se cuidar das próprias finanças sem necessariamente depender de um sistema predatório para tal.


## Sobre

O código permite acessar as taxas praticadas, atualizadas no mercado de financiamento imobiliário diretamente pela API do Bacen, para os bancos que oferecem esse serviço (em geral se faz necessário compreender os regulamentos e política de aceitação para cada entidade).

## Funcionalidade

O código conta com uma API disponibilizada pelo Banco central para consultar os bancos e modelos de financiamento disponíveis, juntamente com o método de cálculo que pode ser escolhido para a aquisição do serviço.

### Método de Cálculo:
* _SAC_: Sistema de Amortização constante consiste em calcular a parcela a amortizar os juros juntamente com a parcela, sendo vantajoso por forçar o contratante a manter uma organização financeira inicial. Com o tempo as parcelas vão se reduzindo a ponto de representarem pouco impacto no decorrer do financiamento.
* _PRICE_: Sistema francês de amortizações consiste em manter a parcela fixa calculada até o final do contrato, sendo vantajoso por permitir que o cliente que possui organização financeira consiga constantemente prover amortizações no contrato ou pelo menos, tornar o financiamento bastante previsível.  

![image](https://github.com/oddpollution/Calculadora_Financiamento/assets/120825682/cc60f6cb-d1a3-477e-9ce0-18c170bab3a0)

### Banco e Modelo de Cálculo:
* _Banco_: Essa opção permite que se selecione a instituição disponibilizada pela API do Bacen para verificar qual taxa de juros é oferecida pela mesma.
* _Modelo de Cáculo_: Essa opção permite verificar qual opção pode ser mais vantajoso pelo momento econômico e pela tarifação realizada pelo banco.

![image](https://github.com/oddpollution/Calculadora_Financiamento/assets/120825682/d9f56327-e6fa-4739-bc74-6c283d7a5cd7)

### Informações Complementares:
* _Taxa de Juros_: Caso não seja selecionado um banco ou gostaria de se simular uma taxa oferecida por derterminada entidade, pode-se adicionar nesse campo uma taxa teorica.
* _Montante a ser Captado_: Valor total do contrato em questão.
* _Meses de Duração do Financiamento_: Meses de duração do contrato.

![image](https://github.com/oddpollution/Calculadora_Financiamento/assets/120825682/d0c37228-f6aa-448d-a814-cf44963f19c2)

### Resultados

* _Taxa de Juros Anual_: Taxa de Juros oferecida pelo Banco e modelo selecionados ou informada no campo acima.
* _Primeira Parcela_: Primeira parcela calculada, podendo ser a mesma até o final do contrato (PRICE) ou maior que as demais (SAC).
* _Total do Financiamento_: Valor total a ser pago para a instituição pelos dados informados.

![image](https://github.com/oddpollution/Calculadora_Financiamento/assets/120825682/80c62179-b1c6-4c6b-b1e0-3b711bf4f600)

### Botões

* _Calcular_: Calcula os resultados
* _Download_: Baixa o arquivo contendo o fluxo de pagamento ao longo do período informado, contendo as informações registradas acima.

### Exemplo

Em uma hipótese uma pessoa gostaria de efetuar a aquisição de um imóvel com as seguintes premissas:
* Serão necessários R$ 100.000 para completar o valor do imóvel;
* O cliente busca parcelas fixas;
* Para caber no bolso, o cliente prefere que sejam estendidas em 35 anos de pagamento (420 meses).

* _Resultados_:

![image](https://github.com/oddpollution/Calculadora_Financiamento/assets/120825682/e8ccb62b-c3c4-4671-95f9-b5d6ad655c20)


