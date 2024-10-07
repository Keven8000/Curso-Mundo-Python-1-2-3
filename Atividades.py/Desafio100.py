from random import randint

numeros = []

def sorteio():
    for c in range(0, 5):
        numeros.append(randint(0, 100))
    print(f'Os números sorteados foram {numeros}')

 
def soma_par():
    soma = 0
    for c in range(0, len(numeros)):
        if numeros[c] % 2 == 0:
            soma += numeros[c]
    print(f'A soma dos números pares é {soma}')


sorteio()
soma_par()