from random import randint

numbers = []
for c in range (0,5):
    numbers.append(randint(0, 1000))
maxi = max(numbers)
mini = min(numbers)

print(f'Os números gerador foram {numbers}')
print(f'O maior valor foi {maxi}, ele está na posição {numbers.index(maxi)+1} e o menor valor foi {mini}, ele está na posição {numbers.index(mini)+1}')
