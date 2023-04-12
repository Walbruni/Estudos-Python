
from flask import Flask

app = Flask(__name__)


@app.route('/ola')
def ola_mundo():
    return 'Olá mundo!'


if __name__ == '__main__':
    app.run()


# a alteração realizada foi a implementação da rota '/ola'
# ao rodar o servidor, aparecerá o erro de codigo 404 (not found), pois o retorno da função nao esta mais na rota raiz '/', e sim na '/ola'
