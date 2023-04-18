
# utilizando a biblioteca numpy
import numpy as np

# declaracao da matriz numeros
# Importante: todos os elementos da biblioteca numpy precisam ter o mesmo tamanho (array de array: matriz)
numeros = np.array([[4, 13, 16], [5, 7, 1], [8, 10, 15]])
print(numeros)

# permite realizar operacoes simples com matrizes que tenham o mesmo tamanho de forma direta
matriz1 = np.array([[1, 2], [3, 4], [5, 6]])
matriz2 = np.array([[7, 8], [9, 10], [11, 12]])

matriz2 = matriz1 + matriz2
print(matriz2)

matriz2 = matriz2 - matriz1
print(matriz2)

# alguns metodos
minimo = numeros.min()

maximo = numeros.max()

soma = numeros.sum()

media = numeros.mean()

desvio = numeros.std()  # desvio padrao

print('Minimo: ', minimo)
print('Maximo: ', maximo)
print('Soma: ', soma)
print('Media: ', media)
print('Desvio: ', desvio)

# permite utilizar a funcao enumerate() para separar os indices e os valores da matriz

# exemplo 1
# A diagonal principal de uma matriz é o conjunto de elementos cujo índice de coluna é igual ao índice da linha.
# Assumindo que temos uma matriz quadrada salva como array na variável matriz, o código que imprime corretamente os elementos da diagonal principal é:

for indice in enumerate(matriz1):
    print(matriz1[1][1])  # (matriz[indice][indice])


# selecionar atraves do indice
# exemplo 2
# Um array de 3 dimensões foi declarado com a linha:

matriz = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11], [12, 13]], [[14, 15]]]

# Para imprimir o valor de 10, o código correto é:

print(matriz[1][0][0])

# O primeiro índice seleciona, na primeira dimensão matriz[1], o conjunto de 2 elementos ([10,11] e [12,13]).
# Na segunda dimensão, você escolhe entre esses elementos. Matriz[1][0] seleciona o par (10,11).
# Por fim, o terceiro índice seleciona entre esses dois. Matriz[1][0[0] seleciona o valor 10.
