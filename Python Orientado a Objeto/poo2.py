
# Conceitos e Pilares da Programação Orientada a Objetos

# OBJETOS:
# Um objeto é a representação computacional de um elemento ou processo do mundo real. Cada objeto possui suas características (informações) e uma série de operações (comportamento) que altera as suas características (estado do objeto).
# Todo o processamento das linguagens de programação orientadas a objetos se baseia no armazenamento e na manipulação das informações (estados). São exemplos de objetos do mundo real e computacional: Aluno, Professor, Livro, Empréstimo e Locação.

# ATRIBUTOS:
# São propriedades do mundo real que descrevem um objeto. Cada objeto possui as respectivas propriedades desse mundo, as quais, por sua vez, possuem valores. A orientação a objetos define as propriedades como atributos. Já o conjunto de valores dos atributos de um objeto define o seu estado naquele momento.

# Atributos e valores armazenados:
# Nome: Lucas, Idade: 29, Peso: 62kg, Altura: 1,62.

# OPERAÇÕES:
# Uma operação é uma função ou transformação que pode ser aplicada a objetos ou dados pertencentes a um objeto. É importante dizer que todo objeto possui um conjunto de operações, as quais, aliás, podem ser chamadas por outros objetos com o propósito de colaborarem entre si.
# Esse conjunto de operações é conhecido como interface.
# A única forma de colaboração entre os objetos é por meio das suas respectivas interfaces. Utilizando o exemplo acima, podemos alterar o nome, a idade e o peso da pessoa graças a um conjunto de operações. Desse modo, essas operações normalmente alteram o estado do objeto.
# Classe empresa = Contratar_Funcionario, Despedir_Funcionario; Classe janela = Abrir, fechar, ocultar.


# O desenvolvimento de um sistema orientado a objetos consiste em realizar um mapeamento.
# Basicamente, deve-se analisar o mundo real e identificar quais objetos precisam fazer parte da solução do problema. Para cada objeto identificado, levantam-se os atributos, que descrevem as propriedades dos objetos, e as operações, que podem ser executadas sobre tais objetos.

# Objeto no mundo real (caracteristicas, comportamento) --> Objeto no mundo computacional (atributos, operações)


# CLASSE:
# A classe descreve as características e os comportamento de um conjunto de objetos. De acordo com a estratégia de classificação, cada objeto pertence a uma única classe e possui os atributos e as operações definidos na classe.
# Durante a execução de um programa orientado a objetos, são instanciados os objetos a partir da classe. Assim, um objeto é chamado de instância de sua classe.
# Um programa orientado a objetos consiste basicamente em um conjunto de objetos que colaboram entre si por meio de uma troca de mensagens para a solução de um problema computacional. Cada troca significa a chamada de uma operação feita pelo objeto receptor da mensagem.


# ENCAPSULAMENTO:
# Seu conceito consiste na separação dos aspectos externos (operações) de um objeto acessíveis a outros objetos, além de seus detalhes internos de implementação, que ficam ocultos dos demais objetos.
# Algumas vezes, o encapsulamento é conhecido como o princípio do ocultamento de informação, pois permite que uma classe encapsule atributos e comportamentos, ocultando os detalhes da implementação.
# Métodos Set e Get

# HERANÇA:
# Na orientação a objetos, a herança é um mecanismo por meio do qual classes compartilham atributos e comportamentos, formando uma hierarquia. Uma classe herdeira recebe as características de outra classe para reimplementá-las ou especializá-las de uma maneira diferente da classe pai.
# A herança permite capturar similaridades entre classes, dispondo-as em hierarquias. As similaridades incluem atributos e operações sobre as classes.
# Uma classe pode ser definida genericamente como uma superclasse e, em seguida, especializada em classes mais específicas (subclasses). A herança permite a reutilização de código em larga escala, pois possibilita que se herde todo o código já implementado na classe pai e se adicione apenas o código específico para as novas funcionalidades implementadas pela classe filha.

# HERANÇA SIMPLES:
# A herança é considerada simples quando uma classe herda as características existentes apenas de uma superclasse. A figura adiante apresenta uma superclasse Pessoa, que possui os atributos CPF, RG, Nome e Endereço. Em seguida, a classe Professor precisa herdar os atributos dessa superclasse, além de adicionar atributos específicos do contexto da classe Professor, como titularidade e salário.
# Considerando um sistema acadêmico, a classe Aluno também se encaixaria na hierarquia acima, tornando-se uma subclasse de Pessoa. Entretanto, ela precisaria de outros atributos associados a seu contexto, como curso e Anoprevformatura.

# HERANÇA MULTIPLIA:
# A herança é considerada múltipla quando uma classe herda características de duas ou mais superclasses. Por exemplo, no caso do sistema acadêmico, o docente também pode desejar realizar outro curso de graduação na mesma instituição em que trabalha.
# Ele, portanto, possuirá os atributos da classe Professor e os da classe Aluno. Além disso, também haverá um atributo DescontoProfessor, que será obtido apenas quando houver a associação de professor e aluno com a universidade.
# Para adaptar essa situação no mundo real, deve ser criada uma modelagem de classes. Uma nova subclasse ProfessorAluno precisa ser adicionada, herdando atributos e operações das classes Professor e Aluno. Isso configura uma herança múltipla. Essa nova subclasse deverá ter o atributo DescontoProfessor, que faz sentido apenas para essa classe.


# POLIMORFISMO:
# O polimorfismo é a capacidade de haver o mesmo comportamento diferente em classes diferentes. Uma mesma mensagem será executada de maneira diversa, dependendo do objeto receptor. O polimorfismo acontece quando reimplementamos um método nas subclasses de uma herança.
# Como exemplificado na figura anterior, o comportamento mover() em um objeto instanciado pela classe Aéreo será diferente do mover() em um objeto da classe Terrestre. Um objeto poderá enviar uma mensagem para se mover, enquanto o objeto receptor decidirá como isso será feito.


# Exemplo de herança e polimorfismo

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print(self.nome, "tem", self.idade, "anos")

    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade


p = Pessoa('Lucas', 29)  # instanciar a classe
p.imprimir()


class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)  # super fazendo referencia a classe "pai"
        self.profissao = profissao  # a profissao apenas a nivel de "filho"

    def imprimir(self):
        super().imprimir()  # imprime os atributos do "pai" (nome e idade)
        # enquanto a classe "pai" imprimia apenas nome e idade, o "filho" imprime também a profissao
        print('e trabalha como', self.profissao)


p = Profissional('Lucas', 29, "Programador")  # instanciar a classe
p.imprimir()
