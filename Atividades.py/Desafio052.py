num = int(input('Digite um número e descubra se ele é primo: '))
#for c in range(1, 1000000):
if num > 1 and num % 2 != 0 and  num % 3 != 0 and num % 5 != 0 and num % 11 != 0 and num % 1 == 0 and num % num == 0:
    print('O número {} é primo'.format(num))
elif num == 2:
    print('O número {} é primo'.format(num))
elif num == 3:
    print('O número {} é primo'.format(num))
elif num == 5:
    print('O número {} é primo'.format(num))
elif num == 11:
    print('O número {} é primo'.format(num))
else:
    print('Não é um número primo')