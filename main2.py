from itertools import permutations
from collections import deque


def calculaChaveHash(config):
    return str(hash(config))


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
    '''
        Para cada permutação possivel do tabuleiro:
            1. Adiciona ela no grafo;
            2. Calcula seus vizinhos e adiciona na lista de adjacências;
            3. Aumenta o número de arestas;
    '''
    numArestas = 0
    grafo = {}
    for perm in permutacoes:
        vizinhos = calculaConfigsAdj(perm)
        grafo[perm] = vizinhos
        numArestas += len(vizinhos) / 2
        
    return grafo, int(numArestas)


def BFS(grafo):
    visitados = set()
    numComponentes = 0
    for no in grafo:
        if no not in visitados:
            BFSVisit(grafo, no, visitados)
            numComponentes += 1
    return numComponentes


def BFSVisit(grafo, origem, visitados):
    camadas = deque([origem])
    while camadas:
        inicio = camadas.popleft()
        for vizinho in grafo[inicio]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                camadas.append(vizinho)


configInicial = "12345678*"
permutacoes = ["".join(perm) for perm in permutations(configInicial)]
numeroNos = len(permutacoes)
grafo, numeroArestas = criaGrafoEstados(permutacoes)
print("Numero de nos: \t\t",numeroNos)
print("Numero de arestas: \t",numeroArestas)
print("Componentes conexos: ", BFS(grafo))