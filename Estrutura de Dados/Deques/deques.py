
# A estrutura de dados deque é uma generalização da fila e da pilha, essencialmente permitindo que se adicione ou remova nós do início ou do final da lista.
# Para evitar confusões, as operações são normalmente identificadas com qual lado da fila está sendo alterado.
# A remoção de um nó do início pode ser chamada de pop_front, enquanto a remoção de um nó ao final pode ser chamada de pop_back.


# inserção no incio: igual a inserção na Pilha (push_front)

# inserção no final: igual a inserção na Fila (push_back)

# remoção no inicio: igual a remoção na Pilha ou Fila (pop_front ou pop_left)

# remoção no final: nao possui equivalencia aos demais (pop_back ou pop_right)

# exemplo de codigo para remoção no final
def popBack(self):
    if self.inicio == None:  # deque vazia (underflow)
        return None

    else:
        k = self.final  # ponteiro para o ultimo elemento salvo em k
        self.final = self.final.anterior  # final recebe agora o final anterior
        self.final.proximo = None  # o proximo apontara para o nulo (vazio)
        return k

# complexidade constante para inserção e remoção - O(1)
