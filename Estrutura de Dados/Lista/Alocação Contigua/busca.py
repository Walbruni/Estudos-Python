
# busca em lista de alocacao contigua

# busca por meio da funcao index()
nomes = ['Joao', 'Maria', 'Ana']
i = nomes.index('Joao')
print(i)


# criando uma funcao para a busca

# percorrer a lista buscando se a chave 'k' corresponde a algum nó da lista
def buscaLista(k, L, n):  # a lista esta armazenada em 'L' e 'n' é o maximo de elementos da lista
    i = 0
    indiceL = -1
    while i < n:
        if L[i] == k:  # nó encontrado
            indiceL = i  # salve o indice
            i = n + 1  # sair do laço
        i = i + 1  # segue a busca
    return indiceL  # caso ocorra algum erro, retornara -1


nomes = ['Arthur', 'Joao', 'Maria', 'Ana']
i = buscaLista('Ana', nomes, len(nomes))
print(i)


# funcao para a busca, no caso da lista L estar ordenada por chave (em ordem crescente)

def buscaOrdenada(k, L, n):
    i = 0
    indiceL = - 1
    while (i < n):
        if L[i] >= k:
            if L[i] == k:
                indiceL = i  # chave encontrada
                i = n + 1  # sair do laço
            else:
                i = n + 1  # chave maior que k, sair do laço
        else:
            i = i + 1  # continuar busca

    return indiceL  # o retorno -1 indica chave nao encontra


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = buscaOrdenada(5, numeros, len(numeros))
print(i)

# exemplo de situacao para chave nao encontrada
i = buscaOrdenada(11, numeros, len(numeros))
print(i)


# COMPLEXIDADE
# No caso da lista ordenada, a busca é mais eficiente em descobrir quando o elemento buscado não está na lista. Nesse caso, a busca para qualquer chave maior que a chave buscada é vista.
# Ao contrário, na lista não ordenada, você sempre tem que percorrer toda a lista para dizer que uma chave não está nela.
