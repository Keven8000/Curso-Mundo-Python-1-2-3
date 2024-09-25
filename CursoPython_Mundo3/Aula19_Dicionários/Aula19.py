'''dicionário = dict() ou dicionário {}'''
dados = {}
dados = {'nome':'pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
'''Para adicionar'''
dados['sexo'] = 'Masculino'
print(dados)
'''Para remover'''
'''del dados['nome']
print(dados)'''

'''Os valores são as infomrmações dentro de dados'''
print(dados.values())
'''As chaves são onde guardam os valores'''
print(dados.keys())
'''Os itens é tudo'''
print(dados.items()) 

for k, v  in dados.items():
    print(f'O {k} é {v}')

'''Pode colocar dicionários dentro de listas '''

'''Para copiar em laços, usa .copy() invés de [:]'''  