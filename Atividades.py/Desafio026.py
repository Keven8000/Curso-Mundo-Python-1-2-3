fra = input ('Escreva sua frase : ').strip().upper()
frase = ''.join(fra.split())
letra = input ('Digite qual letra quer achar: ').upper()
print ('Quantas vezes aparece: ', frase.count(letra))
print ('Qual sua primeira aparição:', frase.find(letra)+1)
# rfind de right = direita
print ('Qual sua última aparição: ', fra.rfind(letra)+1)
print ('Quantos caracteres tem: ', len(frase))