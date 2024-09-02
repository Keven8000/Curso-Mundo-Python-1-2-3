while True:
    number_texto = str(input('Digite o número que você quer a tabuada: '))
    if '-' in number_texto:
        break
    number = int(number_texto)
    for c in range(1,11):
        tabu = c * number
        print(f'{c} x {number} = {tabu}')