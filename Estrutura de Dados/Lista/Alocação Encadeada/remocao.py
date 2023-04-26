
# remocao em alocacao encadeada

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def removeLista(self, k):
        noAtual = self.cabeca
        if noAtual == None:  # erro, lista vazia
            return None

        if noAtual.chave == k:  # primeiro nó é o alvo
            self.cabeca = noAtual.proximo
            return 0

        noAnterior = noAtual  # continua a busca
        noAtual = noAtual.proximo

        while (noAtual != None):
            if noAtual.chave == k:  # chave encontrada
                noAnterior.proximo = noAtual.proximo  # removeu o nó
                return k
            else:
                noAnterior = noAtual  # continua a busca
                noAtual = noAtual.proximo

        return -1  # erro, chave nao encontrada


# complexidade O(n)

Lista = ListaEncadeada()
Lista.removeLista(2)


# A remoção de um nó se dá fazendo com que o ponteiro do nó anterior a ele aponte para outro nó.
# Para não perder o encadeamento da lista, o ponteiro do nó anterior tem que apontar para o nó seguinte ao nó removido.
