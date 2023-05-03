

class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


# inserção em árvores binárias de busca
def inserirBST(raiz, chave):
    if raiz is None:  # verificar se a raiz esta vazia
        return NoArvore(chave)
    else:  # se nao estiver vazia
        if raiz.chave == chave:  # verificar se o elemento a ser inserido ja esta na raiz
            return raiz
        elif raiz.chave < chave: # se o elemento a ser inserido é maior que o elemento do nó atual
            raiz.direita = inserirBST(raiz.direita, chave) # segue para a direita desse nó
        else: # se nao, caso seja menor
            raiz.esquerda = inserirBST(raiz.esquerda, chave) # segue para a esquerda desse nó 
    return raiz 


if __name__ == '__main__':
    raiz = NoArvore(55)
    inserirBST(raiz, 35)
    inserirBST(raiz, 75)
    inserirBST(raiz, 25)
    inserirBST(raiz, 45)
    inserirBST(raiz, 65)
    inserirBST(raiz, 85)
