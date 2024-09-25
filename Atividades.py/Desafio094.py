geral = []
pessoa = {}
maior_media = []
media =  0


maxi = int(input('Quantas pessoas irá cadastrar: '))
for c in range(0, maxi):
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))
    geral.append(pessoa.copy())
    media += geral[c]['idade']
media = media / maxi

for i in range(0, maxi): 
    if geral[i]['idade'] > media:
        maior_media.append(geral[i])

print(f'''O total de pessoas cadastradas foi {maxi}\nA média de idade foi {media}\nPessoa(s) com idade acima da media:''')
for m in range(0, len(maior_media)):
    print(maior_media[m])


