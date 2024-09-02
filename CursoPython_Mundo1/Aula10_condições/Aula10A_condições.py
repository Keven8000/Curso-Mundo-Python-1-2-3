# PRIMEIRA OPÇÃO:
tempo =int(input('Quantos de uso tem o seu carro:'))
# if é 'se'
if tempo<=3:
    print('Carro novo')
# else é 'senão'
else:
    print('Carro velho')

# SEGUNDA OPÇÃO
tempo =int(input('Quantos de uso tem o seu carro:'))
print('carro novo' if tempo<=3 else'carro velho')