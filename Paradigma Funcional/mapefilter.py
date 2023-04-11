
# Na programação funcional, como boa prática, NÃO é recomendado utilizar laços de repetição (for e while), mas sim composição de funções ou recursividade

# Map
# Utilizada para aplicar uma determinada função em cada elemento de um iterável (lista, tupla, dicionários etc.), retornando um novo iterável com os valores modificados.
# A função map é pura e de ordem superior, pois depende apenas de seus parâmetros e recebe uma função como parâmetro.
# A função map sempre retorna um novo iterável.

lista = [1, 2, 3, 4, 5]


def triplica(item):
    return item * 3


def main():
    nova_lista = map(triplica, lista)
    print(list(nova_lista))


if __name__ == '__main__':
    main()

# utilizando o map com a função lambda

lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista)


def main():
    print(list(nova_lista))


if __name__ == '__main__':
    main()


# Filter
# É utilizada para filtrar elementos de um iterável (lista, tupla, dicionários etc.)
# O filtro é realizado utilizando uma função, que deve ser capaz de retornar true ou false (verdadeiro ou falso) para cada elemento do iterável.
# Todo elemento que for avaliado como true será incluído em um novo iterável retornado pela função filter, que é pura e de alta ordem, pois depende apenas dos parâmetros e recebe uma função como parâmetro.

lista = [1, 2, 3, 4, 5]


def impar(item):
    return item % 2 != 0


def main():
    nova_lista = filter(impar, lista)
    print(list(nova_lista))


if __name__ == '__main__':
    main()


# utilizando o filter com a função lambda

lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)


def main():
    print(list(nova_lista))


if __name__ == '__main__':
    main()


# A programação funcional é muito útil para a manipulação de listas e se adequa muito bem em aplicações de Big Data!
