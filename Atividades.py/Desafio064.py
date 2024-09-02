num = dig = soma = 0


print('Para parar digite 999')
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    dig += 1

print('Você digitou {} números e a soma entre todos eles foi {}'.format(dig, soma - 999))
