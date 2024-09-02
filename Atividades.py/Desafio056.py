from math import floor

med = 0
idavelho = 0 
no_velho = ''
mulher_20 = 0
for c in range(1,5):
    no = str(input('Digite o nome: \n'))
    ida = int(input('Digite sua idade: \n'))
    sex = int(input("""Escolha o gênero:
    [1] Homem
    [2] Mulher
    [3] Prefiro não dizer\n"""))
    med += ida
    if ida > idavelho and sex == 1:
        idavelho = ida
        no_velho = no
    if ida < 20 and sex == 2:
        mulher_20 += 1
   
media = med / 4


print ('A idade média do grupo é de {:.0f} anos'.format(floor(media)))
print('O homem mais velho é {} com {} anos'.format(no_velho, idavelho))
if mulher_20 > 1 or mulher_20 == 0:
    print('Tem {} mulheres com mais de 20 anos'.format(mulher_20))
else: 
    print ('Tem {} mulher de 20 anos'.format(mulher_20))

