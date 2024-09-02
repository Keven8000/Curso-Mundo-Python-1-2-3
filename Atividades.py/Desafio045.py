import random

print('-=-'*12, 'JO-KEN-PÔ', '-=-'*12)
#pedra = 1
#tesoura = 2
#papel = 3

com = random.randint(1, 3)
player = int(input("""Escolha seu ataque: 
1 = Pedra
2 = Tesoura
3 = Papel\n"""))

if com == 1 and player == 1 or com == 2 and player == 2 or com == 3 and player == 3:
    print('Os dois empataram')

elif com == 1 and player == 2:
    print('Eu joguei pedra, eu venci huahuahua')

elif com == 1 and player == 3:
    print('Eu joguei pedra, você venceu...')

elif com == 2 and player == 1:
    print('Eu joguei tesoura, você venceu...')

elif com == 2 and player == 3:
    print('Eu joguei tesoura, eu venci huahuahua')  

elif com == 3 and player == 1:
    print('Eu joguei papel, eu venci huahuahua')  

elif com == 3 and player == 2:
    print('Eu joguei papel, você venceu...')  

#print(com)