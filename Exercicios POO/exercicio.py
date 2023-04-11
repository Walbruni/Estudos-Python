
# Exercicio 1
# Implemente um programa para criar uma classe Veiculo com atributos de instancia "velocidade maxima" e "quilometros percorridos por litro"

class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

    def imprimir(self):
        print(f'Nome = {self.nome}')
        print(f'Velocidade maxima = {self.velocidade_max}')
        print(f'Quilometros percorridos por litro = {self.quilometro_litro}')


modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.imprimir()


# Crie uma classe filha "Onibus" que herdara todas as variaveis e metodos (caracteristicas) de Veiculo

class Onibus(Veiculo):
    pass


onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.imprimir()


# Modifique a classe filha "Onibus", de modo que ela fornece a quantidade de assentos. Alem disso, o valor desse parametro deve ser 70.

class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

    def capacidade_assentos(self, capacidade):  # incluido um novo metodo
        print(
            f'A capacidade maxima de assentos do veiculo {self.nome} é {capacidade}')  # capacidade como parametro do proprio metodo, e nao um atributo da classe

    def imprimir(self):
        print(f'Nome = {self.nome}')
        print(f'Velocidade maxima = {self.velocidade_max}')
        print(f'Quilometros percorridos por litro = {self.quilometro_litro}')


modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.imprimir()


class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade=70):
        return super().capacidade_assentos(capacidade=70)


onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.imprimir()
onibus_escolar.capacidade_assentos()
