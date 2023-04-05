
class ContaTeste:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Transferência realizada')

    def gerar_saldo(self):
        print(f'numero: {self.numero}, saldo: {self.saldo}')
