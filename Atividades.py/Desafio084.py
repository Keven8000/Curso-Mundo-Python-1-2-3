dados = []
pessoas = []

pessoas_pesadas = []
pesos_pesados = []
pessoas_leves = []
pesos_leves = []
contagem = 0
cadastros = int(input('Quantos cadastros você irá fazer: '))

for p in range(0, cadastros):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])

    if contagem == 0:
        ''' Pessoas pesadas'''
        pesos_pesados.append(dados[1])
        pessoas_pesadas.append(dados[0]) 
        ''' Pessoas Leves'''
        pesos_leves.append(dados[1])
        pessoas_leves.append(dados[0])
        contagem += 1

    elif dados[1] >= pesos_pesados[0]:
        ''' Pessoas pesadas'''
        pesos_pesados.append(dados[1])
        if dados[1] > pesos_pesados[0]:
            pessoas_pesadas.clear()
        pessoas_pesadas.append(dados[0])
        pesos_pesados.clear()
        pesos_pesados.append(dados[1])

    elif dados[1] <= pesos_leves[0]:
        ''' Pessoas leves'''
        pesos_leves.append(dados[1])
        if dados[1] < pesos_leves[0]:
            pessoas_leves.clear()
        pessoas_leves.append(dados[0])
        pesos_leves.clear()
        pesos_leves.append(dados[1])
    dados.clear()

print(f'Você cadastrou {cadastros} pessoas')
print(f'As pessoas cadastradas foram {pessoas}')
print(f'O maior peso foi {pesos_pesados} de {pessoas_pesadas}')
print(f'O menor peso foi {pesos_leves} de {pessoas_leves}')
