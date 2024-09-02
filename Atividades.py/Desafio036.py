print('\033[1;31;40m-=-\033[m'*12, '\033[1;31;40mFINANCIAMENTO DE CASAS\033[m', '\033[1;31;40m-=-\033[m'*12)
casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o salário do financiador: '))
meses = float(input('Em quantos meses o financiador deseja pagar: '))
entrada = float(input('Qual o valor da entrada do financiador: '))
casaen = casa - entrada
prestacao = casaen / meses
maximo = (30 * salario) / 100
if maximo >= prestacao:
    print("""O financiador está autorizado a financiar a casa, dando uma entrada de R$ {:.2f},
          pagando em {:.2f} meses e com uma prestação de R$ {:.2f}"""
          .format(entrada, meses, prestacao))
else: 
    print("""O financiador não bater o requesito necessário para financiar a casa,
          que é a prestação mensal não passar de 30% do seu salário.
          Caso o financiador queira, ele pode aumentar o valor da entrada ou aumentar
          o tempo de pagamento.""")
    