
# Listas especiais que podem ser iteradas infinitamente
# Geralmente encadeada
# É preciso garantir a condição circular a cada inserção no final ou remoção no início ou final

# inserção (caso encadeado)
def insereCircular(novoNo):
    if inicioLista == None:  # caso a lista esteja vazia, cria uma lista circular com apenas um nó
        inicioLista = novoNo
        finalLista = novoNo
        novoNo.proximo = novoNo

    else:  # tratamento de caso normal
        finalLista.proximo = novoNo  # insere o nó
        finalLista = novoNo
        finalLista.proximo = inicioLista  # atualiza ponteiros

# complexidade constante O(1)
# caso a lista seja ordenada, a complexidade é linear O(n), pois depende da busca pela posição correta a ser inserido


# A remoção em lista circular funciona de forma semelhante à lista linear
# precisando apenas atualizar os ponteiros de início e final da lista, caso um dos extremos seja removido

# remoção
def removeCircular(k):
    noAnterior = buscarAnterior(k)  # busca pelo nó anterior para remove-lo

    if noAnterior == None:  # caso o nó anterior nao seja encontrado
        return None

    if finalLista == inicioLista:  # lista com um unico nó
        lista = None  # remove o nó
        return 0  # lista vazia

    if noAnterior == finalLista:  # remover o nó inicial da lista
        finalLista.proximo = inicioLista.proximo
        inicioLista = finalLista.proximo  # mantendo a circularidade da lista

    elif noAnterior.proximo == finalLista:  # remover o nó final da lista
        finalLista = noAnterior
        noAnterior.proximo = inicioLista  # mantendo a circularidade da lista

    else:  # remoção de um nó que não está nas pontas
        noAtual = noAnterior.proximo
        noAnterior.proximo = noAtual.proximo
    return 0  # saida normal

# complexidade linear O(n), pois envolve a busca pela posição correta
