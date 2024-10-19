class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas  
        
        
    
    def ligar_motor(self):
        print('Ligando o motor')
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join ([f'{chave}={valor}' for chave, valor in 
        self.__dict__.items()])}'
        
    

class motocileta(veiculo):
    '''def empinando(self):
        print('DARAMMMMM')'''
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    pass


moto = motocileta('azul', 'x9', 2)
moto.ligar_motor()
print(moto)