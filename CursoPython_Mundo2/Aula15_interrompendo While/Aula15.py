# interrompa = break

'''c = 0

while True: 
    c += 1
    print (c)'''


n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma foi {s}')