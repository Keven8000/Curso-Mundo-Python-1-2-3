numbers = []

for n in range(0,5):
    valor = int(input('Digite um valor: '))
    numbers.append(valor)

if 5 in numbers:
    cinco = 'está'
else:
    cinco = 'não está'

print(f'Foram digitados {len(numbers)} valores')
print(f'A lista em ordem crescente fuca assim: {sorted(numbers)}')
print(f'O número 5 {cinco}')