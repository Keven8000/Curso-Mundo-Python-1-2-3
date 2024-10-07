def escreva(texto):
    linhas = len(texto) + 4
    print('~' * linhas )
    print(' ', texto)
    print('~' * linhas )


mensagem = str(input('Digite o texto que você quer que apareça: '))
escreva(mensagem)