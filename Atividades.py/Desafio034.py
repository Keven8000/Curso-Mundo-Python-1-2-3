sala = float(input('Digite seu salário: '))
aum10 =   (sala*10)/100 + sala
aum15 =   (sala*15)/100 + sala
if sala <= 1250.00:
    print('Seu salário teve um aumento de 15% e ficou R${}'.format(aum15))
if sala > 1250.00:
    print('Seu salário teve um aumento de 10% e ficou R${}'.format(aum10))