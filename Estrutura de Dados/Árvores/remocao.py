
# O processo de remoção do nó de uma árvore binária de busca deve obedecer as seguintes regras:
# - Se o nó a ser deletado é uma folha: a remoção é simples. Basta buscar pelo nó e remove-lo
# - Se o nó a ser excluido tem apenas um filho: Copie o filho para o nó e exclua o filho
# - Se o nó a ser excluido tem dois filhos: Encontre o sucessor in-order (em ordem) do nó. Copie o conteúdo do sucessor in-order para o nó e exclua o sucessor in-order.

class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


def valorNo(no): # função para auxiliar a remoção dos nós 
        atual = no
        
        while(atual.esquerda is not None):
            atual = atual.esquerda
        return atual 

# remoção em árvores binárias de busca
def deleteBST(raiz, chave):
    if raiz is None:
        return raiz

    if chave < raiz.chave:  # se o elemento a ser removido é menor que o nó atual
        raiz.esquerda = deleteBST(raiz.esquerda, chave)  # segue a esquerda

    elif (chave > raiz.chave):  # se o elemento a ser removido é maior que o nó atual
        raiz.direita = deleteBST(raiz.direita, chave)  # segue a direita

    else:  # armazenar temporariamente a chave que ira substituir a chave eliminada
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp

        temp = valorNo(raiz.direita) # depois de eliminar, substituir pela chave temporaria 
        raiz.chave = temp.chave
        raiz.direita = deleteBST(raiz.direita, temp.chave)
