n = int(input('Digite o numero que você quer fatorar: '))
fat = n 
res = 0
while fat != 1:
    fat -= 1
    res = n * fat
    n = res
    print(res)