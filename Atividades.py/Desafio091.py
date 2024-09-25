from random import randint
from operator import itemgetter

resultado = {}

resultado ['jogador1'] = randint(0, 6)
resultado ['jogador2'] = randint(0, 6)
resultado ['jogador3'] = randint(0, 6)
resultado ['jogador4'] = randint(0, 6)
print(resultado)
resultado = sorted(resultado.items(), key=itemgetter(1))
print(f'''1° {resultado[0]}
2° {resultado[1]}
3° {resultado[2]}
4° {resultado[3]}''')

