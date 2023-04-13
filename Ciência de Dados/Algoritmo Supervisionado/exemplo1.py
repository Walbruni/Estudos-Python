
# treinamento supervisionado - classificação

from sklearn.tree import DecisionTreeClassifier


lisa = 1
irregular = 0

pera = 1
laranja = 0

# é necessário passar as informações para que o algoritmo aprenda com elas (treinamento)
pomar = [[120, lisa], [140, lisa], [180, irregular], [200, irregular]]

resultado = [pera, pera, laranja, laranja]

# gerar arvore de decisao
clf = DecisionTreeClassifier()

# classificador
clf = clf.fit(pomar, resultado)

# informações passadas pelo usuario como entrada para retornar o tipo da fruta que esta sendo tratada baseado no peso e na superficie
peso = int(input('Digite o peso: '))
# 1 para lisa e 0 para irregular
superficie = int(input('Digite a superficie: '))

resultado_final = clf.predict([[peso, superficie]])

if resultado_final == 1:
    print('Pera')
else:
    print('Laranja')
