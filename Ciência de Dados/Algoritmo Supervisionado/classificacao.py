
# Os algoritmos de classificação são do tipo supervisionado, nos quais passamos um conjunto de características sobre um determinado item de uma classe de forma que o algoritmo consiga compreender, utilizando apenas as características, qual a classe de um item não mapeado.
# Vamos treinar dois algoritmos de classificação, árvore de decisão e máquina de vetor suporte (support vector machine – SVM) para montar dois classificadores de flores de Íris.

from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC

### Pré-Processamento ###
# Coleta e Integração
iris = load_iris()

caracteristicas = iris.data
rotulos = iris.target

print('Características:\n', caracteristicas[:2])
print('Rótulos:\n', rotulos[:2])
print('############################')

# Partição de Dados
carac_treino, carac_teste, rot_treino, rot_teste = train_test_split(
    caracteristicas, rotulos)

### Mineração ###
# Arvore de Decisão #
arvore = DecisionTreeClassifier(max_depth=2)
arvore.fit(X=carac_treino, y=rot_treino)

rot_preditos = arvore.predict(carac_teste)
acuracia_avore = accuracy_score(rot_teste, rot_preditos)

# Maquina de Vetor Suporte #
clf = SVC()
clf.fit(X=carac_treino, y=rot_treino)

rot_preditos_svm = clf.predict(carac_teste)
acuracia_svm = accuracy_score(rot_teste, rot_preditos_svm)

### Pós-Processamento ###
print('Acurácia Ávore de Decisão: ', round(acuracia_avore, 5))
print('Acurácia SVM: ', round(acuracia_svm, 5))
print('############################')

r = export_text(arvore, feature_names=iris['feature_names'])
print('Estrutura da árvore')
print(r)


# A etapa de mapeamento entre categorias e números se chama codificação categórico-numérica e o pré-processamento já foi realizada e disponibilizada pela função load_iris().

# A variável características contém uma lista com 150 itens, onde cada item contém outra lista com quatro elementos.
# Cada um dos quatro elementos corresponde ao comprimento da sépala, largura da sépala, comprimento da pétala e largura da pétala, respectivamente.

# A variável rótulo contém uma lista com 150 itens que variam entre 0, 1 ou 2. Cada número corresponde a uma classe de flor (0: Iris-Setosa; 1:Iris-Versicolor; 2:Iris-Virginica).
# Outra etapa de pré-processamento a realizar é a partição dos dados. Ela nos permitirá verificar a qualidade do algoritmo de classificação. Para isso, precisamos particionar nossos dados em treino e teste.
# Os dados de treino são utilizados para treinar (ajustar) o algoritmo, enquanto os dados de testes são utilizados para verificar a acurácia dele, comparando o valor calculado para os testes com os valores reais.
# Para separar as amostras em treino e teste, o Scikit-Learn disponibiliza uma função chamada train_test_split, que recebe como primeiro parâmetro uma lista com as características e segundo parâmetro uma lista com os rótulos.

# Com a etapa de pré-processamento concluída, o próximo passo é treinar um algoritmo de classificação com os dados de treino.
# Para isso, criamos uma instância do classificador DecisionTree passando como parâmetro a profundidade máxima da árvore, ou seja, o número máximo de níveis, ou camadas, a partir do nó raiz, que a árvore encontrada poderá ter.
# Para realizar o treinamento (fit), precisamos passar os parâmetros X e y, que conterão as características de treino e rótulos de treino respectivamente.
# Após treinado o algoritmo, vamos utilizar o método predict do objeto árvore, passando como argumento as características para teste.
# Esse resultado será utilizado como parâmetro para a função accuracy_score, que calcula a acurácia do classificador, comparando os resultados preditos com os resultados reais.
# Analogamente, faremos o treinamento de um algoritmo de classificação utilizando o SVM, por meio da classe SVC (support vector classification) em que utilizaremos os valores padrão do construtor para o classificador

# No pós-processamento, vamos imprimir a acurácia de cada classificador e uma representação textual da árvore, utilizando a função export_text.
# A acurácia do classificador SVC foi ligeiramente melhor que da árvore de decisão, 0,97 contra 0,92 da árvore.
