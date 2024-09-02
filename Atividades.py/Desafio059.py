op = 0

while op != 5:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('=-='*12, 'MENU', '=-='*12)
    op = int(input("""[1] somar
[2] multiplicar
[3] maior valor
[4] digitar novos números
[5] fechar programa
opção desejada: """))
    if op == 1:
        res = n1 + n2 
        print('O resultado da sua soma foi: {}'.format(res))
    if op == 2:
        res = n1 * n2
        print('O resulltado da sua multiplicação foi {}'.format(res))
    if op == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        elif n2 > n1:
           print('O maior valor é {}'.format(n2))
        elif n1 == n2:
            print ("os valores sao iguas")
print('Obrigado por usar nosso programa =D')