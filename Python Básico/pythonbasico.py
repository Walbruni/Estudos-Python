curso = 'Ensino a distancia'

print(curso.upper())
print(curso.lower())
print(curso.split())

# O operador + realiza operações de soma para tipos numericos e concatenação para tipos sequenciais
# O operador * realiza operações de multiplicação para tipos numericos e concatenação para tipos sequenciais
a = ['U'] + ['RN']
print(a)
print(len(a))

b = ['4'] * 4
print(b)
print(len(b))

# É possivel realizar a troca de variáveis da seguinte maneira, sem a necessidade de criar uma terceira variavel

c, d = 1, 2  # pode ser escrito dessa forma
c = 1
d = 2  # ou pode ser escrito dessa forma

c, d = d, c
print(f'O valor da variavel c: {c}')
print(f'O valor da variavel d: {d}')

# Entrada de dados com a função input() para retornar strings e eval() para numeros

nome = input('Digite o seu nome: ')
print(nome)
idade = eval(input('Digite a sua idade: '))
print(idade)

# Formatação de dados de saída

hora = 10
minutos = 26
segundos = 18

print(f'{hora}:{minutos}:{segundos}')

# Imprimir uma sequencia de substrings

str = 'Hello World'
print(str[2:8])

# Imprimir da direita para a esquerda

print(str[::-1])
print(str[8:2:-1])
