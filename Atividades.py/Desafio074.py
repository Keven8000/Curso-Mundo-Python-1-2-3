from random import randint 
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
'''for c in range(0, 5):
    numeros += (randint(0, 10))
    print(numeros)'''
print(f'Os números gerados foram {numeros}')
print(f'O maior numero foi {max(numeros)}')
print(f'O menor numero foi {min(numeros)}')