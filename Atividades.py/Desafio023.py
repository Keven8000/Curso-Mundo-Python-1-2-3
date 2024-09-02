number = ((input('escolha um número entre 0 e 9999: ')))
numberr = int(number)
if numberr>999:
    print ("Unidade: {}".format(number[3]))
else:
    print ("Unidade: 0")
if numberr>99:
    print ("Dezena: {}".format(number[2]))
else: 
    print ("Dezena: 0")
if numberr>9:
    print ("Centena: {}".format(number[1]))
else: 
     print ("Centena: 0")
print ("Milhar: {}".format(number[0]))