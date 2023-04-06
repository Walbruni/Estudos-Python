

class ContaCliente:
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestido = valorInvestido
        self.taxaRendimento = taxaRendimento

    def calculaRendimento(self):  # 1
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)
        self.valorInvestido = (self.valorInvestido -
                               (self.taxaRendimento * self.IOF * self.IR))

    def extrato(self):
        print(
            f'O saldo atual da conta {self.numero} é {self.valorInvestido:10.2f}')


class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def calculaRendimento(self):  # 2
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)


class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def calculaRendimento(self):  # 3
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)
        self.valorInvestido -= self.valorInvestido * self.IOF
