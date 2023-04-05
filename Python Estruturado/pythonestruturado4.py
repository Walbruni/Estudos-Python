
# Tratamento de exceções na linguagem Python

# Tipos de exceções:

# KeyboardInterrupt (quando o usuário pressiona CTRL + C)
# OverflowError (quando uma expressão de ponto flutuante é avaliada como um valor muito grande)
# ZeroDivisionError (quando se tenta dividir por zero)
# IOError (quando uma operação de entrada/saída falha por um motivo relacionado a isso)
# IndexError (quando um índice sequencial está fora do intervalo de índices válidos)
# NameError (quando se tenta identificar (nome) não atribuído)
# TypeError (quando uma operação da função é aplicada a um objeto do tipo errado)
# ValueError (quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto)

# faça o tratamento de exceção para verificar se a entrada é, de fato, um número

try:
    x = int(input('Digite um número: '))
except ValueError:
    print('Digite um número válido.')


# Outro exemplo (captura de tipo de exceção NameError)

try:
    num = eval(input('Entre com um número inteiro: '))
    print(num)
except NameError:
    print('Entre com o valor numérico e não letras')


# Captura de exceção de múltiplos tipos
# Suponha que, durante a execução, o usuário entre com a palavra “numero” quando solicitado:
# Como o usuário inseriu uma palavra, e não um número, a exceção não será do tipo ValueError nem do tipo IndexError. Assim, a cláusula except a ser executada é a da linha 8, imprimindo Mensagem 3.

try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")


# Verifique se uma entrada é numérica e que, além disso, insita que o usuário digite um número válido

while True:
    try:
        x = int(input('Digite um numero: '))
        break
    except ValueError:
        print('Entre com um numero valido.')


# Implemente uma solução que faça o tratamento de exceção de divisão por zero

def dividir(x, y):
    try:
        resultado = x / y
        print('O resultado é: ', resultado)
    except ZeroDivisionError:
        print('Divisão por zero')
