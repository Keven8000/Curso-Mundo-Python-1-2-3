print ('='*15, 'PAGAMENTO DO ALUGUEL','='*15)
dias = int(input('Quantos dias ficou com o carro: '))
km = float(input('Quantos km foram rodados: '))
valor = (dias*60) + (km*0.15)
print('Você rodou por {} dias e rodou {}km, então o valor total ficou: R${:.2f}'.format(dias, km, valor))