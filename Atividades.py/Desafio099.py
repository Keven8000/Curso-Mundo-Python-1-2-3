def maior(valores):
    return f'Os valores informados foram {valores} e maior valor informado foi {max(valores)}'


valores = []
maximo = int(input('Quantos valores você quer informar: '))

for c in range(0, maximo):
    valores.append(int(input('Digite o valor: ')))

print(maior(valores))
