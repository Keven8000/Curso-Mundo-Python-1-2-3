from random import randint
from time import sleep
comp = randint(1, 10)
player = 0
tentativas = 0

print('=-='*12, 'JOGO DA ADVINHAÇÃO 100% ATUALIZADO', '=-='*12)

while comp != player:
    player = int(input('Advinhe o número que estou pensando entre 1 e 10: '))
    print ('Processando...')
    sleep(3)
    if comp != player:
        print('ERROUUUUUUUU, tenta dnv ai kkkkkkkkkkkkkkkkkkkkkkkkk')
    tentativas += 1

if tentativas < 5:
    print('Né que acertou, você tentou {} vezes'.format(tentativas))
else:
    print('Mas também, depois de {} vezes fica fácil'.format(tentativas))