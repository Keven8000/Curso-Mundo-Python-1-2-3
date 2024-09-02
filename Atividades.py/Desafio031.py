print('-'*12, 'Bem-vindo a sua companhia de transporte','-'*12)
km = float(input('Quantos km tem a sua viagem: '))
if km<=200:
    print('O preço da sua passagem ficará R$ {:.2f}'.format(km*0.50))
else: 
    print('O preço da sua passagem ficará R$ {:.2f}'.format(km*0.45))
print('Obrigado por nós escolher, tenha um bom dia.')