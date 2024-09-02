import random
print('-'*12, 'SORTEADOR', '-'*12)
aluno1 = input ('Digite o nome do 1° aluno: ')
aluno2 = input ('Digite o nome do 2° aluno: ')
aluno3 = input ('Digite o nome do 3° aluno: ')
aluno4 = input ('Digite o nome do 4° aluno: ')
lista = aluno1, aluno2, aluno3, aluno4
print('A ordem dos alunos sorteados foram: {}'.format(random.sample(lista, 4)))
# random.shuffle poderia ser usado no lugardfrh
