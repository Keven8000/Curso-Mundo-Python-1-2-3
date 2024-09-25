from datetime import date
from datetime import datetime

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
nascimento = (input('Data de nascimento baseado no seguinte exemplo: 30/01/2000... '))
dias = date.today().day -  datetime.strptime(nascimento, '%d/%m/%Y').day
mes = date.today().month -  datetime.strptime(nascimento, '%d/%m/%Y').month 
ano = date.today().year -  datetime.strptime(nascimento, '%d/%m/%Y').year
mess = int(mes)
carteira = int(input('Número da carteira: (0 não tem)'))
if carteira != 0:
    contratado = int(input('Ano de contratação: '))
    aposentar = (contratado+20 ) - date.today().year
    pessoa['aposentadoria'] = aposentar
pessoa['idade'] = ano
pessoa['carteira'] = carteira


if carteira != 0:
    pessoa['contratação'] = contratado
    pessoa['salário'] = int(input('Salário: '))

print(f'{pessoa['nome']}\n{pessoa['idade']} anos\nNúmero da CTPS: {pessoa['carteira']}')
if carteira != 0:
    print(f'Ano de contratação: {pessoa['contratação']}\nSalário: {pessoa['salário']}')
    if aposentar <= 0:
        print('Aposentadoria: Já pode se aposentar')
    else:
     print(f'Aposentadoria: falta {pessoa['aposentadoria']} anos de contribuação')