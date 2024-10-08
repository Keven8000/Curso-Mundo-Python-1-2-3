conta = 0
operacoes_extratos = ''



def deposito():
    global conta
    global operacoes_extratos
    valor_deposito = float(input('Digite o valor que deseja depositar: '))
    
    if valor_deposito <= 1:
        print('Não é possível depositar valores abaixo de R$1,00')
    else: 
        conta += valor_deposito
        operacoes_extratos += f'Depósito R${valor_deposito:.2f}\n'
    return f'saldo: R${conta:.2f}'.replace('.', ',')


def saque():
    global conta 
    global operacoes_extratos
    saques_maximos = 0
    valor_saque = float(input('Digite o valor que deseja sacar: '))

    if valor_saque > conta:
        print('Saldo Insuficiente')

    elif valor_saque > 500:
        print('Saques acima de R$500,00 apenas na central do banco')

    elif valor_saque < 500 and saques_maximos != 3: 
        conta -= valor_saque
        operacoes_extratos += f'Saque R${valor_saque:.2f}\n'
        saques_maximos += 1
    return f'saldo: R${conta:.2f}'.replace('.', ',')


def extrato():
    global conta
    global operacoes_extratos

    print('-'*15)
    print('EXTRATO'.center(15))
    print('-'*15)

    print(f'''
Saldo na conta: R${conta:.2f}
Operações feitas: 
{operacoes_extratos}
'''.replace('.', ','))
