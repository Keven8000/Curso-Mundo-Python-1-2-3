km = int(input('Olá, a quantos km/h o carro passou? '))
multa = (km-80)*7
if km>80:
    print('O carro passou {} km/h a mais do que o permitido, ele será multado no valor de R$ {:.2f}'.format(km-80, multa))
else:
    print('O carro passou dentro da velocidade permitida, sem multas')
print('Obrigado por usar nosso programa')  