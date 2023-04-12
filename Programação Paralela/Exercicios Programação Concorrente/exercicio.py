
# exercicio 1
# Inicie a execução de um Thread, coloque-a para esperar 2 segundos e informe o inicio e o final da execução da Thread

from time import sleep
from threading import Thread


def tarefa(tempo_espera, mensagem):
    print(f'Iniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')


x = Thread(target=tarefa, args=(2, 'Thread em execução'))
x.start()

print('Aguardando a execução da thread...')
x.join()
print('A execução foi concluida!')


# exercicio 2
# Inicie a execução de duas Threads, coloque a primeira e a segunda para esperar, respectivamente, 3 e 2 segundos, e informe a ordem da execução das threads

def execucao(tempo, nome):
    print(f'Iniciando a {nome} execução')
    sleep(tempo)
    print(f'Concluida a {nome} execução')


a = Thread(target=execucao, args=(3, 'primeira'))
a.start()  # inicia a thread

print('Aguardando...')
a.join()  # aguarda pelo resultado


b = Thread(target=execucao, args=(2, 'segunda'))
b.start()  # inicia a thread

print('Aguardando...')
b.join()  # aguarda pelo resultado

print('As execuções das Threads foram concluidas!')


# exercicio 3
# Inicie a execução de duas Threads, em que a primeira deve calcular o quadrado de um numero e a segunda deve calcular o cubo de um numero,
# coloque a primeira e a segunda para esperarem, respectivamente, 2 e 3 segundos, e informe a ordem de execução das threads.

def calculo1(ao_quadrado, tempo):
    print(f'Quadrado do numero: {ao_quadrado}')
    ao_quadrado = ao_quadrado ** 2
    sleep(tempo)
    print(f'Resultado: {ao_quadrado}')
    print('Conclusão do calculo do quadrado')


def calculo2(ao_cubo, tempo):
    print(f'Cubo do numero: {ao_cubo}')
    ao_cubo = ao_cubo ** 3
    sleep(tempo)
    print(f'Resultado: {ao_cubo}')
    print('Conclusão do calculo do cubo')


quadrado = Thread(target=calculo1, args=(5, 2))
quadrado.start()
print('Aguardando o calculo...')
quadrado.join()

cubo = Thread(target=calculo2, args=(5, 3))
cubo.start()
print('Aguardando o calculo...')
cubo.join()

print('As execuções dos calculos foram concluidos!')
