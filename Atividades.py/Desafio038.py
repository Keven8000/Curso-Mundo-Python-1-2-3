n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior, ele é {}'.format(n1))
elif n2 > n1:
    print('O segundo valor é maior, ele é  {}'.format(n2))
else:
    print('Não existe valor maior,  os dois são iguais.')