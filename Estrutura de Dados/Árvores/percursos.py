
# Pré-ordem: Visitar, primeiro, a raiz, depois a subárvore esquerda e, por último, a subárvore direita.
# Em ordem: Visitar, primeiro, a subárvore esquerda, depois a raiz e, por último, a subárvore direita. (tambem chamado em ordem simetrica)
# Pós-ordem: Visitar, primeiro, a subárvore esquerda, depois a subárvore direita e, por último, a raiz.


# percurso pre-ordem
def visitaPreOrdem(raiz):
    if raiz:
        print(raiz.chave)
        visitaPreOrdem(raiz.esquerda)
        visitaPreOrdem(raiz.direita)


# percurso in-ordem
def visitaInOrder(raiz):
    if raiz:
        visitaInOrder(raiz.esquerda)
        print(raiz.chave)
        visitaInOrder(raiz.direita)


# percurso pos-ordem
def visitaPosOrdem(raiz):
    if raiz:
        visitaPosOrdem(raiz.esquerda)
        visitaPosOrdem(raiz.direita)
        print(raiz.chave)


