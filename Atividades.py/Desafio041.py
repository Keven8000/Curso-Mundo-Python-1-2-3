# CODIGO DESGRÇADO
from datetime import date
from datetime import datetime


nascimento = (input('Digite a data de nascimento do atleta baseado no seguinte exemplo: 30/01/2000... '))
dias = date.today().day -  datetime.strptime(nascimento, '%d/%m/%Y').day
mes = date.today().month -  datetime.strptime(nascimento, '%d/%m/%Y').month 
ano = date.today().year -  datetime.strptime(nascimento, '%d/%m/%Y').year
if mes > 0: 
    idade = ano 
elif mes < 0: 
    idade = ano - 1
elif mes == 0:
    if dias >= 0:
        idade = ano
    elif dias < 0:
        idade = ano - 1
print('O atleta tem {} anos'.format(idade))

if idade <= 9: 
    print('O atleta irá competir na cartegoria mirim')
if idade <= 14 and idade > 9: 
    print('O atleta irá competir na cartegoria infaltil')
if idade <= 19 and idade > 14: 
    print('O atleta irá competir na cartegoria junior')
if idade == 20: 
    print('O atleta irá competir na cartegoria sênior')
if idade > 20: 
    print('O atleta irá competir na cartegoria master')