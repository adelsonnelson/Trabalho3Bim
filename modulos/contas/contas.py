from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Conta, Cliente

bp_contas = Blueprint('contas', __name__, template_folder="templates")

@bp_contas.route('/')
def index():
    dados = Conta.query.all()
    return render_template('contas.html', dados = dados)

@bp_contas.route('/add')
def add():
    c = Cliente.query.all()
    return render_template('contas_add.html', clientes=c)

@bp_contas.route('/save', methods= ['POST'])
def save():
    saldo = request.form.get('saldo')
    tipo_conta = request.form.get('tipo_conta')
    cliente_id = request.form.get('cliente_id')
    
    cliente = Cliente.query.all()

    if saldo and tipo_conta and cliente_id:
        objeto = Conta(saldo, tipo_conta, cliente_id)
        db.session.add(objeto)
        db.session.commit()
        flash('Conta salva com sucesso!!!')
        return redirect('/contas')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/contas/add')

@bp_contas.route("/remove/<int:id>")
def remove(id):
    C = Conta.query.get(id)
    try:
        db.session.delete(C)
        db.session.commit()
        flash("Conta removida!")
    except:
        flash("Conta Inválida!")
    return redirect("/contas")

@bp_contas.route("/edit/<int:id>")
def edit(id):
    C = Conta.query.get(id)
    c = Cliente.query.all()
    return render_template("contas_edit.html", dados=C, clientes=c)

@bp_contas.route("/edit-save", methods=['POST'])
def edit_save():
    saldo = request.form.get("saldo")
    tipo_conta = request.form.get("tipo_conta")
    cliente_id = request.form.get("cliente_id")
    id = request.form.get("id")
    if saldo and tipo_conta and cliente_id and id:
        C = Conta.query.get(id)
        C.saldo = saldo
        C.tipo_conta = tipo_conta
        C.cliente_id = cliente_id
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/contas")
