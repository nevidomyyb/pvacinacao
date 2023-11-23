from db import db
from models import Bairro
class PontoVacinacao(db.Model):
    __tablename__ = 'ponto_vacinacao'

    idpontovacinacao = db.Column(db.String(36), primary_key=True)
    nome = db.Column(db.String(248), nullable=False, unique=True)
    bairro = db.Column(db.Enum(Bairro), nullable=False)
    endereco = db.Column(db.String(248), nullable=False)
    horario_expediente = db.Column(db.String(248), nullable=False)
    faixa_etaria = db.Column(db.String(248), nullable=False)
