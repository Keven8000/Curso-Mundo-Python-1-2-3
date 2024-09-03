numeros_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero_usuario = int(input('Digite um número entre 0 e 20: '))
if numero_usuario >= 0 and numero_usuario < 21:
    print (numeros_extensos[numero_usuario])
else: 
    print('O número digitado não está entre 0 e 20, tente novamente. ')