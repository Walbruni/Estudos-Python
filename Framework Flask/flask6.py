
from flask import Flask, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Página Inicial'


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'Olá, ' + nome


# para metodos HTTP, é necessário utilizar o parametro methods do decorator @app.route(), que espera uma lista de strings com o nome dos métodos aceitos
@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return 'Recebeu post! Fazer login!'
    else:
        return 'Recebeu get! Exibir FORM de login'


if __name__ == '__main__':
    app.run()


# as aplicações web disponibilizam os seguintes métodos para acessar uma URL: GET, POST, PUT e DELETE
# Atenção: Por padrão, as rotas do Flask somente respondem as requisições GET !!
# Para responder a outros métodos, é necessário explicitar, na rota, quais métodos serão aceitos

# Caso seja requisitada uma rota que exista, porém o método não seja aceito pela rota, o erro retornado é o 405 – Method Not Allowed (método não permitido), e não o 404 – Not Found (não encontrado), como ocorre quando a rota não existe.
