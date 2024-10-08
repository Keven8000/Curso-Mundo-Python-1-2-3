import operacoes
print('-'*30)
print('Sistema bancário'.center(30))
print('-'*30)


while True:
    opcoes = int(input('''
[1] depósito
[2] saque
[3] extrato
[4] Fechar sistema
'''))
    if opcoes == 1:
        print(operacoes.deposito())
    elif opcoes == 2:
        print(operacoes.saque())
    elif opcoes == 3:
        print(operacoes.extrato())
    elif opcoes == 4:
        print('Obrigado por usar nosso sistema')
        break
    else:
        print(f'[{opcoes}] não é válido, tente novamente')