maior = ['smd', 98, 'sla']
print(len(maior))

meu_dicionario = {'b': 2, 'a': 50, 'c': 3}
dicionario_ordenado = sorted(meu_dicionario.items())
print(dicionario_ordenado)
  
from operator import itemgetter
    
meu_dicionario = {'b': 2, 'a': 50, 'c': 3}
dicionario_ordenado = sorted(meu_dicionario.items(), key=itemgetter(1))
print(dicionario_ordenado)

from datetime import date
from datetime import datetime

contratado = int(input('Ano de contratação: '))
aposentar = (contratado+20 ) - date.today().year
print(aposentar)