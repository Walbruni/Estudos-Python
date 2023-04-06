
from contas import Conta
from poupanca import Poupanca


class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxaRemuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxaRemuneracao)
        self.taxaRemuneracao = taxaRemuneracao

    def remunera_conta(self):
        self.saldo += self.saldo * (self.taxaRemuneracao/30)
        self.saldo -= self.taxaRemuneracao
