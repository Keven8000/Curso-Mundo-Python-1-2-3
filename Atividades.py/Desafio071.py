saque = int(input('Digite quanto você quer sacar: '))
total = saque
ced = 50
total_ced= 0 

while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        print(f'Total de {total_ced} céduças de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break