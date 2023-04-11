
# Funções de Ordem Superior
# Na programação funcional, é muito comum utilizar funções que aceitem outras funções, como parâmetros ou que retornem outra função.

# funcao 5

# dentro da funcao pai multiplica_por, foi definido a funcao multi, que espera um parametro chamado multiplicando
def multiplicar_por(multiplicador):
    def multi(multiplicando):  # esse parametro sera multiplicado pelo multiplicador passado como parametro para a funcao pai
        return multiplicando * multiplicador
    return multi  # a funcao multi é retornada e armazenada na variavel abaixo multiplica_por_10


def main():
    # a função interna multi foi definida como multiplicando * 10
    # a variavel multiplica_por_10 é uma referencia para a funcao multi
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))

    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))


if __name__ == '__main__':
    main()
