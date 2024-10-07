def turma(*numbers):
    informacoes = {}
    informacoes['Quantidades de notas'] = len(numbers)
    informacoes['Maior Nota'] = max(numbers)
    informacoes['Menor Nota'] = min(numbers)
    m =  sum(numbers) / len(numbers)
    informacoes['Média da turma'] = f'{m:.2f}'
    if sum(numbers) / len(numbers) >= 7:
        informacoes['situação'] = 'Acima da média'
    else:
        informacoes['situação'] = 'Abaixo da média'
    print(informacoes)


turma(7, 10, 5, 6)


