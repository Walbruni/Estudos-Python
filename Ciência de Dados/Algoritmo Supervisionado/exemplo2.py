
# Implemente uma solução para estudar o comportamento de uma série temporal com Regressão linear

# a regressão linear é de extrema importancia quando se quer estudar tendencias!!

import numpy as np
# framework para ciencia de dados (sikitlearn)
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1)) # reorganização dos elementos da lista 
y = np.array([6, 12, 14, 23, 27, 32])


model = LinearRegression().fit(x, y) # o fit é o processo de montagem da função para encontrar a regressão 


y_pred = model.predict(x) # passado os parametros de x 
print('Dados do teste:', y, sep='\n') # os dados reais do teste
print('Dados da predição:', y_pred, sep='\n') # os dados que o modelo gerou para a comparação 

# matplotlib para a impressão
plt.scatter(x, y, c='blue')
plt.plot(x, y_pred, c='red')
plt.legend(['Predição', 'Real'])
plt.show()
