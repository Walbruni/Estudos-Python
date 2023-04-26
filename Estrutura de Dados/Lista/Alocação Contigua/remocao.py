
# remoção em lista de alocacao contigua

# remocao por meio da funcao remove()
nomes = ['Joao', 'Maria', 'Ana', 'Arthur']
nomes.remove('Arthur')  # remove atraves do valor
print(nomes)

# remocao por meio da funcao pop()
nomes.pop(2)  # remove atraves do indice
print(nomes)


# criando uma funcao para a remocao

def removeL(k, L, n):  # uma lista L com n nós e quer remover um nó de chave k
    i = 0  # inicio da busca do nó
    posRemocao = -1
    while (i < n):
        if L[i] == k:
            posRemocao = i  # chave encontrada
            i = n + 1  # sair do laço
        else:
            i = i + 1  # continuar busca
    if i == n:
        return -1  # erro, chave nao existe
# o trecho de codigo acima serve para buscar a chave a ser removida

    i = posRemocao  # inicio do ajuste da lista
    while (i < n - 1):  # esse laço serve para fechar o 'buraco' gerado pela remocao do elemento. Em alocao contigua nao pode existir esses buracos
        L[i] = L[i + 1]  # puxa cada nó posterior uma posição
        i = i + 1

    L.pop(n - 1)  # ajusta o tamanho da lista
    return posRemocao  # saída normal da função


nomes = ['Joao', 'Maria', 'Ana', 'Arthur']
i = removeL('Maria', nomes, len(nomes))
print(nomes)


# caso seja uma lista ordenada, pode-se melhorar o processo de busca permitindo que o erro de chave não encontrada seja detectado logo após ser vista uma chave maior que k:

def removeOrdenada(k, L, n):
    i = 0
    posRemocao = -1
    while (i < n):
        if L[i] == k:
            posRemocao = i  # chave encontrada
            i = n + 1  # sair do laço
        else:
            if L[i] > k:
                return -1  # erro, chave nao existe
            i = i + 1

        i = posRemocao
        while (i < n - 1):
            L[i] = L[i + 1]
            i = i + 1

        L.pop(n - 1)
        return posRemocao


nome = ['Carlos', 'Lucas', 'Jose']
i = removeOrdenada('Carlos', nome, len(nome))
print(nome)


# COMPLEXIDADE
# Apenas no caso de remoção infrutífera (o nó buscado não existe na lista) a pequena alteração para a lista ordenada terá uma complexidade melhor, pois você interrompe a busca assim que descobre uma chave maior que a do nó buscado.
