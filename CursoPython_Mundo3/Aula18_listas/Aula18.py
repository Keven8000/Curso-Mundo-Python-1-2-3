'''dados = []
dados.append('Pedro')
dados.append(27)
print(dados,' -- dados')
pessoas = []
pessoas.append(dados[:])
print(pessoas, '-- pessoas')'''

'''pessoas = [['Pedro', 25], ['Julia', 17], ['Anna', 17]]
print(pessoas[0][1])

pessoas = [['Pedro', 25], ['Julia', 17], ['Anna', 17]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')
for c in range(0,len(pessoas)):
    print(f'{pessoas[c][0]} tem {pessoas[c][1]} anos ')
'''

galera = []
geral = []
for c in range(0,3):
    galera.append(str(input('Nome: ')))
    galera.append(int(input('idade: ')))
    geral.append(galera[:])
    galera.clear()
print(galera)