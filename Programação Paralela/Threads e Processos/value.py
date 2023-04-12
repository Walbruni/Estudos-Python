
# Para criar uma área de memória compartilhada e permitir que diferentes processos acessem a mesma variável, podemos utilizar a classe value do módulo multiprocessing

from threading import Thread
from multiprocessing import Process, Value


def funcao_a(indice, cont):
    for i in range(100000):
        with cont.get_lock():
            cont.value += 1
    print("Termino processo", indice)


def main():
    contador = Value('i', 0)
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice, contador))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador.value)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador.value)


if __name__ == "__main__":
    main()


# Como não temos acesso a variáveis globais entre os processos, precisamos passar esta para o construtor process por meio do parâmetro args.
# Como a passagem de parâmetros é posicional, o parâmetro índice da funcao_a recebe o valor da variável índice e o parâmetro cont recebe uma referência para a variável contador
# Isso já é o suficiente para termos acesso à variável contador por meio do parâmetro cont da função funcao_a. Porém, não resolve a condição de corrida.
# Para evitar esse problema, vamos utilizar uma trava (lock) para realizar a operação de incremento, assim como fizemos no exemplo anterior.
# O Python já disponibiliza essa trava nos objetos do tipo value, não sendo necessário criar uma variável específica para a trava (lock).
# Observe como foi realizada a trava utilizando o método get_lock()
