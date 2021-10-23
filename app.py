from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__) 
#A variável app recebe o objeto Flask, essa parte sinaliza que vou usar o flask no meu arquivo principal.
app.secret_key = 'luaprogrammer'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com' ,
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)

mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome,
        self.email = email,
        self.mensagem = mensagem

#Rota HOME, com uma função que não recebe parametro e renderiza o index.html no retorno dela.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"],
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender= app.config.ger("MAIL_USERNAME"),
            recipients= [ 'luanamelissaprogrammer@gmail.com', app.config.ger("MAIL_USERNAME")],
            body= f'''
            
            {formContato.nome} com o e-mail {formContato.email}, tem enviou a seguinte mensagem :
            {formContato.mensagem}

            
            '''
            
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    
    return redirect('/')






if __name__ == '__main__':
    app.run(debug=True) 
    #Vai rodar o arquivo se ele tiver no arquivo principal, ou seja, na main. O debug ativa o modo desenvolvedor e vai fazer com que minha página atualize automaticamente.