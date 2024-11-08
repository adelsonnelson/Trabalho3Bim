from database import db

class Cliente(db.Model):
    __tablename__='cliente'
    id = db.Column(db.Integer, primary_key = True) #o Primary key torna ele auto-incremment e chava primária
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email

    def __repr__(self):    
        return "<Cliente {}>".format(self.nome)


class Conta(db.Model):
    __tablename__='conta'
    id = db.Column(db.Integer, primary_key = True)
    saldo = db.Column(db.Float)
    tipo_conta = db.Column(db.String(50))
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    

    usuario = db.relationship('Usuario', foreign_keys = usuario_id)


    
    def __init__(self, sabor, ingredientes, preco):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preco = preco

    def __repr__(self):
        return "<Conta {}>".format(self.sabor)
        
