
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    instrucao = '<p>Digite dois números no endereço do browser na rota /somar!</p>'
    return boas_vindas + instrucao


@app.route('/somar/')
@app.route('/somar/<num01>/<num02>')
def soma(num01=0, num02=0):
    resultado = float(num01) + float(num02)
    return str(resultado)


if __name__ == '__main__':
    app.run(debug=True)
