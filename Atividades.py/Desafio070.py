total = mais_mil = preco = preco_barato = cont= 0
barato = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite preço: '))
    cont += 1
    
    total += preco
    if preco > 1000:
        mais_mil +=1
    if cont == 1 or preco < preco_barato:
        preco_barato = preco
        barato = nome
    else:
        if preco_barato > preco:
            barato = nome
        
    

    cont = int(input('[1] Continuar\n[2] Encerrar progama\n'))
    if cont == 2:
        break

print(f'''O total da compra foi {total}, {mais_mil} produtos custam mais de R$ 1000,00 e o produto mais barato é {barato}''')