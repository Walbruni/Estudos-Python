
# USO DE BIBLIOTECAS PYTHON
# Para calcular as raízes de uma equação de segundo grau: numpy (nome da biblioteca a ser importada no python)

# Para gerar um gráfico / histograma utiliza-se as bibliotecas numpy (para a entrada de listas) e a matplotlib (para a geração do gráfico / histograma)

# Para fazer a importação do módulo desejado usa-se a instrução: import nome_modulo
# Para chamar a função desejada, precedida do nome do módulo, usa-se a instrução: nome_modulo.nome_funcao(parametros)

# USO DE MÓDULOS NATIVOS DO PYTHON
# Uso do módulo math (dedicado a operações matemáticas, porem não permite operações com números complexos) e cálculo da raíz quadrada por meio da função sqrt()

from tkinter import *
import time
import math

x = math.sqrt(5)
print(x)


# Módulo random (usado para geradores de numeros pseudoaleatorios); distribuição de valores reais e função para numeros inteiros e sequencias.

# Módulo smtplib (permite enviar e-mail para qualquer máquina da internet com um serviço de processamento SMTP ou ESMTP)
# Observação: para enviar tal email por meio do gmail, é necessário alterar a configuração de segurança em: Acesso a app menos seguro -> ative a opção Permitir aplicativos menos seguros

# Módulo time (permite diversas funções relacionadas a tempo)
# Módulo datetime e Módulo calendar

a = time.time()
print(f'Local time: {time.ctime(a)}')


# Módulo tkinter (permite a criação de interface gráfica padrão do Python). Criação de janelas com elementos gráficos, como a entrada de dados e botões.


def funcClicar():
    print('Botão pressionado')


janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Minha janela exibida")
texto.pack()

pic = PhotoImage()  # para aparecer alguma imagem, insira o parametro -> file = ""
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

botao = Button(master=janelaPrincipal, text='Cliquei', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()
