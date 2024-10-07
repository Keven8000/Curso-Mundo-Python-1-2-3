def hel(ajuda):
    help(ajuda)
    
função = str(input('Digite a função ou biblioteca ou 0 para parar: ' )).strip()
if função == '0':
    print('PROGRAMA ENCERRADO')
else:
    hel(função)
