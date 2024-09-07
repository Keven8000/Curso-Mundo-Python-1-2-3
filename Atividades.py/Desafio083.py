contagem = 0

expressao = str(input('Digite sua expressão: '))
contagem += expressao.count('(')
contagem += expressao.count(')')
if contagem % 2 == 0:
    validando = 'é valida'
else:
    validando = 'não é valida'
print(f'Sua expressão {validando}')
