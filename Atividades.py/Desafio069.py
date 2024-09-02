homem = mulher = maior = 0

while True:
    ida = int(input('Digite a idade: '))
    sexo = int(input('[1] Homem\n[2] Mulher\n'))
    if sexo == 1: 
        homem += 1 
    if sexo == 2:
        mulher += 1
    if ida == 18 or ida > 18:
        maior += 1
    cont = int(input('[1] Continuar\n[2] Encerrar progama\n'))
    if cont == 2:
        break

print(f'Tem {homem} homens,{mulher} mulheres e {maior} são de maiores')