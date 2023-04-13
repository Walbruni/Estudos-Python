
# Exemplo de algoritmo de agrupamento são k-means (k-medias) e mean-shift
# O objetivo de um algoritmo de agrupamento é reunir objetos de uma coleção que mantenham algum grau de afinidade.
# É utilizada uma função para maximizar a similaridade de objetos do mesmo grupo e minimizar entre elementos de outros grupos.

# Utilizaremos o algoritmo k-medias para gerar grupos a partir do dataset de Flor de Íris.
# Porém, como o agrupamento é um algoritmo não supervisionado, não utilizaremos os rótulos para treiná-lo. O algoritmo vai automaticamente separar as amostras em grupos, que serão visualizados em um gráfico.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


################## Pré-processamento ###################
# Coleta e Integração
iris = load_iris()

caracteristicas = iris.data

################### Mineração #####################
grupos = KMeans(n_clusters=3)
grupos.fit(X=caracteristicas)
labels = grupos.labels_  # indice do grupo ao qual cada amostra pertence

################ Pós-processamento ####################
fig = plt.figure(1)
ax = Axes3D(fig)
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(caracteristicas[:, 0], caracteristicas[:, 1],
           caracteristicas[:, 2], c=grupos.labels_, edgecolor='k', )

target = iris.target
fig = plt.figure(2)
ax = Axes3D(fig)
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(caracteristicas[:, 0], caracteristicas[:, 1],
           caracteristicas[:, 2], c=target, edgecolor='k')

plt.show()


# Na etapa de mineração de dados, treinaremos o algoritmo de agrupamento K-medias com as características das flores.
# Para isso, criamos uma instância da classe KMeans passando como parâmetro o número de grupos (ou classes) que desejamos que o algoritmo identifique (n_clusters)
# Passamos o número 3, pois sabemos que são 3 classes de flor, mas poderíamos alterar esse valor.
# O objeto grupos criado será utilizado para treinar (ajustar) o algoritmo.
# Para realizar o treinamento (fit), precisamos passar apenas parâmetros X, que conterão as características das flores.

# Após o treino, podemos utilizar o atributo labels_ do objeto grupos para retornar uma lista com o índice do grupo ao qual cada amostra pertence.
# Como o número de grupos (n_clusters) é 3, o índice varia entre: 0, 1 e 2.

# Na etapa de pós-processamento utilizamos a biblioteca Matplotlib para exibir dois gráficos, onde objetos do mesmo grupo apresentam a mesma cor.
