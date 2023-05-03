
# Operação de busca em árvore binária

class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


if __name__ == '__main__':
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)

    raiz.direita.esquerda = NoArvore(65)
    raiz.direita.direita = NoArvore(85)
    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita = NoArvore(45)


# imprimir a arvore implementada

cont = [10]


def imprimeArvoreRecurs(raiz, nivel):
    if (raiz == None):
        nivel = nivel + cont[0]
        return nivel


# imprime filhos a direita
imprimeArvoreRecurs(raiz.direita, nivel)
print()
for i in range(cont[0], nivel):
    print(end="")
    print(f'{raiz.chave}<')


# imprime filhos a esquerda
imprimeArvoreRecurs(raiz.esquerda, nivel)


def imprimeArvore(raiz):
    imprimeArvoreRecurs(raiz, 0)


def buscaBST(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz

    if raiz.chave < chave:
        return buscaBST(raiz.direita, chave)
    else:
        return buscaBST(raiz.esquerda, chave)
