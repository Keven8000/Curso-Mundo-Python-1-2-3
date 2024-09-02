soma = cont = number = 0

while True:
    number = int(input('Digite um número:(999 para parar) '))
    if number == 999:
        break
    soma += number
    cont += 1 
print(f'Você digitou {cont} números e a soma deles foi {soma}')