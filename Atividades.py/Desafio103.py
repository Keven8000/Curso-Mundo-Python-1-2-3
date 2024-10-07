def atleta(jogador = '', gols = 0 ):
    global nome_f
    nome_f = jogador
    if len(nome_f) < 1: 
        nome_f = 'Desconhecido'
    print(f'O atleta {nome_f} fez {gols} gols')
    

nome = str(input('Digite o nome do jogador: '))
gols = int(input('Digite quantos gols foram feitos: '))
atleta(nome, gols)

