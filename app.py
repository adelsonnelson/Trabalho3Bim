from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'QualquerCoisa'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/bancodedados'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Cliente, Conta

from modulos.clientes.clientes import bp_cliente
app.register_blueprint(bp_cliente, url_prefix='/clientes')

from modulos.contas.contas import bp_contas
app.register_blueprint(bp_contas, url_prefix='/contas')

@app.route('/')
def index():
    return render_template('ola.html')