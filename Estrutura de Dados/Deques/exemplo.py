
# exemplo utilizando o modulo collections do Python
from collections import deque

q = deque()  # cria o deque

q.append('b')  # insere no final

q.append('c')  # insere no final

q.appendleft('a')  # insere no inicio

print(q)  # imprime o deque
print(q.popleft())  # remove do inicio
print(q.pop())  # remove do final


# criando o proprio deque
# Para uma alocação encadeada, você precisa manter um ponteiro para o início e para o final do deque.
# Se o deque estiver vazio, ambos apontarão para o valor nulo.
# Utiliza-se um encadeamento duplo, que permite percorrer a lista em qualquer uma das direções e a partir de qualquer uma das pontas.
class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None


class DequeEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio


# para insercao no inicio da estrutura, seu funcionamento é identico a Pilha.
# para insercao no final da estrutura, seu funcionamento é identifico a Fila.

# para remoção no inicio da estrutura, seu funcionamento é identico a Pilha.

# caso encadeado
# quando a remoção ocorre no final, usa-se a seguinte estrutura:

    def popBack(self):
        if self.inicio == None:  # erro deque vazia
            return None  # None indica erro quando vazia

        else:
            k = self.final  # salva o nó removido
            self.final = self.final.anterior  # remove o nó
            self.final.proximo = None  # aponta o proximo do final para Nulo
            return k  # retorna o nó consumido


# Para alocacao contigua, pode-se usar um vetor circular igual para a fila.
# As duas variáveis (InicioDeque e FinalDeque) indicam as pontas do deque e vão se deslocando conforme os nós são inseridos e removidos.
# Ao chegar ao fim do espaço alocado e ser incrementada, a variável faz a volta e o índice volta para zero.
maxDeque = 10
deque = [None] * maxDeque
inicioDeque = None
finalDeque = None


# remoção no caso contiguo
# Possui 4 variáveis: Deque guarda o espaço de memória, MaxDeque guarda o número máximo de elementos do deque, InicioDeque e FinalDeque guardam o índice do início e final do deque.
def popBack():
    global inicioDeque  # indica o acesso as variaveis globais
    global maxDeque
    global finalDeque
    global deque

    if inicioDeque == None:  # deque vazia
        return None  # erro de deque vazia

    k = deque[inicioDeque]  # salva o nó removido
    if finalDeque == inicioDeque:
        inicioDeque = None  # deque vazia após remoção

    else:
        finalDeque = (finalDeque - 1) % maxDeque  # remove o nó
        return k  # retorna o nó consumido
