from flask import Flask, render_template, request, redirect, session, flash, url_for       #request é pra pegar informações do formulário, redirect é pra fazer redirecionamento
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')   #passando as configurações pra cá do arquivo config.py

db = SQLAlchemy(app)


from routes import *

if __name__ == '__main__':
    app.run(debug=True)