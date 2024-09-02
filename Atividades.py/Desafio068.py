from random import randint

vitorias = 0
while True:
    # Obtendo dados e resultados
    opc_player = int(input('[1] par\n[2] ímpar\n'))
    player = int(input('Digite seu número entre 1 e 10: '))
    comp = randint(1,10)
    print(comp, 'comp')
    res = (player + comp ) % 2
    # Definindo ganhador
    if res == 0 and opc_player == 1:
        print('Você ganhou')
        vitorias += 1 
    elif res == 1 and opc_player == 2:
        print('Você ganhou')
        vitorias += 1 
    else:
        break


if vitorias > 1 or vitorias == 0:
    print(f'Você ganhou {vitorias} vezes')
else:
    print('Você ganhou 1 vez')