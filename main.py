# node = config do tabuleiro
class Node():
    def __init__(self, config):
        self.config = config
        '''
            config -> string composta apenas por valores inteiros e um '*'.
            Cada índice da string representa uma posição do tabuleiro, que pode estar 
            ocupada por um número ou por '*', que representa vazio  
        '''
        
# a has table eh um dict:
# hash = {
#     'chaveHash': config
# }


def calculaQuadrantesAdj(posicao):
    '''
        Função que, dado um quadrante do tabuleiro, retorna todos os quadrantes adjacentes ao mesmo dentro do vetor de config.
    ''' 
    quadrante = posicao + 1
    match (quadrante):
        case 1: return 1, 3
        case 2: return 0, 4, 2
        case 3: return 1, 5
        case 4: return 0, 4, 6
        case 5: return 1, 3, 5, 7
        case 6: return 2, 4, 8
        case 7: return 3, 7
        case 8: return 6, 4, 8
        case 9: return 5, 7
        case _: return None


def calculaHash(config):
    mod = (10**9) + 9
    sum = 0
    p = 11
    for i in range(len(config)-1):
        sum += config[i] * (p ** i)
        
    return sum % mod


def criaGrafoEstados(configInicial) -> dict:
    ...


configInicial = Node("12345678*")