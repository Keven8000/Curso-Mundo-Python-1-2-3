class animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join ([f'{chave}={valor}' for chave, valor in 
        self.__dict__.items()])}'
        


class mamifero(animal):
    def __init__(self, num_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(num_patas)

class ave(animal):
    def __init__(self, num_patas):
        super().__init__(num_patas)
    

class cachorro(mamifero):
    pass


class gato(mamifero):
    pass


class leão(mamifero):
    pass


class urubu(ave):
    pass


miau = gato(4, 'branco')
print(miau)