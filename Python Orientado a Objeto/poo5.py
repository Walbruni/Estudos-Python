
# Atributos de classe

# Existem algumas situações em que os sistemas precisam controlar valores associados à classe, e não aos objetos (instâncias) das classes.
# É o caso, por exemplo, ao se desenvolver um aplicativo de desenho, como o Paint, que precisa contar o número de círculos criados na tela.

# utilizado no final do arquivo, na parte de estudo de METODOS ESTATICOS !!
import datetime
import math


class Circulo():
    _total_circulos = 0  # inicializado antes do __init__, trata-se de uma variavel de classe, ou seja, terá valor unico para todos os objetos da classe

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        # o valor da variavel de classe a cada instanciação de um objeto da classe Circulo é atualizado
        self._total_circulos += 1

# Para que o acesso a variavel de classe nao seja permitido, deve-se colocar a variavel com o atributo privado atraves do underscore '_'


# Métodos de classe

# Os métodos de classe são a maneira indicada para se acessar os atributos de classe. Eles têm acesso diretamente à área de memória que contém os atributos de classe.

class Circulo():
    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos += 1

    @classmethod  # utilizado para definir um metodo como estatico
    def get_total_circulos(cls):  # parametro cls criado como referencia para a classe
        return cls._total_circulos


# Métodos publicos e privados

# As mesmas regras definidas para atributos são válidas para os métodos das classes. Desse modo, o método pode ser declarado como privado, mesmo que ainda possa ser chamado diretamente como se fosse um método público.
# Os dois underscores antes do método indicam que ele é privado

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    # definido como privado, só pode ser acessado apenas internamente pela classe Conta
    def __gerarsaldo(self):
        print(f'Numero: {self.numero} Saldo: {self.saldo}')


# Métodos estáticos

# São métodos que podem ser chamados sem haver uma referência para um objeto da classe, ou seja, não existe a obrigatoriedade da instanciação de um objeto da classe.
# O método pode ser chamado diretamente
# Pertencem à classe e não ao objeto, dessa forma são compartilhados com todos os objetos do ambiente
# Definidos, por padrão, antes do init


class Math:

    @staticmethod
    def sqrt(x):
        # O método sqrt da classe Math foi chamado sem que um objeto da classe Math fosse instanciado.
        return math.sqrt(x)

# Atenção!
# Os métodos estáticos não são uma boa prática na programação orientada a objetos. Eles devem ser utilizados apenas em casos especiais, como o de classes de log em sistemas.


# Exemplo de atributos estáticos:

class Pessoa:
    _contador = 0  # atributo estatico, todas as pessoas irao compartilhar o mesmo contador

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1  # incrementado o contador da classe

    def imprimir(self):
        print(self.nome, 'tem', self.idade, 'anos')

    @property  # o @ são decorações, metadados associados à classe. O compilador injeta determinados comportamentos
    def contador(self):
        # o type(self) funciona como um atalho à Pessoa
        return type(self)._contador


p1 = Pessoa('Lucas', 29)
print(p1.contador)  # ambos incrementam o contador
print(Pessoa._contador)  # ambos incrementam o contador


# Exemplo de métodos da classe e de método estático:

class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # pertence a classe, mas ganha uma referencia para a classe (cls)
    # padrões factory - cria objeto a partir de uma determinada informação
    @classmethod  # método da classe
    def fromString(cls, texto):
        nome, sobrenome = map(str, texto.split(' '))
        objeto = cls(nome, sobrenome)  # cls = NomeCompleto
        return objeto

    @staticmethod  # método estático
    def isValid(texto):
        # metodo split serve para dividir em varias palavras
        nomes = texto.split(' ')
        # caso na lista de palavras tenham 'nome' e 'sobrenome', nesse caso será válido (isValid) usar
        return len(nomes) > 1


# o nome é dividido em 2, chama o construtor cls e retorna um objeto da classe
registro1 = NomeCompleto.fromString('Lucas Walbruni')


# Agregação (caso exclua um, o outro continua existindo) Cliente - Conta

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        # construção de um objeto. Se acabar com a conta, acaba tambem com o extrato
        self.extrato = Extrato()  # COMPOSIÇÃO

    def depositar(self, valor):
        self.saldo += valor
        # utilizando a lista de transações criada na classe Extrato
        self.extrato.transacoes.append(['DEPOSITO', valor])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            # utilizando a lista de transações criada na classe Extrato
            self.extrato.transacoes.append(['SAQUE', valor])
            return True


# Composição: objeto gerado dentro de outro objeto (caso exclua, o outro deixa de existir) Conta - Extrato


class Extrato:
    def __init__(self):
        self.transacoes = []

    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])


class ContaEspecial(Conta):
    # atributo limite foi implementado apenas na subclasse ContaEspecial
    def __init__(self, clientes, numero, saldo, limite):
        # em herança simples pode-se usar a palavra super() para fazer referencia à classe Pai. Porém não é válido para heranças múltiplas
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        # método para verificar se o valor sacado é menor que a soma do saldo atual mais o limite da conta especial
        if (self.saldo + self.limite) < valor:
            return print(f'Valor do saque maior que o valor disponivel {self.saldo}')
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['SAQUE', valor])
            return print('Saque realizado com sucesso')


class Poupanca:  # herança múltipla
    def __init__(self, taxaRemuneracao):
        self.taxaRemuneracao = taxaRemuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneraConta(self):
        self.saldo += self.saldo * self.taxaRemuneracao


class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxaRemuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxaRemuneracao)

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaRemuneracao/30)
        self.saldo -= self.taxaRemuneracao


c1 = Cliente('121212121-12', 'Lucas', 'Rua X')
c2 = Cliente('434343434-34', 'Joao', 'Rua YZ')

# os clientes não são dependentes da conta, foram AGREGADOS a ela
conta = Conta([c1, c2], 123212, 2500)
# caso exclua a conta, os clientes continuarão

conta.depositar(1000)
conta.sacar(500)
conta.extrato.imprimir()

cx = ContaRemuneradaPoupanca([c1, c2], 9893123, 1500.00, 0.03)
cx.remuneraConta()
print(cx.saldo)
