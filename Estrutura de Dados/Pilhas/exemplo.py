
# Para uma alocação encadeada, você só precisa manter um ponteiro para o início (comumente chamado de topo) da pilha.
# Se a pilha estiver vazia, o TopoPilha apontará para o valor nulo.

class PilhaEncadeada:
    def __init__(self, topo=None):
        self.topo = topo


# Para uma alocação contígua, você usará o espaço alocado de memória exatamente como uma pilha, enchendo da base (índice 0) para cima, e manterá uma variável TopoPilha que guarda o índice do topo da pilha.
# Deve apenas tomar cuidado para não armazenar mais nós do que o espaço reservado (que pode ser salvo em MaxPilha).

# Indice     Endereco de Memoria     No
#   4                24                     <-- maxPilha
#   3                20
#   2                16              k2     <-- topoPilha
#   1                12              k1
#   0                 8              k0     <-- pilha


# No esquema acima, podemos ver que a variável Pilha aponta para o início do espaço alocado em memória. Pilha[0] contém o nó k0, e assim por diante.
# O topo da pilha está apontado por TopoPilha, que tem valor 2.
# O valor de MaxPilha é 5, ou seja, se topo pilha apontar para 4 e tentarmos inserir um nó, deve ocorrer um erro e a inserção não vai acontecer.

maxPilha = 10
pilha = [None] * maxPilha
topoPilha = None


class PilhaEncadeada:
    def __init__(self, topo=None):
        self.topo = topo

# insercao (tambem chamada de push)
# caso encadeado
    def push(self, novoNo):
        novoNo.proximo = self.topo  # insere o novo no
        self.topo = novoNo  # atualiza o topo da pilha

# remocao (tambem chamado de pop)
# caso encadeado
    def pop(self):
        if self.topo == None:
            return None  # erro de pilha vazia (underflow)

        k = self.topo  # salva o no removido
        self.topo = self.topo.proximo  # aponta o topo para o prximo e remove o no
        return k  # retorna o no removido


# Para o caso contíguo, você possui 3 variáveis: Pilha guarda o espaço de memória, MaxPilha guarda o número máximo de elementos na pilha, TopoPilha guarda o índice do topo da pilha.
maxPilha = 10
pilha = [None] * maxPilha
topoPilha = None


# insercao
def push(novoNo):
    global pilha
    global topoPilha
    global maxPilha

    if topoPilha == None:  # pilha vazia
        pilha[0] = novoNo  # insere o no
        topoPilha = 0  # atualiza o topo da pilha

    # elif (topoPilha = maxPilha - 1): # pilha cheia
    #     return - 1 # erro de pilha cheia (overflow)

    else:
        topoPilha = topoPilha + 1  # atualiza o topo da pilha
        pilha[topoPilha] = novoNo  # insere o no
    return topoPilha  # saida normal


# remocao
def pop():
    global pilha
    global topoPilha
    global maxPilha

    if topoPilha == None:  # erro de pilha vazia (underflow)
        return None  # retorna vazio

    else:
        k = pilha[topoPilha]  # salva o no removido
        if topoPilha == 0:  # a pilha so possuia um no
            topoPilha = None  # pilha vazia apos a remocao

        else:
            topoPilha = topoPilha - 1  # remove o no
        return k  # retorna o no removido


# teste
print(pilha)
for i in range(10):
    push(i)
    print(pilha)

# print(push(11))
for i in range(10):
    print(pop())
print(pop)
