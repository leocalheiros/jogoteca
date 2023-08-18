from flask import render_template, request, redirect, session, flash, url_for #request é pra pegar informações do formulário, redirect é pra fazer redirecionamento
from jogoteca import app, db
from models import Jogo, Usuario

#session permite manter as informações através dos cookies do navegador
#flash é pra mostrar mensagens rápidas

@app.route('/')
def index():
    lista = Jogo.query.order_by(Jogo.id)
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

    jogo = Jogo.query.filter_by(nome=nome).first()
    if jogo:
        flash('O jogo já é existente na lista.')
        return redirect(url_for(index))

    novo_jogo = Jogo(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)   #adicionar esse novo jogo no banco de dados
    db.session.commit()         #commitar a adição

    return redirect(url_for('index'))       #coloca a função que instancia a página

@app.route('/editar/<int:id>')   #colocamos o id <id> aqui entre chaves pra ele reconhecer na url
def editar(id):    #instanciamos o id aqui também
    if 'usuario_logado' not in session or session['usuario_logado'] is None:   #verificar se tem algum usuario logado, se não tiver vai pro login
        return redirect(url_for('login'))   #se o usuario tentar acessar a novo sem autenticar, ele vai criar um parametro de proxima página e dps q o usuario logar vai pro novo

    jogo = Jogo.query.filter_by(id=id).first()   #buscar o jogo pelo id instanciado

    return render_template('editar.html', titulo='Editar Jogos', jogo=jogo)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    jogo = Jogo.query.filter_by(id=request.form['id']).first()  #receber o id hidden no html pra ele filtrar por esse id
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:   #verificar se tem algum usuario logado, se não tiver vai pro login
        return redirect(url_for('login'))   #se o usuario tentar acessar a novo sem autenticar, ele vai criar um parametro de proxima página e dps q o usuario logar vai pro novo

    Jogo.query.filter_by(id=id).delete()
    db.session.commit()
    flash(f'O jogo foi deletado!')

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima') #pegando o argumento do proxima=novo pra caso tiver
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Usuario.query.filter_by(nickname=request.form['usuario']).first()  #se ele não achar nenhum valor ele vai retornar uma variável False pra esse usuario
    if usuario:
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

@app.route('/cadastrar-usuario', methods=['GET', 'POST'])
def cadastro():
    if 'usuario_logado' in session and session['usuario_logado'] is not None:  # Verifica se o usuário já está logado
        flash('Você já está logado, por isso não é possível acessar o cadastro.')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nome = request.form['nome']
        nickname = request.form['nickname']
        senha = request.form['senha']

        novo_usuario = Usuario(nome=nome, nickname=nickname, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('login'))

    return render_template('cadastro.html', titulo='Cadastro de Usuário')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))