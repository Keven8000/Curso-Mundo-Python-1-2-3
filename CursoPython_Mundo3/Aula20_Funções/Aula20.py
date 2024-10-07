def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('SISTEMA DE ALUNOS')

def soma(a, b):
    print(f'A = {a} + B = {b} = ', end='')
    s = a + b
    print(s)


soma(8, 6)
soma(0, 5)
soma(b = 3, a = 9)
    

'''EMPACATADOR''' 
def contador(* number):
    print(number)
    

contador(2, 3, 5)
contador(5, 6)
contador(4, 9, 6, 4, 9)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1


valores = [1, 6, 5, 9]
dobra(valores)
print(valores)