
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Página inicial'


@app.route('/ola')
def ola_mundo():
    return 'Olá mundo!'


if __name__ == '__main__':
    app.run()


# agora possui uma rota raiz '/' que retorna 'pagina inicial' e a rota '/ola' que retorna 'ola mundo'
