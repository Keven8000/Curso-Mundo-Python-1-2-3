# Se = if --- elif = senão se --- else= senão
Nome = int(input('Digite sua idade: '))
if Nome < 18:
    print('Você ainda é de menor, não pode beber, dirigir, vá estudar.')
elif Nome >= 18 and Nome <= 65 :
    print('Você já é adulto, vá trabalhar e cuidar da sua família')
else: 
     print('Vá aproveitar o resto de sua vida com sabedoria e paz')    