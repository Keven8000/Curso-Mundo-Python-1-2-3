def leiaInt(n):
    if n.isdigit():
        return(f'O número digitado foi {n}')
    else:
        return('Você não digitou um número, tente novamente')
      



n = input('Digite um número: ')
print(leiaInt(n))