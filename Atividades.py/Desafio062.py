pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
ter = int(input('Digite quantos termos você quer: '))
maxi = 0

print(pri)
while maxi != ter :
    res = raz + pri
    pri = res
    maxi += 1 
    print(res)
    if maxi == ter:
        cont = int(input('''Pronto!
        [1] encerrar progrma
        [2] para mostrar mais termos: '''))
        if cont == 1:
            print('Obrigado por usar nosso programa')
        if cont == 2:
            ter_mais = int(input('Digite quantos termos você quer: '))
            maxi == 0
            ter += ter_mais