
# lista em alocação contigua

# Como a alocação contígua reserva um espaço sequencial de memória para armazenar uma lista, os seus elementos estarão sempre sequencialmente em memória, ordenados ou não.

# exemplo lista nao ordenada
compras = [[15, 'laranja', 3], [2, 'palmito', 20], [35, 'feijao', 5]]

# exemplo visual da lista:

# ProdutoID    NomeProduto    Preco
#     15        Laranja        3,00
#     2         Palmito       20,00
#     35        Feijao         5,00

# BUSCA percorre a lista sequencialmente - O(n) - complexidade linear (inicia sempre no indice zero e no pior caso vai ate o final da lista)

# INSERCAO pode ser feita sempre ao final - O(1) - complexidade constante (sempre tera uma variavel apontando ao ultimo elemento da lista)

# REMOCAO depende da BUSCA - O(n) - complexidade linear


# exemplo lista ordenada
compras = [[2, 'palmito', 20], [15, 'laranja', 3], [35, 'feijao', 5]]

# exemplo visual da lista:

# ProdutoID    NomeProduto    Preco
#     2         Palmito       20,00
#     15        Laranja        3,00
#     35        Feijao         5,00

# BUSCA percorre a lista sequencialmente - O(n) - complexidade linear

# INSERCAO deve manter a ordenacao - O(n) - complexidade linear (o elemento sera inserido de forma que fique tudo ordenado, com os demais elementos sendo 'afastados')

# REMOCAO depende da BUSCA - O(n) - complexidade linear (o elemento sera removido de forma que fique tudo ordenado, com os demais elementos sendo 'puxados' para preencher o espaço vazio na memoria)
