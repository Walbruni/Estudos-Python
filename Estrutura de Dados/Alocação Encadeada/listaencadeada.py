
# LISTA ENCADEADA
# possui um campo especial, um ponteiro para o próximo nó da lista.
# Essa estrutura permite que os nós estejam salvos em espaços não contíguos da memória, espalhados por diversos endereços distantes entre si, mas que, ainda assim, seja possível percorrer a lista sem se perder.
# O ponteiro para o próximo nó deve armazenar o endereço em que está salvo o próximo nó. O último nó da lista, por sua vez, aponta para um valor nulo.
# So pode percorrer a lista apenas em um sentido, seguindo os ponteiros “próximo”.


class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def print(self):
        current = self.cabeca

        while current:
            print(current.valor)
            current = current.proximo


# LISTA DUPLAMENTE ENCADEADA
# Na lista duplamente encadeada um nó armazena não só o ponteiro para o próximo nó, como também um ponteiro para o nó anterior.
# Dessa forma, a lista pode ser percorrida em ambos os sentidos.
# Mantendo uma variavel apontada para o primeiro e para o ultimo nó da lista, permitirá que percorra a lista no sentido inverso, seguindo os ponteiros anteriores.

# com a lista ordenada
# Com o uso da variável armazenando o último nó, você consegue iniciar o percurso da lista de trás para frente.
# Somando a isso o uso de encadeamento duplo, você consegue percorrer a lista de trás para frente, no sentido em que as chaves estarão ordenadas em ordem decrescente.
