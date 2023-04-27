
# Politica do LIFO (Last in - First Out) - O ultimo elemento a entrar sera o primeiro a sair
# as inserções se dão no topo da fila, assim como as remoções

# Só pode colocar um novo elemento no topo da pilha ou retirar o elemento do topo da pilha, os demais estão “debaixo”, então não podem ser movidos.


# insercao
# exemplo encadeado
def push(self, novoNo):
    novoNo.proximo = self.topo
    self.topo = novoNo

# insercao
# exemplo contiguo (o mais usual para pilhas)


def push(novoNo):
    global pilha
    global topoPilha
    global maxPilha

    if topoPilha == None:  # pilha vazia
        pilha[0] = novoNo
        topoPilha = 0

    # elif (topoPilha=maxPilha - 1):  # pilha cheia
    #     return -1

    else:
        topoPilha = topoPilha + 1
        pilha[topoPilha] = novoNo  # insere o nó
        topoPilha

# complexidade constante O(1)


# remocao
# exemplo encadeado
def pop(self):
    if self.topo == None:  # verificar se estar vazia (underflow)
        return None
    k = self.topo  # salva o elemento a ser removido em k
    self.topo = self.topo.proximo  # aponta o topo para o proximo elemento
    return k


# remocao
# exemplo contiguo (mais comum)
def pop():
    global pilha
    global topoPilha
    global maxPilha

    if topoPilha == None:  # tratamento do underflow
        return None

    else:
        k = pilha[topoPilha]  # k guarda o topo da pilha
        if topoPilha == 0:  # se o topo for igual a 0 significa que so possuia um elemento
            topoPilha = None  # agora ela passara a estar vazia

        else:  # se possuia mais de um elemento na pilha
            topoPilha = topoPilha - 1  # diminui em um o indice guardado no topo da pilha
    return k

# complexidade constante O(1)
