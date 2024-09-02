peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = (peso / altura) / altura
print(imc)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso'.format(imc))
if imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} e você está com peso ideal'.format(imc))
if imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso'.format(imc))
if imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f} e você está com obesidade'.format(imc))
if imc > 40:
    print('Seu IMC é {:.2f} e você está obesidade mórbida'.format(imc))

    