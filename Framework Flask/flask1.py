
from flask import Flask

app = Flask(__name__)  # criado uma instancia de classe Flask, que recebe __name__ como argumento para que o Flask consiga localizar, na aplicação, arquivos estaticos como css e javascript e arquivos de modelo (templates), se for o caso


# uso de rotas para direcionar o acesso as paginas (endpoints). As rotas servem para guiar as requisições feitas ao servidor para o trecho de código que deve ser executado. Os nomes das rotas são os nomes utilizados pelo usuário para navegar na sua aplicação.
@app.route('/')  # decorator que espera como parametro a rota (URL)
def ola_mundo():  # toda requisição feita para uma rota é encaminhada para essa função
    return 'Olá mundo!'  # o retorno é a resposta que o nosso servidor enviará ao usuário


if __name__ == '__main__':
    # Ao iniciar a execução do script, recebemos no console algumas informações, incluindo em qual endereço o servidor está “escutando”.
    app.run()
