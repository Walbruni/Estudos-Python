
# O metodo range() pode ser Simples, no qual a sequencia sera iniciada no 0 ate o limite do parametro passado (excluindo o ultimo numero). Ex: range(3): (0,1,2)
# Pode ser Não iniciadas em 0, no qual se passa o parametro de inicio e o fim. Ex: range(2,7): (2,3,4,5,6)
# Pode indicar o inicio, fim e o passo, no qual o passo é o valor que será incrementado de um para o outro. Ex: range(2,9,3): (2,5,8)

for item in range(2, 9, 3):
    print(item)

# Exemplo do laço for com uma string

nome = input("Entre com seu nome: ")

for letra in nome:
    print(letra)


# Estrutura de repetição while

palavra = input("Digite uma palavra: ")

while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: ')

print('Você digitou a palavra sair e agora está fora do laço')


# Instrução break em laço while infinito

while True:
    palavra = input('Entre com uma palavra: ')
    if palavra == 'sair':
        break

print('Você digitou sair e agora está fora do laço')


# Instrução break com vários laços aninhados

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso:')
    if opcao1 == 'SIM':
        break  # esse break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso:')
            if opcao2 == 'SIM':
                break  # esse break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço.')


# Instrução continue interrompe apenas a iteração corrente, fazendo com que o laço passe para a próxima iteração

for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado.')


# Exemplo de estratégia para utilização de condicionais
# Qual dos valores é maior

a = 10
b = 20
maior = a

if (b > maior):
    maior = b

print(f'O maior número é: {maior}')


# Exemplo para verificar se um número é par ou ímpar

numero = 46

if (numero % 2 == 0):
    situacao = "O número é par"
else:
    situacao = 'O número é ímpar'

print(situacao)


# Exercicio condicional com calculo de media

media = 8.5

if (media >= 7.0):
    resultado = "aprovado"
elif (media >= 5.0):
    resultado = "recuperação"
else:
    resultado = "reprovado"

print(f'O estudante está: {resultado}')


# Exercicio condicional com valores e descontos
# Calcule o valor da compra sendo que o preco unitario é R$ 10,00. Se a compra for até 10 unidades, nao tem desconto. Se for entre 11 e 20 unidades, 10% desconto. Acima de 20 unidades, é dado 20% de desconto.

preco_unitario = 10

DESCONTO10 = 0.1  # desconto de 10%

DESCONTO20 = 0.2  # desconto de 20%

quantidade = eval(input("Digite a quantidade que vai comprar: "))

if (quantidade <= 10):
    valor_final = preco_unitario*quantidade
elif (quantidade <= 20):
    valor_final = preco_unitario*quantidade*(1-DESCONTO10)
else:
    valor_final = preco_unitario*quantidade*(1-DESCONTO20)

print(f'O valor final da compra é: {valor_final}')


# Exercicio com estrutura de repetição
# Implemente uma solução em Python que some todos os números pares de uma lista

lista = [10, 2, 5, 7, 6, 3]

soma = 0  # variavel criada para acumular os valores

for num in lista:
    if (num % 2 == 0):
        soma = soma + num

print(f'O somatório dos elementos pares da lista é: {soma}')
