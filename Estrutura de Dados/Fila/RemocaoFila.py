
# Remocao na fila (acontece sempre no inicio - logica FIFO - first in - first out)


# exemplo encadeado
def remove(self):
    # tratamento de erro para fila vazia (underflow)
    if self.inicio == None:
        return None

    # tratamento para a remocao
    else:
        k = self.inicio  # variavel guarda o valor removido
        # aponta o endereco de inicio da fila para o proximo elemento
        self.inicio = self.inicio.proximo
        return k  # retorna o elemento removido

# complexidade constante O(1)


# exemplo contiguo (aritmetica modular)
def removeFila():
    global inicioFila
    global maxFila
    global finalFila
    global fila

    if inicioFila == None:  # fila vazia (erro de underflow)
        return None

    k = fila[inicioFila]  # salva o nó removido
    if finalFila == inicioFila:  # se forem iguais significa que a fila so tinha um elemento
        inicioFila = None  # fila vazia apos remocao

    else:
        # remove o nó (atualiza o inicio da fila)
        inicioFila = (inicioFila + 1) % maxFila

    return k
