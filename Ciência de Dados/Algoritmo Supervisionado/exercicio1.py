
# Carregar dados da base load_digits e informar a quantidade de dados.

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

digitos = load_digits()

# Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64
print('Shape dos dados de imagens: {}'.format(digitos.data.shape))

# Apresentar o total de dados rotulados com inteiros de 0 a 9
print('Shape dos dados rotulados: {}'.format(digitos.target.shape))


# Visualizar os dados que foram carregados.
plt.figure(figsize=(14, 4))  # dimensao das figuras que aparecerao em tela

# laço for para varrer os digitos, tanto os dados (data) quanto os rotulos (target)
for index, (imagem, rotulo) in enumerate(zip(digitos.data[0:5], digitos.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(imagem, (8, 8)), cmap=plt.cm.gray)
    plt.title('Treinamento: {}\n'.format(rotulo, fontsize=15))

plt.show()


# Utilizar um modelo de regressão logistica

# treinamento
x_treino, x_teste, y_treino, y_teste = train_test_split(
    digitos.data, digitos.target, test_size=0.25, random_state=0)

pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(x_treino, y_treino)

Pipeline(steps=[('standardscaler', StandardScaler()),
         ('logisticregression', LogisticRegression())])


# Utilizar o modelo de regressão logistica treinado para fazer classificação

# predição (classificação)
previsto = pipe.predict(x_teste[0].reshape(1, -1))
real = y_teste[0]
print('previsto: {}, real: {}'.format(previsto[0], real))
