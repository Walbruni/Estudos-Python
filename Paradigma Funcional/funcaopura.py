
# Funções Puras
# São aquelas que dependem apenas dos parâmetros de entrada para gerar uma saída. Elas sempre retornam um valor, um objeto ou outra função. Em qualquer ponto do programa, ao chamar uma função pura, com os mesmos parâmetros, devemos obter sempre o mesmo resultado.

# funcao 1 (exemplo de função NÃO pura - pois além de nao depender apenas dos parametros, essa função nao retorna valor algum)
valor = 20


def multiplica(fator):
    global valor
    valor = valor * fator
    print('Resultado', valor)


def main():
    numero = int(input('Digite um numero: '))
    multiplica(numero)
    multiplica(numero)


# NAME referente a ele tem valor igual à "__main__".
# Nesse caso, a condição do IF a seguir será TRUE, então o que está no corpo do IF será executado.
if __name__ == '__main__':
    main()


# funcao 2 (exemplo de função PURA! - Pois depende apenas de seus parametros para gerar o resultado, e nao acessa ou modifica nenhuma variavel externa à função e retorna um valor)
# Função a ser seguida no paradigma funcional!
valor = 20


def multiplica(valor, fator):
    valor = valor * fator
    return valor


def main():
    numero = int(input('Digite um numero: '))
    print('Resultado', multiplica(valor, numero))
    print('Resultado', multiplica(valor, numero))


if __name__ == '__main__':
    main()


# IMPORTANTE - Evitar efeitos colaterais!
# As funções puras e dados imutáveis buscam evitar os efeitos indesejáveis. Na terminologia de programação funcional, chamamos isso de efeito colateral (side effect). Além de evitar o efeito colateral, a programação funcional evita a dependência do estado de um programa.
# A dependência apenas dos parâmetros para gerar saídas garante que o resultado será sempre o mesmo, independentemente do estado da aplicação, por exemplo, valores de outras variáveis. Ou seja, não teremos diferentes comportamentos para uma função baseado no estado atual da aplicação.
# O objetivo principal da programação funcional não é utilizar funções puras e dados imutáveis, mas sim evitar o efeito colateral.
