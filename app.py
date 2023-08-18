from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy #tratar o banco de dados
import json
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/jogoteca'

db = SQLAlchemy(app)
class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

class Usuario(db.Model):
    nome = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(8), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()
