n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

numeros = (n1, n2, n3, n4)
par = 0
if n1 % 2 == 0:
    par += 1 
elif n2 % 2 == 0:
    par += 1     
elif n3 % 2 == 0:
    par += 1
elif n4 % 2 == 0:
    par += 1      

print(f'Voce digitou os valores {numeros}')
print(f'o 9 aparace {numeros.count(9)} vezes')
print(f'o 3 aparece na posição {numeros.index(3)+1}°')
print(f'Tem {par} números')




