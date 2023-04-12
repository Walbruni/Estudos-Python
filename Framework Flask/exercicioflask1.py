
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    boas_vindas = '<h1>Olá, programdores!</h1>'
    link = '<p><a href="user/Usuário">Clique Aqui!</a></p>'
    return boas_vindas + link


@app.route('/user/')
@app.route('/user/<nome>')
def user(nome='Usuário'):
    personalizar = f'<h1>Olá, {nome}!</h1>'
    instrucao = '<p>Altere o nome no <em>endereço do browser</em> e recarregue a página.</p>'
    return personalizar + instrucao


if __name__ == '__main__':
    app.run(debug=True)


# também é possível digitar o código html no próprio arquivo flask
