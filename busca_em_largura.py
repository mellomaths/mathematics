def jogo_fichas(posicao_inicial):
    fila = []
    largura = {}
    l = 1
    pai = {}
    nivel = {}
    aresta = {}

    fila.append(posicao_inicial)
    largura[posicao_inicial] = l
    pai[posicao_inicial] = None
    nivel[posicao_inicial] = 1

    grafo = {
        posicao_inicial: []
    }

    while len(fila):
        vertice = fila.pop(0)

        casa_vazia = vertice.index('i')
        destino = casa_vazia + 1
        if (destino < len(vertice)):
            posicao_list = list(vertice)
            temp = posicao_list[destino]
            posicao_list[destino] = 'i'
            posicao_list[casa_vazia] = temp
            posicao_final = "".join(posicao_list)
            grafo[vertice].append(posicao_final)
            if (not grafo.get(posicao_final)):
                grafo[posicao_final] = []

        destino = casa_vazia + 2
        if (destino < len(vertice)):
            posicao_list = list(vertice)
            temp = posicao_list[destino]
            posicao_list[destino] = 'i'
            posicao_list[casa_vazia] = temp
            posicao_final = "".join(posicao_list)
            grafo[vertice].append(posicao_final)
            if (not grafo.get(posicao_final)):
                grafo[posicao_final] = []

        destino = casa_vazia - 1
        if (destino > -1):
            posicao_list = list(vertice)
            temp = posicao_list[destino]
            posicao_list[destino] = 'i'
            posicao_list[casa_vazia] = temp
            posicao_final = "".join(posicao_list)
            grafo[vertice].append(posicao_final)
            if (not grafo.get(posicao_final)):
                grafo[posicao_final] = []

        destino = casa_vazia - 2
        if (destino > -1):
            posicao_list = list(vertice)
            temp = posicao_list[destino]
            posicao_list[destino] = 'i'
            posicao_list[casa_vazia] = temp
            posicao_final = "".join(posicao_list)
            grafo[vertice].append(posicao_final)
            if (not grafo.get(posicao_final)):
                grafo[posicao_final] = []

        for vizinho in grafo.get(vertice):
            if not largura.get(vizinho):
                fila.append(vizinho)
                l += 1
                largura[vizinho] = l
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1

        if pai[vizinho] == vertice or pai[vertice] == vizinho:
            aresta[(vertice, vizinho)] = 'aresta de arvore'
        elif nivel[vertice] == nivel[vizinho]:
            if pai[vertice] == pai[vizinho]:
                aresta[(vertice, vizinho)] = 'aresta irma'
            else:
                aresta[(vertice, vizinho)] = 'aresta primo'
        else:
            if nivel[vertice] < nivel[vizinho]:
                aresta[(vertice, vizinho)] = 'aresta tia'
            else:
                aresta[(vertice, vizinho)] = 'aresta sobrinha'
    
    return largura, pai, aresta, nivel



largura, pai, aresta, nivel = jogo_fichas('bbipp')
print(largura)
print()
print(pai)
print()
print(aresta)
print()
print(nivel)