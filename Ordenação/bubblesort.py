
# ordenacao pelo metodo da bolha (bubblesort)
# consiste em ir movendo os elementos para o final da lista ate encontrarem a sua posicao correta
# o algoritmo vai percorrer o array fazendo trocas par a par entre dois elementos consecutivos

# procedimento para trocar elemento com o proximo
def trocar(seq, i):  # parametro dessa funcao é a sequencia e o indice
    aux = seq[i]
    seq[i] = seq[i + 1]
    seq[i + 1] = aux  # o que era seq[1] passa a ser seq[i + 1]


# inicializacao da sequencia de teste (lista nao-ordenada)
seq = [10, 5, 20, 1, 4]

# variavel de controle para o laço
troca = 1

# laço das multiplas passagens pela lista
while troca:
    troca = 0
    i = 0
    for i in range(len(seq)-1):  # laço interno de uma passagem pela lista
        if seq[i] > seq[i + 1]:
            trocar(seq, i)
            troca = 1  # caso ocorra a troca, essa variavel passa a ser 1 para 'avisar' ao laço principal
# o laço se encerra quando na passagem 'for' nao ocorrer mais nenhuma troca

# impressao da sequencia ordenada
print(seq)


# Na primeira passagem do laço for:
# [10, 5, 20, 1, 4]
# o algoritmo compara 10 > 5? Sendo true, ele troca a posição de ambos os elementos: [5, 10, 20, 1, 4]
# compara 10 > 20? Sendo false, nao ocorre troca: [5, 10, 20, 1, 4]
# compara 20 > 1? Sendo true, troca: [5, 10, 1, 20, 4]
# compara 20 > 4? Sendo true, troca: [5, 10, 1, 4, 20]

# com o primeiro laço interno 'for' encerrado, é iniciado uma segunda passagem pelo laço 'for':
# [5, 10, 1, 4, 20]
# compara 5 > 10? false, nao ocorre troca
# compara 10 > 1? true, ocorre a troca: [5, 1, 10, 4, 20]
# compara 10 > 4? true, ocorre a troca: [5, 1, 4, 10, 20]
# compara 10 > 20? false, nao ocorre troca

# Na terceira passagem, sera trocado o 5 com 1, depois 5 com 4.
# A lista nesse momento está ordenada, mas o algoritmo não sabe disso. Apenas sabe que houve trocas, logo ele precisará de uma quarta passagem para verificar que o array já está ordenado.


# bubblesort possui complexidade O(n2) em seu pior caso, mas é um algoritmo mais rápido quanto mais próximo de ordenada a lista de entrada estiver.

# A complexidade de melhor caso acontece com a lista de entrada já ordenada, caso no qual o algoritmo realiza apenas uma passagem comparando os valores consecutivos par a par.
# Isso se concretiza em complexidade linear ou O(n).
# Já no pior caso, a lista precisa ser totalmente invertida, necessitando de n passagens e somatório de 1 a (n - 1) trocas, o que resulta em uma complexidade quadrática, ou O(n2).
