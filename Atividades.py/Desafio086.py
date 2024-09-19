matriz = []
coluna1 = []
coluna2 = []
coluna3 = []
contagem = 0

for c in range(0, 3):
    coluna1.append(input(f'Valor do [0, {contagem}]: '))
    contagem += 1
contagem = 0
for c in range(0, 3):
    coluna2.append(input(f'Valor do [1, {contagem}]: '))
    contagem += 1
contagem = 0
for c in range(0, 3):
    coluna3.append(input(f'Valor do [2, {contagem}]: '))
    contagem += 1

matriz.append(coluna1[:])
matriz.append(coluna2[:])
matriz.append(coluna3[:])
print(matriz)

for c in range(0, 3):
    print(f'[ {matriz[0][c]} ]', end='')
print('')
for c in range(0, 3):
    print(f'[ {matriz[1][c]} ]', end='')
print('')
for c in range(0, 3):
    print(f'[ {matriz[2][c]} ]', end='')