
def calculaQuadrantesAdj(posicao):
    '''
        Funcao que, dado um quadrante do tabuleiro, retorna todos os quadrantes adjacentes 
        ao mesmo dentro do vetor de config.
    ''' 
    quadrante = posicao + 1 #=>o quadrante do tabuleiro eh a posicao do vetor + 1
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
    lista_adjacentes = list()
    lista_quadrantes = calculaQuadrantesAdj(config.index('*'))
    for quadrante  in lista_quadrantes:
        index = config.index('*')
        aux = list(config)
        aux[quadrante], aux[index] = aux[index], aux[quadrante]
        config_adj = "".join(aux)
        lista_adjacentes.append(config_adj)
    print("Config original: ",config)
    print("Configs adjacentes: ",lista_adjacentes)
    ...


def calculaChaveHash(config) -> str:
    '''
        Funcao que retorna a chave hash para uma configuracao.
    '''
    return str(hash(config))


def incluiNoGrafoEstado(config, hashtable, grafo):
    '''
    	1. Calcula chave hash para a nova configuracao
        2. Verifica se no ja existe no grafo por meio de sua chave
            2.1. Se nao existe, o adicionamos na hash table
    '''
    chave_hash = calculaChaveHash(config)
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
                3.1.1. Se nao existe, adiciona-o no grafo
                3.1.2. Chama a funcao recursivamente para este no?????????????????
    '''
    posicao_vazia = config_inicial.index('*')
    casas_adjacentes = calculaQuadrantesAdj(posicao_vazia)
    for casa in casas_adjacentes:
        # cria nó movendo quem está na casa adjacente para o vazio
        # verifica se este novo nó existe no grafo
        ...

configInicial = "1234567*8"
calculaConfigsAdj(configInicial)