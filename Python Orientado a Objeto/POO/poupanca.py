
import datetime


class Poupanca:  # herança múltipla
    def __init__(self, taxaRemuneracao):
        self.taxaRemuneracao = taxaRemuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneracao_conta(self):
        self.saldo += self.saldo * self.taxaRemuneracao
