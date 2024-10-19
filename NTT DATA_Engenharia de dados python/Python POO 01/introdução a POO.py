'''
Classe e objetos: Uma classe define as carcterísticas e comportamentos de um objeto, 
porém não se pode usar elas diretamente. Os objetos podem ser usados e possuem as 
carcterísticas e comportamentos que foram definidos na classe.

'''

class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    
    def latir(self):
        print('AuAu')
        
    def dormir(self):
        self.acordado = False
        print('Zzzz...')
        

cao_1 = cachorro('fofito', 'preto', False)
cao_2 = cachorro('Maicon', 'Branco')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir
print(cao_2.acordado)