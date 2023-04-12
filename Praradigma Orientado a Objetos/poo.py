
# Propriedades da POO

# Abstração: Modelo reduzido (descrever o problema)

# Encapsulamento: Restringe o acesso a métodos e atributos em uma classe. Em Python, isso é obtido usando métodos ou atributos privados usando sublinhado como prefixo,
#                   ou seja, "_" simples ou duplo "__"

# Herança: Permite definir uma classe que herda todos os métodos e atributos de outra classe (útil para a reutilização de código)

# Polimorfismo: Permite usar uma única interface com diferentes formas (mesmas funções com comportamentos diferentes, por exemplo)

class Pessoa:
    def __init__(self, nome, ender):  # nesse exemplo, o parâmetro self (obrigatório) de auto referência, para através dele acessar os atributos e métodos da classe
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        # atribuição para um atributo da própria classe, pois inicialmente NOME é apenas um parâmetro, mas agora será um atributo da classe. É escrito dessa forma, "self.(parametro)"
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):  # enquanto o set é responsável pelas atribuições, o get é responsável por retornar o atributo da classe (encapsulamento)
        return self.nome

    def get_ender(self):
        return self.ender


pessoa1 = Pessoa('maria', 'rua 01234')  # instanciar a classe
pessoa2 = Pessoa('joao', 'rua56789')  # instanciar a classe

print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')
