
# declaração do array
nomes = ["Joao", "Maria", "Ana"]
print(nomes)

# para acessar um elemento diretamente (por meio do seu indice)
x = nomes[2]
print(x)

# para saber o tamanho da lista
x = len(nomes)
print(x)

# iterando sobre a lista (percorrendo elemento por elemento)
for x in nomes:
    print(x)

# inserção de Gustavo ao final do array
nomes.append('Gustavo')
print(nomes)

# remoção de Joao
nomes.remove('Joao')
print(nomes)

# remoção do elemento do array por meio do seu índice
nomes.pop(2)
print(nomes)
