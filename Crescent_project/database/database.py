from . import db

class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    tipo_usuario = db.Column(db.String(100), nullable=False)

class Usuario(Info):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)

class Admin(Info):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    nome_responsavel = db.Column(db.String(100), unique=False, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)
    capacidade_maxima_lot = db.Column(db.String(100), unique=False, nullable=False)
    CEP = db.Column(db.String(100), unique=False, nullable=False)
    logradouro = db.Column(db.String(100), unique=False, nullable=False)
    cidade = db.Column(db.String(100), unique=False, nullable=False)
    

class Prop(Info):
    __tablename__ = 'propaganda'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome_empresa = db.Column(db.String(100), unique=False, nullable=False)
    nome_responsavel = db.Column(db.String(100), unique=False, nullable=False)
    razao_social = db.Column(db.String(100), unique=True, nullable=False)
    CNPJ = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)
    tpo_veiculo = db.Column(db.String(100), unique=True, nullable=False)
    caracteristica_veiculo = db.Column(db.String(100), unique=True, nullable=False)

class Patro(Info):
    __tablename__ = 'patrocinador'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome_empresa = db.Column(db.String(100), unique=False, nullable=False)
    nome_responsavel = db.Column(db.String(100), unique=False, nullable=False)
    CNPJ = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)
