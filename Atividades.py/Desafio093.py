time = {}
gols = []


time['atleta'] = str(input('Nome do atleta: '))
partidas = int(input('Partidas jogadas: '))
time['partidas'] = partidas

for c in range(0, partidas):
    print('gols na ', c+1, '° partida: ', end= '')
    gols.append(int(input('')))


total_gols = sum(gols)
media_gols = total_gols / partidas
print(time, gols)
print(f'O atleta {time['atleta']} jogou {time["partidas"]} jogos')
print(f'Total de gols: {total_gols}\nMédia de gols por partida: {media_gols}')

for c in range(0, partidas):
    print('Gols feitos na ', c+1, f'° partida: {gols[c]}')