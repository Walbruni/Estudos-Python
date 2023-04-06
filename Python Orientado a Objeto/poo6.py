
# Herança

class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def multiplica(self):
        return self.a * self.b


# Herança (a classe Derivada passou a ter todos os atributos e funções da classe SomaMultiplica). Forma de reaproveitamento de código
class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b

    def dividr(self):
        return self.a / self.b


d = Derivada(10, 20)  # objeto criado para instanciar as classes
print(f'A soma de 10 e 20 é: {d.somar()}')
# Forma de testar se uma classe é ou não derivada de outra
print(issubclass(Derivada, ClasseSomaMultiplica))


# Sobrecarga (Passo importante antes do polimorfismo)

def somar(x, y, z=0):  # caso nao chame o terceiro parâmetro, o valor dele será 0
    return x + y + z


print(somar(20, 30))  # dessa forma é possível passar somente dois parâmetros
print(somar(20, 30, 50))  # ou passar os três parâmetros


# Polimorfismo

class Argentina():
    def capital(self):
        print('Buenos Aires é a capital da Argentina')

    def lingua_oficial(self):
        print('O espanhol é a língua oficial da Argentina')


class Brasil():
    def capital(self):
        print('Brasília é a capital do Brasil')

    def lingua_oficial(self):
        print('O português é a língua oficial do Brasil')


obj_arg = Argentina()
obj_bra = Brasil()

# A variável pais se comporta em determinado momento como obj_arg e em outro como obj_bra
# As classes precisam possuir os mesmos métodos
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()
# Principal comportamento do polimorfismo


# Outro exemplo Polimorfismo

class Veiculo:
    def rodar(self):
        print('Reduz o consumo de combustivel')


class VeiculoEletrico(Veiculo):  # herda da classe Veiculo
    def rodar(self):
        super().rodar()  # o super faz referencia ao construtor da classe Pai e acessa o método rodar() da classe Pai
        print('Esse veiculo utiliza a eletricidade')


veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()


# Exemplo de Exceção (Erros)

x = 10
if x > 5:
    raise Exception(
        'x não pode ser maior do que 5. O valor de x foi de: {}'.format(x))
# a exceção foi criada a partir do raise, ou seja, foi forçado que ocorresse a exceção
# exemplo prático seria o combustível de um carro, para que nao ultrapasse seu limite, seria forçado uma exceção como um alerta
