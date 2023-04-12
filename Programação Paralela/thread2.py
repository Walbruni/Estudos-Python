
import threading
import time


# exemplo de funcao com parametro
def funcao(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)


print("Iniciando o programa!")
# a virgula após a mensagem passada como argumento é necessaria, pois se trata de uma tula para as threads
x = threading.Thread(target=funcao, args=('Executando',)) # parametro passado na thread 
x.start()
print("Finalizando o programa!")
