from database import db

class Cliente(db.Model):
    __tablename__='cliente'
    id = db.Column(db.Integer, primary_key = True) #o Primary key torna ele auto-incremment e chava primária
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):    
        return "<Cliente {}>".format(self.nome)


class Conta(db.Model):
    __tablename__='conta'
    id = db.Column(db.Integer, primary_key = True)
    saldo = db.Column(db.Float)
    tipo_conta = db.Column(db.String(50))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    

    cliente = db.relationship('Cliente', foreign_keys = cliente_id)


    
    def __init__(self, saldo, tipo_conta, cliente_id):
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.cliente_id = cliente_id

    def __repr__(self):
        return "<Conta {}>".format(self.saldo)
        
