import operacoes
print('-'*30)
print('Sistema bancário'.center(30))
print('-'*30)
 

while True:
    opcoes = int(input('''
[1] Depósito
[2] Saque
[3] Extrato
[4] Criar usuário
[5] Criar conta                       
[6] Fechar sistema
'''))
    if opcoes == 1:
        print(operacoes.deposito())
    elif opcoes == 2:
        print(operacoes.saque())
    elif opcoes == 3:
        print(operacoes.extrato())
    elif opcoes == 4:
        print(operacoes.criar_usuario())
    elif opcoes == 5:
        print(operacoes.criar_conta())
    elif opcoes == 6:
        print('Obrigado por usar nosso sistema')
        break
    else:
        print(f'[{opcoes}] não é válido, tente novamente')