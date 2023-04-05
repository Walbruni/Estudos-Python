from contas import ContaTeste
from clientes import ClienteTeste

cliente1 = ClienteTeste(123, 'Joao', 'Rua 1')
cliente2 = ClienteTeste(345, 'Maria', 'Rua 2')
conta1 = ContaTeste([cliente1, cliente2], 1, 0)
conta1.gerar_saldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerar_saldo()
