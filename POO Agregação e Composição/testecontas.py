from clientes import Cliente
from contas import Conta


cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
conta1 = Conta([cliente1], 1, 0)
conta2 = Conta([cliente2], 2, 1000)
conta1.extrato.extrato(conta1.numero)
conta1.depositar(300)
conta1.sacar(250)
conta2.transfereValor(conta1, 100)
conta1.gerarsaldo()
conta2.extrato.extrato(conta2.numero)
conta2.gerarsaldo()
