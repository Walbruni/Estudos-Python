
# inserção em lista de alocacao contigua

# insercao por meio da funcao append()
nomes = ['Joao', 'Maria', 'Ana']
nomes.append('Arthur')  # insere um novo nó no final da lista contendo Arthur
print(nomes)


# criando uma funcao para insercao por conta propria (ao final da lista)

def insereL(k, L, n):
    L.append('')  # aumente um indice na lista
    L[n] = k  # indices na lista iniciam em 0
    n = n + 1  # incrementa o numero nós n


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
insereL(12, numeros, len(numeros))
print(numeros)


# Caso a sua lista seja ordenada é necessario buscar a posição correta para inserir o novo nó.
# Todos os nós posteriores terão que ser “empurrados” uma posição à frente, para abrir espaço.
# Caso a chave buscada já exista na lista, não poderemos inserir o nó, o que deve gerar um erro.

# criando uma funcao para a insercao em lista ja ordenada

def insereOrdenada(k, L, n):
    i = 0
    posInsercao = - 1
    while (i < n):
        if L[i] >= k:
            if L[i] == k:
                return -1  # erro, chave ja existe
            else:
                posInsercao = i  # posicao achada
                i = n + 1  # sair do laço
        else:
            i = i + 1  # continuar no laço
        if i == n:
            posInsercao = n  # insercao no final da lista
# ate esse trecho de codigo acima, serve para buscar a posicao correta para a insercao

# a partir daqui, serve para inserir na posicao correta
    L.append('')
    i = n  # inicio do ajuste da lista
    while (i > posInsercao):
        L[i] = L[i - 1]  # empurra cada nó para o final da lista
        i = i - 1

    L[posInsercao] = k  # insere novo nó
    return posInsercao  # saída normal da função


numeros = [1, 2, 3, 4, 6, 7, 8, 9, 10]
insereOrdenada(5, numeros, len(numeros))
print(numeros)


# COMPLEXIDADE
# Imagine que você tenha uma lista linear com milhões de entradas. Se você faz buscas muito frequentes, mas raramente inserções, pode valer a pena mantê-la ordenada, pois as buscas infrutíferas são resolvidas com muito mais rapidez.
# Entretanto, as inserções têm custo linear. Se você faz muitas inserções na lista, o custo constante da lista não ordenada pode ser muito mais interessante, e não haveria motivo para mantê-la ordenada.
