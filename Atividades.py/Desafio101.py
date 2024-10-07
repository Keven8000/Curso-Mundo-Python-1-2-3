def voto():
    from datetime import date
    global idade

    idade =  date.today().year - nascimento 
    if idade > 15 and idade < 18 or idade > 65:
        votacao = 'Voto opcional'
    elif idade < 16:
        votacao = 'Voto proibido'
    else: 
        votacao = 'Obrigatoria'
    return votacao


nascimento = int(input('Digite sua idade de nascimento: '))
print(f'A votação do cidadão é {voto()}, pois o cidadão tem {idade} anos')
