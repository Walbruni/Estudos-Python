
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('indice.html')


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return render_template('ola.html', nome_do_usuario=nome)


if __name__ == '__main__':
    app.run()


# nesse exemplo, desejamos exibir o nome passado via URL na página. Para passar a variável nome para o HTML, precisamos chamar a função render_template com um parâmetro a mais
# 'nome_recebido' é o nome da variavel que está dentro do template
# 'nome' é a variável local da função ola_mundo

# no arquivo ola.html:
# Delimitadores: {{ ... }}, serve para escrever algo no modelo, como o valor de uma variavel
# Declarações: {% ... %}, serve para ser utilizado em laços e condicionantes, por exemplo
