idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você ainda é de menor, não precisa se alistar. Ainda lhe falta {} anos para poder se alistar'.format(18 - idade))
elif idade >= 18 and idade <= 45:
    print('Você já pode e deve se alistar')
elif idade > 45:
    print('Você já passou da idade de se alistar, devia ter se alistado no máximo a {} anos'.format(idade - 45))
