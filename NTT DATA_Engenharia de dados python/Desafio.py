'''def calcular_quadrado(numero):
    return numero ** 2

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(calcular_quadrado, numeros))
print(quadrados)
'''

def analise_vendas(vendas):
    # todo: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input('Digite as vendas de cada mês separando por vírgula apenas:  ').split(',')
    print(entrada)
    vendas = list(map(int, entrada))
    # todo: Converta a entrada em uma lista de inteiros:
    
    return vendas


vendas = obter_entrada_vendas()
print(analise_vendas(vendas))

'''-----------------------'''

def analise_vendas(vendas):
    # todo: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input().split(',')
    vendas = list(map(int, entrada))
    # TODO: Converta a entrada em uma lista de inteiros:
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))