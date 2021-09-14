from flask import Flask, render_template, redirect

app = Flask(__name__) 
#A variável app recebe o objeto Flask, essa parte sinaliza que vou usar o flask no meu arquivo principal.

#Rota HOME, com uma função que não recebe parametro e renderiza o index.html no retorno dela.
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run() 
    #Vai rodar o arquivo se ele tiver no arquivo principal, ou seja, na main. O debug ativa o modo desenvolvedor e vai fazer com que minha página atualize automaticamente.