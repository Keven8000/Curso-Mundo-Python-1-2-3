time = {}
gols = []
time_total = []
gols_total = []
maxi = int(input('Quantos atletas irá analisar: '))

for c in range(0, maxi):
    time['atleta'] = str(input('Nome do atleta: '))
    partidas = int(input('Partidas jogadas: '))
    time['partidas'] = partidas
    time_total.append(time.copy())
    for c in range(0, partidas):
        print('gols na ', c+1, '° partida: ', end= '')
        gols.append(int(input('')))
    gols_total.append(gols[:])
    gols.clear()

print(gols_total)
print(time_total)

for a in range(0, maxi):
    print(f'- O atleta {time_total[a]['atleta']} jogou {time_total[a]['partidas']} jogos')
    print(f'''- Total de gols: {sum(gols_total[a])}\n- Média de gols por partida: {(sum(gols_total[a])) / time_total[a]['partidas'] }''')

    for g in range(0, time_total[a]['partidas']):
        print('- Gols feitos na ', g+1, f'° partida: {gols_total[a][g]}')