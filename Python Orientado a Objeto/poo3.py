
# Classe

from datetime import date


class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo


def main():
    c1 = Conta(1, 1323404, 'Lucas', 1000)  # objeto sendo instanciado
    print(f'Nome do titular da conta: {c1.nomeTitular}')
    print(f'Numero da conta: {c1.numero}')
    print(f'CPF do titular da conta: {c1.cpf}')
    print(f'Saldo da conta: {c1.saldo}')


# Quando um script python é executado, a variável reservada NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso, é um chamado ao método main do script.
if __name__ == '__main__':
    main()


# Outro exemplo do uso de método

class ContaBancaria:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def gerar_extrato(self):
        print(f'numero: {self.numero}, cpf: {self.cpf}, saldo: {self.saldo}')


def main2():
    c2 = ContaBancaria(1, 232321, 'Lucas', 0)
    c2.depositar(300)
    c2.sacar(100)
    c2.gerar_extrato()


if __name__ == '__main__':
    main2()


# Métodos com retorno

class OutraConta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f'numero: {self.numero}, cpf: {self.cpf}, saldo: {self.saldo}')


def main3():
    c3 = OutraConta(1, 23444, 'Lucas', 0)
    c3.depositar(400)
    saque = c3.sacar(100)
    c3.gerar_extrato()
    print(f'O saque foi realizado? {saque}')


if __name__ == '__main__':
    main3()


# Agragação (utilizado em sistemas bancários, por exemplo. Conta corrente, conta conjunta)


class Salario:
    def __init__(self, base, bonus):
        self.base = base  # parametros passados como atributos
        self.bonus = bonus  # parametros passados como atributos

    def salario_anual(self):
        return (self.base*12) + self.bonus


class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        # agregação (instancia da classe Salario)
        self.salario_agregado = salario
        # salario_agregado é um atributo do tipo salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()


# 10000 e 700 sao os parametros passados para o construtor (__init__) instanciados na classe Salario
salario = Salario(10000, 700)
emp = Empregado('Lucas', 29, salario)
# nao precisa de parametros pois esta dentro da classe que ja possui atributos / valores
print(emp.salario_total())


# Método de Classe x Método Estático

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # método de classe para criar um objeto Pessoa através do ano do nascimento
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)  # retorna a classe Pessoa

    @staticmethod  # método estático para verificar se é maior de idade
    # não recebe "self" nem "cls", pois esse método estático ele não é dependente do estado da classe, não está relacionado a um objeto especificamente, mas sim geral
    def ehMaiorIdade(idade):
        return idade >= 18


pessoa1 = Pessoa('maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)
print(Pessoa.ehMaiorIdade(17))
