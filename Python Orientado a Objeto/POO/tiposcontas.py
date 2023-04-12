

class ContaCliente:
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestido = valorInvestido
        self.taxaRendimento = taxaRendimento

    def calculaRendimento(self):  # polimorfismo, sera argumentado nos filhos
        pass  # argumento pass para definir que o metodo sera realizado adiante, no caso, a depender de cada filho


class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def calculaRendimento(self):  # 2 Polimorfismo - usara o metodo do filho
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)


class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def calculaRendimento(self):  # 3 Polimorfismo - usara o metodo do filho
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)
        self.valorInvestido -= self.valorInvestido * self.IOF
