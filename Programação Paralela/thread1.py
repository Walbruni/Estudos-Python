
# para utilizar a thread
import threading
import time


# exemplo de funcao sem parametro
def funcao():
    for i in range(3):
        print(i, 'Executando a thread!')
        time.sleep(1)


print("Iniciando o programa!")
threading.Thread(target=funcao).start()
print("Finalizando o programa!")


# imprime iniciando o programa
# executa a primeira linha da thread
# imprime o finalizando o programa (em função do time.sleep de 1 segundo)
# retorna a executar a thread dentro do for
