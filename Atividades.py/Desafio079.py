numbers = []
maximo = int(input('Digite quantos cadastros você quer fazer: '))
contagem = 0 

while True:
    cadastro = int(input('Digite o número de cadrasto: '))
    if cadastro not in numbers:
        numbers.append(cadastro)
        contagem += 1 
    else:
        cadastro = int(input(f'Digite outro número de cadrasto que não seja algum desses {numbers}: '))
        numbers.append(cadastro)
        contagem += 1
    if maximo == contagem:
        break
print(f'Os números cadastrados foram esses: {numbers}')
'''print(f'Os números cadastrados foram esses: {sorted(numbers)}')'''