n1 = float(input('Digite a primeira reta: '))
n2 = float(input('Digite a segunda reta: '))
n3 = float(input('Digite a terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('È possível formar um triângulo.')
else: 
    print('Não é possível formar um triângulo')