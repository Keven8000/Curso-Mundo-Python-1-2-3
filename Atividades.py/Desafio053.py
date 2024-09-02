fra = str(input('Digite sua frase: ').upper()).split()
fra1 = ''.join(fra)
fra2 = fra1[::-1]
if fra1 == fra2:
    print('Sua frase é políndroma')
else: 
    print('Sua frase não é políndroma')