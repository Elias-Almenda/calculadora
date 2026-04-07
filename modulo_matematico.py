
def somar(n1, n2):
    
   return n1 + n2

def multiplicar(n1, n2):
    
    return n1 * n2
    
def subtrair(n1, n2):
    
    return n1 - n2

def divisao(n1, n2):
    if n2 == 0:
        print('Não é possivel dividir por 0')
    return n1 / n2

def potencial(n1, n2):
    
    return n1 ** n2

def raiz(numero: float, indice: int = 2) -> float:
    if indice == 0:
        raise ValueError("O índice não pode ser zero")
    
    if numero < 0 and indice % 2 == 0:
        raise ValueError("Não existe raiz real para esse caso")
    
    return numero ** (1 / indice)
    
