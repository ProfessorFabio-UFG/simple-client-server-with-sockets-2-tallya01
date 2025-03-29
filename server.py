from socket  import *
from constCS import * #-
from datetime import datetime
from datetime import timedelta

def get_days_until_bday(date):
  splitted_date = date.split('/')
  day = int(splitted_date[0])
  month = int(splitted_date[1])

  today = datetime.today()
  current_year = today.year
    
  bday_this_year = datetime(current_year, month, day)
    
  if bday_this_year < today:
    bday_next_year = datetime(current_year + 1, month, day)
    return (bday_next_year - today).days

  return (bday_this_year - today).days

def is_leap(year):
  year = int(year)
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def add_days_to_date(date_str, days):
  date_obj = datetime.strptime(date_str, "%d/%m/%Y")
  new_date = date_obj + timedelta(days=days)
  return new_date.strftime("%d/%m/%Y")

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  splitted_data = bytes.decode(data).split(';')
  function = splitted_data[0]
  payload = splitted_data[1]

  return_data = 'Função não encontrada'

  if function == 'aniversario':
    return_data = f'Faltam {get_days_until_bday(payload)} dias para o seu aniversário!!!'
  if function == 'bissexto':
    return_data = f'O ano {payload}{'' if is_leap(payload) else 'não'} é bissexto'
  if function == 'adicionar':
    splitted_payload = payload.split(',')
    date = splitted_payload[0]
    days = int(splitted_payload[1])
    return_data = f'Após {days} dias a partir de {date} será dia {add_days_to_date(date, days)}'

  conn.send(str.encode(return_data+"*")) # return sent data plus an "*"
conn.close()               # close the connection