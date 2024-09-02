num = 0
media = 0
contador = 0
maior_menor = []
cont = 0

while cont != 1:
    num = float(input('Digite um número: '))
    contador += 1
    media += num

    maior_menor.append (num)

    if contador > 1:
        cont = int(input('''
        [1] encerrar programa
        [2] continuar: '''))
    if cont == 1:
        print('Obrigado por usar nosso programa')
    if cont == 2:
        print('')

print('Você digitou {} valores, o maior valor digitado foi {}, o menor foi {} e média desses valores foi {}'.format(contador, max(maior_menor),min(maior_menor), media / contador))