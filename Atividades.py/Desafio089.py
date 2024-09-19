maximo = int(input('Digite quantos alunos você quer cadastrar: '))
dados = []
alunos = []

for x in range(0, maximo): 
    dados.append(str(input('Digite o nome do aluno: ')))
    dados.append(int(input('Digite a primeira nota do aluno: ')))
    dados.append(int(input('Digite a segunda nota do aluno: ')))
    alunos.append(dados[:])
    dados.clear()

print('Número', ' '*5, 'Aluno', ' '*5, 'Média')   
for c in range(0, maximo): 
    print(c, ' '*10, alunos[c][0], ' '*8, (alunos[c][1] + alunos[c][2])/2) 

while True:
    nota = int(input('De qual aluno você quer as notas: (999 interrompe): '))
    if nota == 999:
        break
    print(f'As notas de {alunos[nota][0]} são: {alunos[nota][1]}, {alunos[nota][2]}')
