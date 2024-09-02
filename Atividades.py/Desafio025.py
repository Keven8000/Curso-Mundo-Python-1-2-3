print ('-'*12, 'Primeira opção', '-'*12)
nome = input ('Digite seu nome completo: ').upper()
if 'SILVA' in nome:
    print ('Seu nome tem Silva')
else: 
    print ('Seu nome não tem Silva')
print ('-'*12, 'Segunda opção', '-'*12)
nome = input ('Digite seu nome completo: ').upper()
print ('Seu nome tem Silva:', 'SILVA' in nome)
