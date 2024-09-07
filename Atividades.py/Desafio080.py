numbers = [1000]

for n in range(0,5):
    valor = int(input('Digite um valor de 1 a 999: '))
    if valor <= numbers[0]:
        numbers.insert(0, valor)
    elif valor <= numbers[1]:
        numbers.insert(1, valor)
    elif valor <= numbers[2]:
        numbers.insert(2, valor)
    elif valor <= numbers[3]:
        numbers.insert(3, valor)
    elif valor <= numbers[4]:
        numbers.insert(4, valor)
        
numbers.pop(-1)
print(numbers)