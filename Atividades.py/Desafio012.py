print('-'*12, 'LIQUIDAÇÃO ESPECIAL', '-'*12)
pro = int(input('Valor do produto: '))
des = pro*(5/100)
print('Seu produto recebeu {} reias de desconto, então ficou por {}'.format(des,pro-des))