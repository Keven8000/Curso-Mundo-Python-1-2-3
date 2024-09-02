pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
ter = int(input('Digite quantos termos você quer: ')) - 1
maxi = 0

print(pri)
while maxi != ter:
    
    res = raz + pri
    pri = res
    maxi += 1 
    print(res)

