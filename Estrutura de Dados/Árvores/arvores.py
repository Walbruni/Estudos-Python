

# Árvores (trees) são estruturas de dados hierárquicas e não linearizadas. 
# são formadas por um conjunto de elementos, que chamamos de nós (ou nodos ou vértices), conectados por um conjunto de arestas. 
# Um dos nós, que dizemos estar no nível 0, é a raiz da árvore e está no topo da hierarquia.
# A raiz está conectada a outros nós, no nível 1, que, por sua vez, estão conectados a outros nós, no nível 2, e assim por diante. 
# Os nós que estão no fim da árvore são chamados de folhas.
# As conexões entre os nós de uma árvore seguem uma nomenclatura genealógica. 
# Um nó, em dado nível, está conectado a seus filhos (no nível abaixo) e a seu pai (no nível acima). A raiz da árvore, que está no nível 0, possui filhos, mas não possui pai.
# Representa-se uma árvore em memória por meio de alocação dinâmica. A árvore não é representada como um todo, mas uma referência para sua raiz.


# Árvores binárias são árvores nas quais cada nó pode ter no máximo dois filhos
# Uma árvore é um conjunto de nós, e cada nó é um objeto com chave e uma referencia aos seus dois filhos (esquerdo e direito)

# exemplo
class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


if __name__ == '__main__':
    raiz = NoArvore(55)  # raiz principal (root)

    raiz.esquerda = NoArvore(35)  # filho da raiz principal (root)
    raiz.direita = NoArvore(75)  # filho da raiz principal (root)

    raiz.direita.esquerda = NoArvore(65)  # filhos do nó pai raiz.direita (75)
    raiz.direita.direita = NoArvore(85)  # filhos do nó pai raiz.direita (75)
    raiz.esquerda.esquerda = NoArvore(25) # filhos do nó pai raiz.esquerda (35)
    raiz.esquerda.direita = NoArvore(45)  # filhos do nó pai raiz.esquerda (35)

# os nós das extremidades que não possuem filhos são chamados de folhas (leaf)


# Árvores Binárias de Busca
# são árvores cujos nós são organizados de acordo com as seguintes propriedades:
# Todos os nós a esquerda da raiz, são menores ou iguais a ele.
# Todos os nós a direita da raiz, são maiores ou iguais a ele.

# exemplo
#                                                                                     raiz principal = 55
#                                               raiz.esquerda = 35                                                         raiz.direita = 75
#                            raiz.esquerda.esquerda = 25   raiz.esquerda.direita = 45                       raiz.direita.esquerda = 65   raiz.direita.direita = 85

                                                                      

# Árvores x Árvores binárias
# A principal diferença é a quantidade de filhos
# Uma árvore binária só pode ter no máximo dois filhos, enquanto uma árvore não possui essa limitação 