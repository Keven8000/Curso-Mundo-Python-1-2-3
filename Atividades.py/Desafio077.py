palavras = 'arroz', 'nos', 'sla', 'pai', 'turismo'
for n in palavras: 
    print(f'\nNa palavra {n} tem as vogais ', end='')
    for vogais in n:
        if vogais in 'aeiou':
            print(vogais, end=' ')