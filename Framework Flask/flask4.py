
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Página inicial'


@app.route('/ola/<nome>')
def ola_mundo(nome):
    return 'Olá, ' + nome


if __name__ == '__main__':
    app.run()


# a rota <nome> é o mesmo do parametro passado na função (nome)
# isso indica que qualquer valor que for adicionado a URL após '/ola/...' será passado como argumento para o parametro nome da função ola_mundo
# entretanto, ao acessar a rota '/ola' ocorrerá o erro 404 (not found)
