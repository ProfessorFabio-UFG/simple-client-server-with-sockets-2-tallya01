from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

print('------ Bem vindo! ------\n')
print('Funções disponíveis:')
print('aniversario - Recebe a data do seu aniversário (DD/MM) e calcula quantos dias faltam para o seu próximo aniversário')
print('bissexto - Recebe um ano e identifica se esse ano é bissexto')
print('adicionar - Recebe uma data (DD/MM/YYYY) e uma quantidade de dias, e retorna a data adicionada dessa quantidade de dias. Os parâmetros devem ser separados por vírgula, exemplo: "01/04/2025,10"\n')

function = input('Escolha uma função: ')
params = input('Digite os dados de entrada: ')
s.send(str.encode(f'{function};{params}'))  # send some data
data = s.recv(1024)     # receive the response
print (bytes.decode(data))            # print the result
s.close()               # close the connection
