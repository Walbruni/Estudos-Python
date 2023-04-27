

maxFila = 10
fila = [None] * maxFila
inicioFila = None
finalFila = None


class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

# para o caso encadeado (insercao)
    def insere(self, novoNo):
        if self.inicio == None:  # fila vazia
            self.inicio = novoNo  # atualiza inicio da fila
            self.final = novoNo  # atualiza final da fila
        else:
            self.final.proximo = novoNo  # insere o nó
            self.final = novoNo  # atualiza o final da fila

# para o caso encadeado (remocao)
    def remove(self):
        if self.inicio == None:  # erro de fila vazia
            return None  # None indica erro de fila vazia
        else:
            k = self.inicio  # salva o nó removido
            self.inicio = self.inicio.proximo  # remove o nó
            return k  # retorna o nó removido

# para o caso contiguo (insercao)
    def insereFila(novoNo):
        global inicioFila  # acesso as variaveis globais
        global maxFila
        global finalFila
        global fila

        if inicioFila == None:  # fila vazia
            fila[0] = novoNo  # insere o nó
            inicioFila = 0  # atualiza o inicio da fila
            finalFila = 0  # atualiza o final da fila

        elif (finalFila + 1) % maxFila == inicioFila:  # fila cheia
            return -1  # retorna erro de fila cheia

        else:
            finalFila = (finalFila + 1) % maxFila  # atualiza o final da fila
            fila[finalFila] = novoNo  # insere o nó
        return finalFila  # saída normal

# para o caso contiguo (remocao)
    def removeFila():
        global inicioFila  # indica o acesso a variaveis globais
        global maxFila
        global finalFila
        global fila

        if inicioFila == None:  # fila vazia
            return None  # erro fila vazia

        k = fila[inicioFila]  # salva o nó removido
        if finalFila == inicioFila:
            inicioFila = None  # fila vazia após remoção

        else:
            inicioFila = (inicioFila + 1) % maxFila  # remove o nó
        return k  # retorna k = o nó consumido

# teste em alocacao contigua
    print(fila)
    for i in range(10):
        insereFila(i)

    print(insereFila(11))

    for i in range(10):
        print(removeFila())

    print(removeFila())
