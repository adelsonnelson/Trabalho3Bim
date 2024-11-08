from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Cliente

bp_cliente = Blueprint('cliente', __name__, template_folder="templates")

@bp_cliente.route('/')
def index():
    dados = Cliente.query.all()
    return render_template('cliente.html', dados = dados)

@bp_cliente.route('/add')
def add():
    return render_template('cliente_add.html')

@bp_cliente.route('/save', methods= ['POST'])
def save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    if nome and email and senha:
        objeto = Usuario(nome, email, senha)
        db.session.add(objeto)
        db.session.commit()
        flash('Usuario salvo com sucesso!!!')
        return redirect('/clientes')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/clientes/add')


