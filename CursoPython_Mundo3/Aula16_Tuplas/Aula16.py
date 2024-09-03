# tuplas são IMUTÀVEIS
lanche = ('arroz', 'suco', 'pizza', 'feijão')
'''
while True:
    for comida in lanche:
        print(f'eu vou cumerrr {comida}')
    if comida == 'feijão':
        break
for c in range(0 , len(lanche)):
    print(f'eu vou cumerrr {lanche[c]}')

for posição, comida in enumerate(lanche):
    print(f'eu vou cumerrr {comida} que está na posição {posição}')'''

a = (1, 5, 6)
b = (4, 6, 7, 8)
c = a + b
print (max(c))
print (min(c))
print (f'Quantas vezes aparece o número 6? aparece : {c.count(6)} vezes')
print (f'Qual posição está o 4? aparece na posição {c.index(4)} ')

#tuplas pode ter dado de mais de um tipo, ex:
pessoa = 'gustavo', 15, 'sla', 99.88
#Unico mudança que se pode fazer com uma tupla é apenas apagar ela toda assim:
del(pessoa)