def área(base, altura):
    area = base * altura
    print(f'A base mede {base}m e tem {altura}m de comprimento, então sua área é de {area}m°')


a = float(input('Digite o comprimento em metros: '))
b = float(input('Digite a base em metros: '))
área(b, a)