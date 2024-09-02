prod = float(input('Digite o valor do produto: '))
form = int(input("""Formas de pagamento:
1 para dinheiro ou cheque - 10% de desconto
2 para á vista no cartão - 5% desconto
3 para até 2x no cartão - preço normal
4 para 3x ou mais no cartão - 20% de juros\n"""))

if form == 1:
    pag = prod - ((10*prod) / 100) 
    print('Seu produto é R$ {:.2f} e no dinheiro/cheque sairá por R$ {:.2f}'.format (prod, pag))

if form == 2:
    pag = prod - ((5*prod) / 100) 
    print('Seu produto é R$ {:.2f} e á vista no cartão sairá por R$ {:.2f}'.format (prod, pag))

if form == 3:
    pag = prod 
    par = pag / 2
    print('Seu produto é R$ {:.2f} e parcelado 2x no cartão sairá por R$ {:.2f}, cada parcela á R$ {:.2f}'
    .format (prod, pag, par))

if form == 4:
    pag = prod + ((20*prod) / 100) 
    parcelamento = int(input('Em quantos vezes o cliente quer parcelar:\n'))
    par = pag / parcelamento
    print('Seu produto é R$ {:.2f} e parcelado {}x no cartão sairá por R$ {:.2f}, cada parcela á R$ {:.2f}'
    .format (prod, parcelamento, pag, par))

if form < 1 or form > 4:
    print(' A OPÇÃO ESCOLHIDA NÃO EXISTE, TENTE NOVAMENTE')