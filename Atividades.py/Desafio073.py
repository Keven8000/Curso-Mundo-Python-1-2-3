print('-=-'*12, 'TABELA BRASILEIRÃO 2023', '-=-'*12)

classificao = "Palmeiras", "Botafogo", "Fluminense", "Atlético Mineiro", "Internacional", "Flamengo", "São Paulo", "Athletico Paranaense", "Corinthians", "Grêmio", "Bragantino", "Fortaleza", "Santos", "Vasco da Gama", "Cuiabá", "Goiás", "Bahia", "Atlético Goianiense", "Coritiba", "América Mineiro" 
time = (input('Digite o nome do time que você quer saber a posição: ')).upper().strip()
c = posicao = 0


while True:
    
    if time == classificao[c].upper():
        print (f'posição {c+1}°')
        posicao = c+1
        c += 21
    else:
        c += 1
    if c > 20:
        break
 
print(f'Os 5 primeiros colocados foram {classificao[:5]} e os 4 últimos foram {classificao[16:]}')

print(f'Assim fica em ordem álfabetica  {sorted(classificao)}')

print (f'O {time.lower()} está na posição {posicao}°')