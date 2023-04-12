
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Página inicial'


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'Olá, ' + nome


if __name__ == '__main__':
    app.run()


# adicionamos duas rotas para a mesma função. Em qualquer das URL, o usuário será direcionado para a função ola_mundo
# a rota '/ola/' agora aparecera normalmente
# a rota '/ola/' aceita requisições tanto para '/ola' quanto '/ola/'
