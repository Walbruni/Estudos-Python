
# Insercao em alocação encadeada

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

# exemplo para listas NAO ordenadas
    def insereFinal(self, novoNo):
        noAtual = self.cabeca
        if noAtual:  # caso a lista nao esteja vazia
            while noAtual.proximo:
                noAtual = noAtual.proximo  # busca o final da lista
                noAtual.proximo = novoNo
        else:  # caso a lista esteja vazia
            self.cabeca = novoNo

# complexidade O(n)

# outra forma é inserir novos nós no inicio da lista (tendo em vista que se trata de lista NAO ordenada!)
    def insereInicio(self, novoNo):
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo

# complexidade O(1)

# exemplo para listas Ordenadas!

    def insereOrdenada(self, novoNo):
        noAtual = self.cabeca  # inicio da busca da posição
        if noAtual.chave > novoNo.chave:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo  # insere no inicio
            return 0
        if noAtual.proximo != None:
            while (noAtual.chave < novoNo.chave):
                if (noAtual.proximo == None):
                    noAtual.proximo = novoNo  # insere no final
                    return 0

                noAnterior = noAtual
                noAtual = noAtual.proximo  # continua a busca
                # fim da busca
        novoNo.proximo = noAtual  # apontar novo nó
        noAnterior.proximo = novoNo  # inserir novo nó

# complexidade O(n)


e1 = No(1, 'Maria')
Lista = ListaEncadeada(e1)

Lista.insereFinal(e1)
e2 = No(-1, 'Ana')
Lista.insereInicio(e2)
e3 = No(2, 'Arthur')
Lista.insereOrdenada(e3)
