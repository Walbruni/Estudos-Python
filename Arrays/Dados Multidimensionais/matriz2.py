
# declarando matriz como lista
# declaracao da matriz compras que possui o produto / seu preco / sua quantidade
compras = [['arroz', 6], ['feijao', 5, 1], ['carne', 50, 2]]
print(compras)

# insercao de um elemento ao final da matriz
compras.append(['cebola', 5, 1])
print(compras)

# insercao de um valor para um elemento na matriz (nesse caso, a quantidade 2 ao arroz)
compras[0].append(2)
print(compras)

# remocao de um elemento da matriz
compras.remove(['feijao', 5, 1])
print(compras)

# para remover um elemento de nivel da matriz
compras[1].remove(50)
print(compras)

# remocao de um elemento da matriz por meio do seu indice
compras.pop(2)
print(compras)

# tambem permite a remocao de elemento de nivel por meio do indice
compras[0].pop(1)
print(compras)

# iteracao para imprimir a lista linha a linha
for x in compras:
    print(x)

# iteracao para imprimir cada elemento em uma linha
for x in compras:
    for y in x:
        print(y)

# para checar se o item de alto nivel é uma lista
for x in compras:
    if isinstance(x, list):
        for y in x:
            print(y)
    else:
        print(x)
