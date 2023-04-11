
# Dados imutáveis
# São aqueles que não podem ser alterados após a sua criação.
# As funções puras devem utilizar apenas os parâmetros de entrada para gerar as saídas.
# Além dessa característica, as funções puras não podem alterar nenhuma variável fora de seu escopo.

# funcao 3
# captando os valores do campo input
valores = input('Digite três numeros: ')

# separando os valores pelo espaço em branco e transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    # essa forma, se altera o valor da variavel global 'valores'. Na programacao funcional, devemos evitar a alteracao de qualquer dado que ja tenha sido criado
    lista[2] = lista[2] + 10
    return lista


def main():
    print('Nova lista', altera_lista(valores))
    print('Nova lista', altera_lista(valores))


if __name__ == '__main__':
    main()


# funcao 4 (Função a ser seguida no paradigma funcional!)
valores = input('Digite três numeros: ')

valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    # aqui ao inves de alterar o valor do proprio parametro, criamos uma copia dele 'nova_lista', sendo assim, nao alteramos a variavel 'valores' e obtemos o mesmo resultado para as duas chamadas da funcao
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return lista


def main():
    print('Nova lista', altera_lista(valores))
    print('Nova lista', altera_lista(valores))


if __name__ == '__main__':
    main()


# IMPORTANTE - Evitar efeitos colaterais!
# As funções puras e dados imutáveis buscam evitar os efeitos indesejáveis. Na terminologia de programação funcional, chamamos isso de efeito colateral (side effect). Além de evitar o efeito colateral, a programação funcional evita a dependência do estado de um programa.
# A dependência apenas dos parâmetros para gerar saídas garante que o resultado será sempre o mesmo, independentemente do estado da aplicação, por exemplo, valores de outras variáveis. Ou seja, não teremos diferentes comportamentos para uma função baseado no estado atual da aplicação.
# O objetivo principal da programação funcional não é utilizar funções puras e dados imutáveis, mas sim evitar o efeito colateral.
