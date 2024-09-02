num = int(input('Digite um número inteiro: '))
opc = int(input("""Escolha uma das bases para conversão:
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL
Digite sua escolha: """))

if opc == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO ESCOLHIDA NÃO EXISTE. TENTE NOVAMENTE')