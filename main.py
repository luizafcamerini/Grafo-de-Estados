# node = config do tabuleiro
class Node():
    def __init__(self, config):
        self.config = config
        '''
            config -> string composta apenas por valores inteiros e um '*'.
            Cada índice da string representa uma posição do tabuleiro, que pode estar 
            ocupada por um número ou por '*', que representa vazio  
        '''
        

def calculaQuadrantesAdj(posicao):
    '''
        Função que, dado um quadrante do tabuleiro, retorna todos os quadrantes adjacentes 
        ao mesmo dentro do vetor de config.
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


def calculaConfigsAdj(config) -> list:
    lista_adjacentes = list()
    ...


def calculaChaveHash(config):
    return str(hash(config))


def incluiNoGrafoEstado(config, hashtable, grafo):
    '''
    	1. Calcula chave hash para a nova configuração
        2. Verifica se nó já existe no grafo por meio de sua chave
            2.1. Se não existe, adicionamos-o na hash table
    '''
    node = Node(config)
    chave_hash = calculaChaveHash(node.config)
    if chave_hash not in hashtable.keys:
        # Inclui na hashtable:
        hashtable[chave_hash] = list()
        hashtable[chave_hash] += config
        
        # Inclui no grafo de adjacencia
        grafo[config] = list()
        configuracoes_adjacentes = calculaConfigsAdj(config)
        grafo[config] += configuracoes_adjacentes
        
        for config_adjacente in configuracoes_adjacentes:
            grafo[config_adjacente].append(config)

    # Retorna o grafo e hashtable atualizados:
    return hashtable, grafo


def criaGrafoEstados(config_inicial):
    '''
        1. Verifica quem são as posições adjacentes à posição vazia ('*')
        2. Formar novos nós
        3. Para cada nó
            3.1. Verifica se já existe no grafo por meio da função de hash
                3.1.1. Se não existe, adiciona-o no grafo
                3.1.2. Chama a função recursivamente para este nó?????????????????
    '''
    posicao_vazia = config_inicial.index('*')
    casas_adjacentes = calculaQuadrantesAdj(posicao_vazia)
    for casa in casas_adjacentes:
        # cria nó movendo quem está na casa adjacente para o vazio
        # verifica se este novo nó existe no grafo
        ...

configInicial = Node("12345678*")