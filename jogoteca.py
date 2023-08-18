from flask import Flask, render_template, request, redirect, session, flash, url_for       #request é pra pegar informações do formulário, redirect é pra fazer redirecionamento
#session permite manter as informações através dos cookies do navegador
#flash é pra mostrar mensagens rápidas
from flask_sqlalchemy import SQLAlchemy
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Leonardo', 'lzn', '123')
usuario2 = Usuario('Camila', 'mila', '1234')
usuario3 = Usuario('Guilherme', 'gui', '12345')

usuarios = {
    usuario1.nickname : usuario1,     #o objeto pra acessar o usuario1 vai ser o nickname
    usuario2.nickname : usuario2,
    usuario3.nickname : usuario3
}

app = Flask(__name__)
app.secret_key = 'alura'     #secret_key pra funcionar a autenticação, assinatura criptografica aos cookies


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/jogoteca'
db = SQLAlchemy(app)

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Usuario(db.Model):
    nome = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(8), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)   #pra referenciar a página html

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:   #verificar se tem algum usuario logado, se não tiver vai pro login
        return redirect(url_for('login', proxima=url_for('novo')))   #se o usuario tentar acessar a novo sem autenticar, ele vai criar um parametro de proxima página e dps q o usuario logar vai pro novo
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']      #id do html
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))       #coloca a função que instancia a página

@app.route('/login')
def login():
    proxima = request.args.get('proxima') #pegando o argumento do proxima=novo pra caso tiver
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso')
            proxima_pagina = request.form['proxima']
            if proxima_pagina and proxima_pagina != "None":
                return redirect(proxima_pagina)
            else:
                return redirect(url_for('index'))
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login')) #coloca a função que instancia a página

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)