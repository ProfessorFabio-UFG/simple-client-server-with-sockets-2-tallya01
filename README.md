# ClientServerBasics (2.0)

## Funções disponíveis
- `aniversario`: esta função recebe a data do seu aniversário (ou qualquer outra data no formato DD/MM), e retorna quantos dias faltam para o aniversário, isto é, para a próxima ocorrência dessa data.
- `bissexto`: esta função recebe um ano e identifica se o ano enviado é bissexto
- `adiciona`: esta função recebe uma data no formato DD/MM/AAAA e um número inteiro, e calcula a data adicionada da quantidade de dias. os parâmetros devem ser separados por vírgula. Por exemplo, `01/04/2025,10` adiciona 10 dias à data 01/04/2025

## Funcionamento do cliente
O cliente irá sempre solicitar uma função e seus parâmetros de entrada. 

Caso a função não exista ou ocorra algum erro, o servidor retornará a mensagem correspondente.