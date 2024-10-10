conta = 0
operacoes_extratos = ''
usuarios = []
contas = []
 

def deposito():
    global conta
    global operacoes_extratos
    valor_deposito = str(input('Digite o valor que deseja depositar: ').replace(',', '.'))
    valor_deposito = float(valor_deposito)


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
    valor_saque = str(input('Digite o valor que deseja sacar: ').replace(',', '.'))
    valor_saque = float(valor_saque)

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


def criar_usuario():
    from datetime import date
    from datetime import datetime

    global usuarios
    dados = {}

    while True: 
        dados.clear()
        print('000 para PARAR')
        dados['cpf'] = int(input('Digite seu cpf: ').replace('.', ''))
        procurando = [chave['cpf'] for chave in usuarios]
        if dados['cpf'] == 000:
            break
        elif dados['cpf'] in procurando :
            print('Esta pessoa já está cadastrada, não é possível cadastrar novamente')
            break
        else: 
            dados['nome'] = str(input('Nome completo: '))
            nascimento = (input('Digite a data de nascimento baseado no seguinte exemplo: 30/01/2000... '))
            dias = date.today().day -  datetime.strptime(nascimento, '%d/%m/%Y').day
            mes = date.today().month -  datetime.strptime(nascimento, '%d/%m/%Y').month 
            ano = date.today().year -  datetime.strptime(nascimento, '%d/%m/%Y').year
            if mes > 0: 
                idade = ano 
            elif mes < 0: 
                idade = ano - 1
            elif mes == 0:
                if dias >= 0:
                    idade = ano
                elif dias < 0:
                    idade = ano - 1
            dados['nascimento'] = idade
            dados['endereco'] = str(input('Digite o seu endereço no seguinte formato "logradouro, núm - bairro - cidade/sigla estado": '))
            usuarios.append(dados.copy())
    return usuarios


def criar_conta():
    global usuarios, contas
    dados = {}
    

    while True:
        print('000 para PARAR')
        dados['cpf'] = int(input('Digite o cpf: ').replace('.', ''))
        procurando = [chave['cpf'] for chave in usuarios]
        if dados['cpf'] == 000:
            break
        elif dados['cpf'] in procurando :
            contas_existente = len(contas) + 1
            dados['agência'] = '0001'
            dados['numero_conta '] = contas_existente         
            contas.append(dados.copy())
        else: 
            print('Não existe nenhuma usúario cadastrado no nosso banco com esse cpf, primeiro cadastre o usuário para poder criar uma conta')
            break
        
    return contas