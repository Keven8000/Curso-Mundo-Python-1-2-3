termos = int(input('Quantos termos você: '))
res1 = 1
res2 = 1
res3 = 0
maxi = 0

print('{} -> {} '.format(res1, res2), end='')
while termos - 2 != maxi:

    res3 = res2 + res1  # 1 + 1 = 2
    res1 = res2  # = 1
    res2 = res3  # = 2

    maxi += 1
    
    print('-> {}  '.format(res3, ), end='')
     
 