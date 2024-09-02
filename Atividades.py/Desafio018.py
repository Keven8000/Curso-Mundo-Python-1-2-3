import math
print ('-'*12, 'Leitor de ângulos', '-'*12)
an = float(input('Digite seu ângulo: '))
se = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print ('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(se,cos,tan))