
# Encapsulamento
# Atributos publicos e privados

# Properties (Propriedade)

# Utilizando o decorator property nos métodos, mantém-se os atributos como protegidos, os quais, por sua vez, são acessados apenas por meio dos métodos “decorados” com property (CAELUM, 2020).
# Os properties ajudam a garantir o encapsulamento no Python

# DICA: Uma boa prática implementada em todas as linguagens orientadas a objetos será a de definir esses métodos apenas se realmente houver regra de negócios diretamente associada ao atributo. Caso não haja, deve-se deixar o acesso aos atributos conforme definido na classe.

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (self.saldo < 0):
            print('saldo inválido')
        else:
            self._saldo = saldo


def main():
    conta = Conta(1)
    conta.saldo = 1000  # usando o @saldo.setter
    print(f'Saldo da conta: {conta.saldo}')  # usando o @property


if __name__ == '__main__':
    main()
