
# arrays utilizando a biblioteca numpy
# so permite a utilizacao de elementos do mesmo tipo (int, str ou float, por exemplo)

# importacao da biblioteca numpy
import numpy as np

nomes = np.array(['Joao', 'Maria', 'Ana'])
print(nomes)

# para acessar um elemento usando o indice
print(nomes[0])

# tambem é possivel acessar os elementos de tras para frente
print(nomes[-1])

# para verificar qual o tipo do array
print(nomes.dtype)

# assinalando um tipo especifico para o array
arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr.dtype)

# criando uma copia (qualquer alteracao feita na copia nao altera os valores do array original)
copia = nomes.copy()
copia[0] = 'Lucas'
print(nomes)
print(copia)

# criando uma visao (qualquer alteracao feita altera os valores do array original)
visao = nomes.view()
visao[0] = 'Lucas'
print(nomes)
print(visao)

# iterando sobre o array
for x in nomes:
    print(nomes)

# criando uma lista duplicada que tera o indice e o valor
for indice, valor in enumerate(nomes):
    print(indice, valor)
