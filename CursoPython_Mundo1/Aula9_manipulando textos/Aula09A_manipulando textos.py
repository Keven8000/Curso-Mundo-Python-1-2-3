frase = ('Macarrão com Frango é Muito bom')
frase1 = ('   Macarrão com Frango é Muito bom  ')
# str 9
print (frase[9])
# str 9 a 13
print (frase[9:13])
# str 9 a 29 pulando de 2 em 2
print (frase[9:29:2])
# str do começo a 5
print (frase[:5])
# str do 20 ao fim
print (frase[20:])
#str do 9 ao fim pulando de 2 em 2
print (frase[9::2])
# len sever para contar quantos caracteres tem
print (len(frase))
# frase.count('letra') contará quantas vezes alguma letra aparece, sendo possível colocar fatiamento após as aspas
print (frase.count('o', 15 ,31)) 
# frase.find('ngo') vai dizer em qual número se encontra o que foi pedido
print (frase.find('ngo'))
# 'Macarrçao' in frase irá dizer se existe tal caracteres na str
print ('Macarrão' in frase)
# frase.replace('macarrão', 'pizza') irá subistitur as str
print (frase.replace('Macarrão','pizza'))
# frase.upper() irá deixar maiúsculo
print (frase.upper())
# frase.lower() irá deixar minúsculo
print (frase.lower())
# frase.capitalize() irá deixar minúsculo toda a frase e primeira letra maiúscula
print (frase.capitalize())
# frase.title() íra deixar a primeira letra de cada frase maiúscula e o resto minúsculo
print (frase.title())
# frase1.strip() íra remover os espaços inúteis antes do começo da frase e ao final da frase
print (frase1.strip())
# frase1.rstrip() íra remover os espaços inúteis da direita da frase
print (frase1.rstrip())
# frase1.lstrip() íra remover os espaços inúteis da esquerda da frase
print (frase1.lstrip())
# frase.split() irá colocar cada palavra dentro de uma outra lista, zerando a contagem a cada palavra e cada palavra recebendo o número de sua "splitagem"
print (frase.split())
# '-'.join(frase) íra juntar tudo denovo substituindo os espaços pelo "-"
print('-'.join(frase.split()))
# colocando """ no fim e no começo de uma string, pode ser fazer um texto continuo em linhas
print ("""O macarrão é conhecido principalmente por ser uma fonte rica em carboidratos.
Mas como os carboidratos agem no nosso corpo?Em termos simples, os carboidratos
são convertidos em glicose, que é usada pelo corpo como fonte de energia.""")


 

# frase = 'Curso em vídeo Python'
# print(frase[9:13])