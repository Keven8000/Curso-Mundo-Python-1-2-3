#__init__ = método construtor // sempre executado quando uma nova instância de classe é criada
'''EX:
class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
'''
#__del__ = método destrutor // executado quando uma instância(objeto) é destruída, menos usado
# em pytho, pois ele tem um coletor lixo que lida com o gerenciamento de memória automaticamente.
'''EX:
class cachorro:
    def __del__(self);
    print('Destruindo a instâncoa')
    
c = cachorro
del c
'''

class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('INICIANDO A CLASSE')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        

    def __del__(self):
        print('Removendo instância')
    
    
    def latir(self):
        print('AuAu')
        
        
    def dormir(self):
        self.acordado = False
        print('Zzzz...')
        

cao_1 = cachorro('fofito', 'preto', False)
cao_2 = cachorro('Maicon', 'Branco')

        