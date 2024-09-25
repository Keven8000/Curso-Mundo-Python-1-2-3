dados = {}
resultados = []
for c in range(0, 3):
    dados ['aluno'] = str(input('Nome do aluno: '))
    media  = float(input('Média do aluno: '))
    dados ['média'] = media
    if media >= 7: 
        dados['situação'] = 'aprovado'

    else:
        dados['situação'] = 'reprovado'
    resultados.append(dados.copy())


print(dados)
print(resultados)

for e in resultados:
        print(e)

