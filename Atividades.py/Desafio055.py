lista = []

for c in range(1,6):
    kg = float(input('Digite seu peso em KG: '))
    lista.append(kg)

#print(lista)
mai = max(lista)
men = min(lista)
print('O maior peso lido  foi {}Kg e o menor peso lido foi {}kg'.format(mai, men))