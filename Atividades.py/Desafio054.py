from datetime import date
from datetime import datetime

soma = 0 

for c in range(1, 8):
    nascimento = (input('Digite a data de nascimento do atleta baseado no seguinte exemplo: 30/01/2000... '))
    dias = date.today().day -  datetime.strptime(nascimento, '%d/%m/%Y').day
    mes = date.today().month -  datetime.strptime(nascimento, '%d/%m/%Y').month 
    ano = date.today().year -  datetime.strptime(nascimento, '%d/%m/%Y').year
    mess = int(mes)

    if mes > 0: 
        idade = ano 
    elif mes < 0:
        idade = ano - 1
    elif mes == 0:
        if dias <= 0:
            idade = ano
        elif dias > 0:
            idade = ano - 1
    if idade >= 18:
        print (soma)
        soma += + 1
    dimi = c - soma
print('{} pessoas são de maiores e {} ainda são de menor'.format(soma, dimi))
