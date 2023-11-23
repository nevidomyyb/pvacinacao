from marshmallow import Schema, fields
from models import Bairro, PontoVacinacao
from uuid import uuid4
from validators import ValorUnico, BairroValidador
from db import db
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError

def validate_func(v):
    print(v, "tte")

class PontoVacinacaoUpdateSchema(Schema):
    idpontovacinacao = fields.Str(dump_only=True)
    nome = fields.Str(required=True, validate=[ValorUnico(model=PontoVacinacao, campo='nome'), ])
    bairro = fields.Function(validate=[BairroValidador(), ], serialize=lambda obj: Bairro.pegar_bairro(obj.bairro).value, deserialize= lambda value: Bairro.pegar_bairro(value))
    endereco = fields.Str(required=False)
    horario_expediente = fields.Str(required=False)
    faixa_etaria = fields.Str(required=False)

    
