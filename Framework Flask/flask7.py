
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('indice.html')


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'Olá, ' + nome


if __name__ == '__main__':
    app.run()


# Para criar e utilizar os templates, os html precisam estar dentro da pasta templates, no mesmo nivel do arquivo que contem a aplicacao Flask
# o conteudo do modelo indice.html sera exibido

# as funções no Flask precisam retornar algo!
# a funcao render_template, disponibilizada pelo Flask, é quem recebe o nome do arquivo que desejamos retornar
