from marshmallow import Schema, fields
from models import Bairro, PontoVacinacao
from uuid import uuid4
from validators import ValorUnico, BairroValidador
from db import db
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError

def validate_func(v):
    print(v, "tte")

class PontoVacinacaoSchema(Schema):
    idpontovacinacao = fields.Str(dump_only=True)
    nome = fields.Str(required=True, validate=[ValorUnico(model=PontoVacinacao, campo='nome'), ])
    bairro = fields.Function(validate=[BairroValidador(), ], serialize=lambda obj: Bairro.pegar_bairro(obj.bairro).value, deserialize= lambda value: Bairro.pegar_bairro(value))
    endereco = fields.Str(required=True)
    horario_expediente = fields.Str(required=True)
    faixa_etaria = fields.Str(required=True)

    @classmethod
    def novo_ponto(cls, dados):
        novo_uuid = uuid4()
        dados['idpontovacinacao'] = novo_uuid
        ponto_vacinacao = PontoVacinacao(**dados)
        try:
            db.session.add(ponto_vacinacao)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500, message="Ocorreu um erro interno ao salvar o ponto de vacinação.")
        return ponto_vacinacao
