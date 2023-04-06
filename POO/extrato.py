
# Composição

# A classe extrato tem a responsabilidade de armazenar todas as transações realizadas na conta e de conseguir imprimir um extrato com a lista dessas transações

class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print(f'Extrato: {numeroconta}')
        for p in self.transacoes:
            print(p[0], p[1])
