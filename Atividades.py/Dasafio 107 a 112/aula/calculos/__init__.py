def metade(preco):
    res = preco / 2
    return moeda(res)


def dobro(preco):
    res = preco * 2
    return moeda(res) 

def aumentar(preco, porc):
    valor = preco / 100 * porc
    res = valor + preco
    return moeda(res)

def diminuir(preco, porc):
    valor = preco / 100 * porc
    res = preco - valor
    return moeda(res)

def moeda(din):
    return f'R${din:.2f}'

def resumo(preco):
    sla = f'{preco}'
    if type(preco) is float:
        print(f'''\nPREÇO: R${preco:.2f}
    METADE: {metade(preco)}
    DOBRO: {dobro(preco)}
    10% A MAIS: {aumentar(preco, 10)}
    13% A MENOS: {diminuir(preco, 13)}
    '''.replace('.', ','))
    else:
        print(f'{sla.strip()} não é um valor aceito, tente novamente')

