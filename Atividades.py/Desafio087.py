matriz = []
coluna1 = []
coluna2 = []
coluna3 = []
contagem = 0
soma_geral = 0

for c in range(0, 3):
    coluna1.append(int(input(f'Valor do [0, {contagem}]: ')))
    contagem += 1
contagem = 0
for c in range(0, 3):
    coluna2.append(int(input(f'Valor do [1, {contagem}]: ')))
    contagem += 1
contagem = 0
for c in range(0, 3):
    coluna3.append(int(input(f'Valor do [2, {contagem}]: ')))
    contagem += 1

matriz.append(coluna1[:])
matriz.append(coluna2[:])
matriz.append(coluna3[:])
soma_geral += sum(coluna1)
soma_geral += sum(coluna2)
soma_geral += sum(coluna3)
soma_terceira = sum(coluna3)

for c in range(0, 3):
    print(f'[ {matriz[0][c]} ]', end='')
print('')
for c in range(0, 3):
    print(f'[ {matriz[1][c]} ]', end='')
print('')
for c in range(0, 3):
    print(f'[ {matriz[2][c]} ]', end='')
print('')

print(f'A soma de todos valores é {soma_geral}')
print(f'A soma dos valores da terceira linha é {soma_terceira}')
print(f'O valor maior da segunda linha foi {max(coluna2)}')