from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Conta

bp_contas = Blueprint('contas', __name__, template_folder="templates")

@bp_contas.route('/')
def index():
    dados = Conta.query.all()
    return render_template('contas.html', dados = dados)

@bp_contas.route('/add')
def add():
    return render_template('contas_add.html')

@bp_contas.route('/save', methods= ['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preço = request.form.get('preço')
    
    if sabor and ingredientes and preço:
        objeto = Conta(sabor, ingredientes, preço)
        db.session.add(objeto)
        db.session.commit()
        flash('Conta salvo com sucesso!!!')
        return redirect('/contas')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/contas/add')


