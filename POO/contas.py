import datetime
from extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataAbertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return print("Não existe saldo suficiente para transferência")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return print("Transferencia Realizada")

    def gerarsaldo(self):
        print(f'Conta: {self.numero} Saldo: {self.saldo}')
