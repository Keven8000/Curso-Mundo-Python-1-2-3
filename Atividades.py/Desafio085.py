par = []
impar = []
geral = []

for c in range(0,7):
    numero = int(input('Digite um valor: '))

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
       
par.sort()
impar.sort()
geral.append(par[:])
geral.append(impar[:])   
print(geral)
print(f'Os valores pares foram {geral[0]}')
print(f'Os valores impares foram {geral[1]}')