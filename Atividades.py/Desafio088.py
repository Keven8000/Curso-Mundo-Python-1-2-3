from random import randint 

print('-'*15, 'PROGRAMA DA MEGA SENA', '-'*15)

sorteio = []
jogos = []
megas = int(input('Quantos jogos você quer: '))

for c in range(0, megas):
    for x in range(0, 6):
        sorteio.append(randint(0,60))
    jogos.append(sorteio[:])
    sorteio.clear()

print(f'Jogo 1: {jogos[0]}\nJogo 2: {jogos[1]}\nJogo 3: {jogos[2]}\nJogo 4: {jogos[3]}\n')