# Serve para quando não souber quantas repetições serão necessárias 
# enquanto não x coisa (enquanto a condição for verdadeira, continuára a rodas):
#   passo
# pega
# while not x coisa (enquanto a condição for verdadeira, continuára a rodas):
#   passo
# pega
'''for c in range(1, 10):
    print (c)
print ('fim')    '''

'''c = 1
while c < 10:
    print(c)
    c += 1 
print('FIM')'''

valor = 1
print('Para parar digite 0.')
while valor != 0:
    valor = int(input('Digite um valor: '))
 