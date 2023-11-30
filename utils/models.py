# IMPORTS
from utils.utils import db
from flask_login import UserMixin

# TABELAS
class User(db.Model, UserMixin):
  __tablename__ = "user"
  id = db.Column(db.Integer, unique=True, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  data_nasc = db.Column(db.Date(), nullable=False)
  email = db.Column(db.String(80), unique=True, nullable=False) 
  tel = db.Column(db.Integer, nullable=False)
  senha = db.Column(db.String(80), nullable=False)
  adm = db.Column(db.Boolean, default=False)
  status = db.Column(db.Boolean, default=True)
  
  def __init__ (self, nome, data_nasc, email, tel, senha, adm, status):
    self.nome = nome
    self.data_nasc = data_nasc
    self.email = email
    self.senha = senha
    self.tel = tel
    self.adm = adm
    self.status = status
    
  def __repr__ (self):
    return f'Teste: {self.nome}.'

class Passageiro(db.Model):
  __tablename__ = "passageiro"
  id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, primary_key=True)
  deficiencia = db.Column(db.String(45), nullable=False)
  
  user = db.relationship('User', foreign_keys=id)

  def __init__(self, id, deficiencia):
    self.id = id
    self.deficiencia = deficiencia

  def __repr__(self):
    return f'Passageiro: {self.id}.'

class Motorista(db.Model):
  __tablename__ = "motorista"
  id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, primary_key=True)
  cnh = db.Column(db.Integer, unique=True, nullable=False)
  
  user = db.relationship('User', foreign_keys=id)

  def __init__(self, id, cnh):
    self.id = id
    self.cnh = cnh
    
  def __repr__(self):
    return f'Motorista: {self.id}.'

class Veiculo(db.Model):
  __tablename__ = "veiculo"
  id = db.Column(db.Integer, unique=True, primary_key=True)
  id_moto = db.Column(db.Integer, db.ForeignKey('motorista.id'), unique=True)
  placa = db.Column(db.String(45), nullable=False)
  renavam = db.Column(db.Integer, nullable=False)
  modelo = db.Column(db.String(45), nullable=False)
  marca = db.Column(db.String(45), nullable=False)
  ano = db.Column(db.Integer, nullable=False)
  cor = db.Column(db.String(45), nullable=False)
  
  motorista = db.relationship('Motorista', foreign_keys=id_moto)

  def __init__(self, id_moto, placa, renavam, modelo, cor, marca, ano):
    self.id_moto = id_moto
    self.placa = placa
    self.renavam = renavam
    self.modelo = modelo
    self.marca = marca
    self.ano = ano
    self.cor = cor
    
  def __repr__(self):
    return f'Veículo: {self.id}.'

class Pagamento(db.Model):
  __tablename__ = "pagamento"
  id = db.Column(db.Integer, unique=True, primary_key=True)
  id_pass = db.Column(db.Integer, db.ForeignKey('passageiro.id'))
  tipo = db.Column(db.String(60), nullable=False)
  valor = db.Column(db.Integer, nullable=False)

  passageiro = db.relationship('Passageiro', foreign_keys=id_pass)

  def __init__(self, id_pass, tipo, valor):
    self.id_pass = id_pass
    self.tipo = tipo
    self.valor = valor

  def __repr__(self):
    return f'Pagamento: {self.id}.'

class Viagem(db.Model):
  __tablename__ = "viagem"
  id = db.Column(db.Integer, unique=True, primary_key=True)
  id_pass = db.Column(db.Integer, db.ForeignKey('passageiro.id'))
  id_moto = db.Column(db.Integer) 
  id_pag = db.Column(db.Integer, db.ForeignKey('pagamento.id'))
  id_ve = db.Column(db.Integer)
  embarque = db.Column(db.String(100), nullable=False)
  desembarque = db.Column(db.String(100), nullable=False)
  data_hora = db.Column(db.DateTime, nullable=False)
  aceitacao = db.Column(db.Boolean, default=True)
  status = db.Column(db.Boolean, default=True)

  passageiro = db.relationship('Passageiro', foreign_keys=id_pass)
  pagamento = db.relationship('Pagamento', foreign_keys=id_pag)

  def __init__(self, id_pass, id_moto, id_pag, id_ve, embarque, desembarque, data_hora, aceitacao, status):
    self.id_pass = id_pass
    self.id_moto = id_moto
    self.id_pag = id_pag
    self.id_ve = id_ve
    self.embarque = embarque
    self.desembarque = desembarque
    self.data_hora = data_hora
    self.aceitacao = aceitacao
    self.status = status

  def __repr__(self):
    return f'Viagem: {self.id}.'
