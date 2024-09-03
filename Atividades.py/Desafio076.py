produtos = ('xbox one s', 2450.49, 'Cadeira gamer', 770.00, 'Monitor 19 Polegadas', 450.00)
'''print(f
{produtos[0]}, por R$ {produtos[1]}
{produtos[2]}, por R$ {produtos[3]}
{produtos[4]}, por R$ {produtos[5]}
)'''
for pos in range(0, len(produtos)):
    if pos % 2 == 0: 
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')