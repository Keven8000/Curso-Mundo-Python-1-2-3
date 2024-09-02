nome = input ('Digite o nome do aluno: ')
n1 = float (input ('Digite a n1: '))
n2 = float (input ('Digite a n2: '))
mb = (n1+n2)/2
print ('A n1 do aluno {} foi {}, a n2 foi {} e a sua média bimestral foi {}'.format(nome,n1,n2,mb))
if mb < 5:
    print('REPROVADO')
elif mb >= 5 and mb <= 6.9:
    print('RECUPERAÇÃO')
else:
    print ('APROVADO')