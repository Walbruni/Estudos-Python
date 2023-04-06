from clientes import Cliente
from contas import Conta
from contaespecial import ContaEspecial
from poupanca import Poupanca
from contaremunerada import ContaRemuneradaPoupanca


cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
cliente3 = Cliente('789', 'Lucas', 'Rua Z')
cliente4 = Cliente('103', 'Manu', 'Rua A')
conta1 = Conta([cliente1], 1, 0)
conta2 = Conta([cliente2], 2, 1000)
conta3 = ContaEspecial([cliente3], 3, 1000, 2000)
conta4 = ContaRemuneradaPoupanca([cliente4], 4, 1000, 0.1)
conta1.extrato.extrato(conta1.numero)
conta1.depositar(300)
conta1.sacar(2)
conta2.transfereValor(conta3, 100)
conta1.gerarsaldo()
conta2.extrato.extrato(conta2.numero)
conta2.gerarsaldo()
conta3.extrato.extrato(conta3.numero)
conta3.sacar(200)
conta3.gerarsaldo()
conta4.extrato.extrato(conta4.numero)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = conta4
contaremunerada1.remunera_conta()
contaremunerada1.gerarsaldo()
