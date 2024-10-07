def um_a_dez():
    contagem = 0
    for c in range(0, 10):
        contagem += 1
        print(' ', contagem)
um_a_dez()


print('-'*7)


def dez_a_um():
    contagem = 10
    while True:
        print(' ', contagem)
        contagem -= 2
        if contagem < 0:
            break
dez_a_um()


print('-'*7)



def personalizado(inicio, fim, passo):
    if passo == 0:
        passo = 1
        
    if inicio < fim:
        if passo < 0:
            print('o passo que você escolheu não é aceitavel para está operação')
        else: 
            while True:
                print(inicio)
                inicio += passo
                if inicio > fim :
                    break
    
    elif inicio > fim:
        passo = abs(passo)
        while True:
            print(inicio)
            inicio -= passo
            if inicio < fim :
                break


inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
personalizado(inicio, fim, passo)