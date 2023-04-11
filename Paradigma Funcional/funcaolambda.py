
# Funções Lambda
# Em Python, equivalem as funções anônimas!
# São definidas sem identificador (nome) e, normalmente, são utilizadas como argumentos para outras funções (de ordem superior)
# sintaxe: inicia-se com a palavra reservada lambda, seguida de uma sequencia de argumentos separados por virgulas, dois pontos e uma expressao de apenas uma linha
# Sempre retornam o valor da expressão automaticamente, não sendo necessário utilizar o return

# exemplo de função (não lambda)
def multiplicar(a, b):
    return a * b


# exemplo da mesma função sendo lambda (anonima)
lambda a, b: a * b

# As funções lambda podem ser armazenadas em variáveis para depois serem chamadas como uma função qualquer.


def multiplicar_por(multiplicador):
    # substituindo a função multi do exemplo de ordemsuperior.py por uma função lambda
    return lambda multiplicando: multiplicando * multiplicador


def main():
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))

    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))


if __name__ == '__main__':
    main()
