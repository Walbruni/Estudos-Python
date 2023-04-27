
# Inserção na fila (acontece sempre ao final - logica FIFO - first in - first out)


# exemplo encadeado
def insere(self, novoNo):
    if self.inicio == None:
        self.inicio = novoNo
        self.final = novoNo
    else:
        self.final.proximo = novoNo
        self.final = novoNo

# complexidade constante O(1)


# exemplo contiguo (aritmetica modular: uma variavel apontando para o inicio da fila, outra para o final da fila e outra reserva o valor do maximo da fila)
def insereFila(novoNo):
    global inicioFila
    global maxFila
    global finalFila
    global fila

    # tratamento para caso a fila esteja vazia
    if inicioFila == None:
        fila[0] = novoNo
        inicioFila = 0
        finalFila = 0

    # tratamento de erro para caso a fila esteja cheia (overflow)
    elif (finalFila + 1) % maxFila == inicioFila:
        return -1

    # tratamento geral caso nenhum dos acima ocorra
    else:
        finalFila = (finalFila + 1) % maxFila
        fila[finalFila] = novoNo
    return finalFila

# complexidade constante O(1)
