
import threading
import time


# sincronizando threads

ls = []


def contador1(n):
    for i in range(1, n + 1):  # range de 1 ate o valor passado para n + 1
        print(i)
        ls.append(i)
        time.sleep(0.4)  # aguarda 0,4 segundos entre um e outro


def contador2(n):
    for i in range(6, n + 1):  # range de 6 ate o valor passado
        print(i)
        ls.append(i)
        time.sleep(0.5)


x = threading.Thread(target=contador1, args=(5,))  # atribuindo 5 ao valor de n
x.start()
# o laço for vai de 1 ate 5 (pois é sempre um valor a menos, n = 5, 5 + 1 = 6)

# o uso desse x.join() fara com que a lista impressa seja apos a finalizaçao das thread
# ou seja, da maneira como voce quer que seja executado
x.join()

# atribuindo 10 ao valor de n ao segundo contador
y = threading.Thread(target=contador2, args=(10,))
y.start()
# o laço for vai de 6 ate 10

# em funcao do sleep, ficara alternando em cada uma das threads
# a lista gerada com esses dois join() sera alternada
x.join()
y.join()

# a instrução de printar a lista sera executada somente apos a thread
# caso exclua o x.join() e y.join() a lista sera mostrada antes, pois nao seguira o curso que voce desejar
print(ls)


# para que a thread siga a sequencia que voce quer que ela realize, é necessário a utilizando do join()
# do contrário, ela não seguirá uma sequencia definida
