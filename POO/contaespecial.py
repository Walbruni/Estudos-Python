
import datetime
from contas import Conta


class ContaEspecial(Conta):
    # atributo limite foi implementado apenas na subclasse ContaEspecial
    def __init__(self, clientes, numero, saldo, limite):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        # método para verificar se o valor sacado é menor que a soma do saldo atual mais o limite da conta especial
        if (self.saldo + self.limite) < valor:
            return print(f'Valor do saque maior que o valor disponivel {self.saldo}')
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['SAQUE', valor, 'Data', datetime.datetime.today()])
            return print('Saque realizado com sucesso')
