class bicicleta:
    def __init__(self, cor, modelo, ano, valor ):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor
        
    def buzinar(self):
           print('BI BIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
             
             
    def parar(self):
        print('FREIANDO>>>\nBicileta parada')
        
        
    def correr(self):
        print('VRUM VRUM VRUMMMMMMMMMMMMM')
            
'''        
bi1 = bicicleta('vermelha', 'caloi', 2022, 600)

bi1.buzinar()
bi1.parar()
bi1.correr()
print(bi1.cor)'''

bi2 = bicicleta('verde', 'renner', 2024, 4.500)

bicicleta.correr(bi2)#bi2.correr()
  