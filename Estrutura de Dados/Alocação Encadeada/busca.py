
# Busca em alocação encadeada

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def busca(self, k):
        noAtual = self.cabeca
        if noAtual.chave == k:
            return noAtual  # trata o caso em que o nó buscado seja o primeiro nó

# laço de progressão por todos os nós da lista (quando nao o nó buscado não for o primeiro)
        while noAtual.proximo != None:  # enquanto noAtual.proximo diferente de nulo
            noAtual = noAtual.proximo  # o noAtual passa a ser o próximo

            if noAtual.chave == k:  # verifica se a chave do novo nó buscado corresponde a k
                return noAtual  # se sim, retorne o noAtual, chave encontrada

        return None  # trata o caso em que o nó não é encontrado na lista


e0 = No(0, 'Joao')
Lista = ListaEncadeada(e0)
k0 = Lista.busca(0)
print(k0.valor)


# complexidade O(n)
