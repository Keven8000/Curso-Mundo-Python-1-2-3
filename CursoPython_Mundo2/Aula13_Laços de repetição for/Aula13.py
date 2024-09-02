# laço c no intervalo(1,10):
    #passo
#pega
# for c in range(1,10):
 #passo
#pega
# for c in range(0,3)
    #if se tiver moeda:
        #pega
    #passo
    #pula
#passo
#pega

for c in range (0, 6):
    print(c)
print('fim')

for c in range (6, 0, -1):
    print(c)
print('fim')

for c in range (0, 6, 2):
    print(c)
print('fim')

soma = 0
for c in range(0, 3):
    num = int(input('Digite um valor: '))
    soma += num
print(soma)

i = int(input('Início: '))
f = int(input('Fim: '))
p= int (input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim') 