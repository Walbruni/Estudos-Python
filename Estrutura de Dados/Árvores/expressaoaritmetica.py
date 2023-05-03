
# Nó de uma árvore que representa um operador não é uma folha
# Nó de uma árvore que representa um operando é uma folha

# considere a expressao aritmetica A + B * C


# prefixo
# visita a raiz
# percorre as subarvores esquerda em prefixo
# percorre as subarvores direita em prefixo

def prefixa(raiz):
    if raiz:
        print(raiz.chave)
        prefixa(raiz.esquerda)
        prefixa(raiz.direita)

# resultado prefixo: + A * B C


# infixo
# percorre a subarvore esquerda em ordem simetrica (infixo)
# visita a raiz
# percorre a subarvore direita em ordem simetrica (infixo)

def infixo(raiz):
    if raiz:
        infixo(raiz.esquerda)
        print(raiz)
        infixo(raiz.direita)

# resultado infixo: A + B * C


# posfixo
# percorre a subarvore esquerda em posfixo
# percorre a subarvore direita em posfixo
# visita a raiz

def posfixo(raiz):
    if raiz:
        posfixo(raiz.esquerda)
        posfixo(raiz.direita)
        print(raiz.chave)

# resultado posfixo: A B C * +
