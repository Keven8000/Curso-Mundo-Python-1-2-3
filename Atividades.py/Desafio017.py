import math
oposto = float(input('Quanto mede o cateto oposto: '))
adjacente = float(input('Quanto mede o cateto adjacente: '))
hipo = math.sqrt(oposto**2 + adjacente**2)
# math.hypot poderia ser usado por ser o calcúlo da hipotenusa.
print ('Sua hipotenuza é {:.2f}'.format(hipo))