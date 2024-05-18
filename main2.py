from itertools import permutations

def calculaQuadrantesAdj(posicao):
    '''
        Funcao que, dado um quadrante do tabuleiro, retorna todos os quadrantes adjacentes 
        ao mesmo dentro do vetor de config.
    ''' 
    quadrante = posicao + 1 # => o quadrante do tabuleiro eh a posicao do vetor + 1
    match (quadrante):
        case 1: return [1, 3]
        case 2: return [0, 4, 2]
        case 3: return [1, 5]
        case 4: return [0, 4, 6]
        case 5: return [1, 3, 5, 7]
        case 6: return [2, 4, 8]
        case 7: return [3, 7]
        case 8: return [6, 4, 8]
        case 9: return [5, 7]
        case _: return None


def calculaConfigsAdj(config):
    '''
        Funcao que retorna uma lista de configuracoes adjacentes a uma configuracao dada.
    '''
    lista_adjacentes = list()
    # Calcula os quadrantes adjacentes ao vazio:
    lista_quadrantes = calculaQuadrantesAdj(config.index('*'))
    # Para cada quadrante adjacente, cria uma config nova o trocando de lugar com o *:
    index = config.index('*')
    for quadrante in lista_quadrantes:
        aux = list(config)
        # Troca as pecas de lugar:
        aux[quadrante], aux[index] = aux[index], aux[quadrante]
        config_adj = "".join(aux)
        # Depois de muitas manipulacoes, adiciona a nova config na lista de configs adjs:
        lista_adjacentes.append(config_adj)
    # Retorna a lista de configs adjacentes:
    return lista_adjacentes


def criaGrafoEstados(permutacoes):
    numArestas = 0
    grafo = {}
    '''
        Para cada permutação
            1. Adiciona ela no grafo
            2. Calcula seus vizinhos e adiciona na lista de adjacências
            3. Aumenta o número de arestas
    '''
    for perm in permutacoes:
        # Calcula os vizinhos desta permutação:
        vizinhos = calculaConfigsAdj(perm)
        # Adiciona 
        grafo[perm] = vizinhos
        numArestas += len(vizinhos)/2
    return grafo, int(numArestas)


configInicial = "12345678*"
permutacoes = list(permutations(configInicial))
numeroNos = len(permutacoes)
grafo, numeroArestas = criaGrafoEstados(permutacoes)
print("Numero de nos: \t\t",numeroNos)
print("Numero de arestas: \t",numeroArestas)