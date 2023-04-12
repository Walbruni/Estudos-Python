
from threading import Thread, Lock

contador = 0


def funcao_a(indice):
    global contador
    for i in range(1000000):
        contador += 1
    print("Termino thread", indice)


def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)


if __name__ == "__main__":
    main()

# Esse resultado inesperado devido à sincronia na concorrência de threads (ou processos) se chama condição de corrida.

# Para evitar a condição de corrida, utilizamos a primitiva lock (trava). Um objeto desse tipo tem somente dois estados: travado e destravado.
# Quando criado, ele fica no estado destravado. Esse objeto tem dois métodos: acquire e release.
# Quando no estado destravado, o acquire muda o estado dele para travado e retorna imediatamente.
# Quando no estado travado, o acquire bloqueia a execução até que outra thread faça uma chamada ao método release e destrave o objeto.

contador = 0
lock = Lock()
print_lock = Lock()


def funcao_a(indice):
    global contador
    for i in range(1000000):
        lock.acquire()
        contador += 1
        lock.release()
    print_lock.acquire()
    print("Termino thread", indice)
    print_lock.release()


def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)


if __name__ == "__main__":
    main()
