
# USO DE FUNÇÕES

# As sentenças de funções def são executáveis. Isso implica que a função só pode ser chamada após a execução da sentença def.
# Ex:

escolha = input('Escolha uma opção de função: 1 ou 2? ')

if escolha == '1':
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)


# Existem funções com comportamento de procedimento, ou seja, não possuem retorno
# Ex:

def fun1(x):
    x = 10
    print(f'Função fun1 - x = {x}')


def fun2(x):
    x = 20
    print(f'Função fun2 - x = {x}')


x = 0
fun1(x)
fun2(x)
print(f'Programa principal - x = {x}')


# Aninhamento de subprogramas (função que tem dentro de sua definição, a definição de outra função)

def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


dist = eval(input('Diga a distância a ser percorrida em km: '))
pagamento = taximetro(dist)
print(f'O valor do pagamento é R$ {pagamento}')


# Implemente uma solução que retorne o menor elemento de uma lista

def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if (elem < minimo):
            minimo = elem
    return minimo


lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrar_minimo(lista_teste)
print('O menor elemento da lista é: [{}]'.format(menor))


# Implemente uma solução que retorne a soma de todos os elementos pares de uma lista

def ehPar(n):
    r = (n % 2 == 0)
    return r


def soma_par(lista):
    soma = 0
    for num in lista:
        if (ehPar(num)):
            soma = soma + num
    return soma


lista = [10, 2, 5, 7, 6, 3]
soma = soma_par(lista)
print(f'O somatório dos elementos pares da lista é: {soma}')


# Implemente uma solução que calcule o fatorial de um número (Também é um exemplo de função recursiva - aquela que chama a si mesmo)
# Atenção: as funções recursivas necessitam de uma condição de parada!

def fatorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        return n * fatorial(n-1)


numero = eval(input('Digite um número: '))
print(f'O fatorial de {numero} é: {fatorial(numero)}')


# Implemente uma solução que determine se um número é ou não Primo

def eh_primo(n):
    if (n < 2):
        return False

    i = n // 2
    while (i > 1):
        if (n % i == 0):
            return False
        i = i - 1
    return True


def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo'
    if (resultado):
        mensagem = f'O número {numero} é primo'
    return mensagem


numero = eval(input('Digite um número: '))
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
