
# Utilizaremos uma série histórica fictícia de casos de dengue de uma determinada cidade e, com o auxílio do algoritmo supervisionado de regressão linear, predizeremos casos futuros.
# A série está em uma planilha (arquivo CSV) com duas colunas, ano e casos (número de casos). Na planilha, temos o número de casos de 2001 a 2017.
# Utilizaremos essa série histórica e aplicaremos o algoritmo de regressão linear para estimar os casos de dengue para o ano de 2018.


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas

#############      Pré-processamento     ###############
# Coleta e Integração
arquivo = pandas.read_csv('dados_dengue.csv')

anos = arquivo[['ano']]
casos = arquivo[['casos']]

##############       Mineração        #################
regr = LinearRegression()
regr.fit(X=anos, y=casos)

ano_futuro = [[2018]]
casos_2018 = regr.predict(ano_futuro)

print('Casos previstos para 2018 ->', int(casos_2018))

############      Pós-processamento     ################
plt.scatter(anos, casos, color='black')
plt.scatter(ano_futuro, casos_2018, color='red')
plt.plot(anos, regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2018])
plt.yticks([int(casos_2018)])

plt.show()


# A classe da biblioteca Scikit-Learn utilizada para realizar a regressão linear se chama LinearRegression.
# Para realizar a regressão, ela precisa dos dados de treinamento (parâmetro X) e seus respectivos resultados (parâmetro y).
# Como estamos usando apenas uma variável para o parâmetro X, o ano, temos uma regressão linear simples e o resultado esperado é uma reta, onde temos os anos no eixo x e os casos no eixo y.

# Após a execução do método fit, o objeto regr está pronto para ser utilizado para predizer os casos para os anos futuros, utilizando o método predict.
# Ao chamar o método predict passando o ano 2018 como argumento, recebemos como retorno o número de casos previsto para 2018

# Na etapa de pós-processamento, na qual utilizamos a biblioteca Matplotlib para exibir um gráfico com os dados da série (pontos em preto), a reta obtida pela regressão, em azul, e o valor predito para o ano de 2018, em vermelho
