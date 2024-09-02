import random
import time
numbers = random.randint(1,5)
numbere = int(input('Escolha um número de 1 a 5: '))
print('CONFERINDO RESULTADO...')
time.sleep(3)
if numbers == numbere:
    print('Parabéns você acertou e acaba de ganhar R$00,00',)
else: 
    print('O número sorteado foi {}, mais sorte na próxima vez'.format(numbers))