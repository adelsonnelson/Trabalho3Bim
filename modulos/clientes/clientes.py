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
    
    if nome and email:
        objeto = Cliente(nome, email)
        db.session.add(objeto)
        db.session.commit()
        flash('Cliente salvo com sucesso!!!')
        return redirect('/clientes')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/clientes/add')

@bp_cliente.route("/remove/<int:id>")
def remove(id):
    c = Cliente.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("Cliente removido!!!")
    except:
        flash("Cliente Inválido!!!")
    return redirect("/clientes")


@bp_cliente.route("/edit/<int:id>")
def edit(id):
    c = Cliente.query.get(id)
    return render_template("cliente_edit.html", dados=c)


@bp_cliente.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    id = request.form.get("id")
    if nome and email and id:
        c = Cliente.query.get(id)
        c.nome = nome
        c.email = email
        db.session.commit()
        flash("Dados atualizados!!!")
    else:
        flash("Preencha todos os campos!!!")
    return redirect("/clientes")
