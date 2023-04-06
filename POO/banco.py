from tiposcontas import ContaComum
from tiposcontas import ContaCliente
from tiposcontas import ContaRemunerada


class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaConta(self, contaCliente):
        self.contas.append(contaCliente)

    def calculaRendimentoMensal(self):
        for c in self.contas:
            c.calculaRendimento()

    def imprimeSaldoContas(self):
        for c in self.contas:
            c.extrato()


banco1 = Banco(999, 'Banco do Estado')
contacliente1 = ContaCliente(1, 0.01, 0.01, 1000, 0.05)
contacomum1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
contaremunerada1 = ContaRemunerada(3, 0.01, 0.1, 2000, 0.5)

banco1.adicionaConta(contacliente1)
banco1.adicionaConta(contacomum1)
banco1.adicionaConta(contaremunerada1)

banco1.calculaRendimentoMensal()
banco1.imprimeSaldoContas()
