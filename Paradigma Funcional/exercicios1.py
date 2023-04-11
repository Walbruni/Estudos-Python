
# exercicio 1
# Implementar uma solução (em programação funcional) na lista abaixo para transformar todos os nomes em maiusculos

veiculos = ['aviao', 'carro', 'navio', 'onibus']


# recebe uma string e o converte para maiusculo
f_maiuscula = lambda x: str.upper(x)


# o list transforma os objetos gerados para uma lista
nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(f'Nomes maiusculos: {nomes_maiusculos}')


# exercicio 2
# Implementar uma solução para imprimir apenas os números pares

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 24]

numeros_pares = lambda x: x % 2 == 0

pares = list(filter(numeros_pares,lista))

print(f'Lista de números pares: {pares}')
print(f'Teste para saber se o número é par = {numeros_pares(5)}') # booleano (True ou False)


# exercicio 3
# Implementar uma solução através da programação funcional para arredondar os valores da lista de números na mesma ordem da lista de precisão

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321] # float 
# os numeros serão arredondados de acordo com as casas abaixo. O primeiro (9.56783) será arredondado em 2 casas, e assim por diante 
lista_precisao = [2,2,3,3]

arredondamento = lambda x,y: round(x,y) # metodo para arredondar

resultado = list(map(arredondamento,lista_numeros,lista_precisao)) # mapeando para cada um dos elementos da lista 

print(resultado)


# exercicio 4
# Implementar uma solução para somar todos os elementos da lista 

from functools import reduce 
# utilizando o reduce para somar os numeros (redução) 1 + 2 = 3; 3 + 3 = 6, 6 + 4 = 10... e assim por diante 
f_soma = lambda x,y: x + y

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = reduce(f_soma,numeros)

print(resultado)
