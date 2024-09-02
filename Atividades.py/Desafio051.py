prim = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
dec = prim + (10-1) * raz
for c in range (prim, dec, raz ):
    print(c)