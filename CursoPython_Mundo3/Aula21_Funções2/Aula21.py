def um_a_dez(i, f, p):
    '''
    i para inicio
    f para fim
    p para passo

    Função criada por keven
    '''
    while i <= f:
        print(i)
        i += p


um_a_dez(0, 12, 1)

help(um_a_dez)


'''Parâmetro opcionais'''
def somar(a, b, c = 0):
    s = a + b + c
    print(s)

somar(1, 2)


'''Escopo variável'''

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2
print(f'No programa principal, n vale {n} pois é uma variável global')
teste()
print(f'No programa principal, x não existe pois ele tem apenas acesso local na função teste, pois é uma variável local  ')


'''Funções com return'''

def somar(a = 0, b = 0, c = 0):
    s = a + b + c

    return s
 
resp1 = somar(7, 2)
resp2 = somar(1, 2, 4)
resp3 = somar(1, 10, 11)

print(f'Os resultados foram {resp1}, {resp2} e {resp3}')