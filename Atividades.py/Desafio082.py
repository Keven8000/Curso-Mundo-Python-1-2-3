numbers = []
par = []
impar = []

for n in range(0,5):
    valor = int(input('Digite um valor: '))
    numbers.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 != 0:
        impar.append(valor)

print(f'Todos valores {numbers}')
print(f'Valores pares {par}')
print(f'Valores ímpares {impar}')



