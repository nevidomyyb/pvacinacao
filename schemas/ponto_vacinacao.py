from marshmallow import Schema, fields
from models import Bairro, PontoVacinacao
from uuid import uuid4
from validators import ValorUnico, BairroValidador
from db import db
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

def serialize(obj):
    return Bairro.pegar_bairro(obj.bairro).value  if isinstance(obj, PontoVacinacao) else obj
    
def deserialize(obj):
    return Bairro.pegar_bairro(obj)

class PontoVacinacaoSchema(Schema):
    idpontovacinacao = fields.Str(dump_only=True)
    nome = fields.Str(required=True, validate=[ValorUnico(model=PontoVacinacao, campo='nome'), ])
    bairro = fields.Function(
        validate=[BairroValidador(), ], 
        serialize=serialize, 
        deserialize= lambda value: Bairro.pegar_bairro(value))
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

    def update(self, obj, novos_dados):

        campos_atualizaveis = [nome_campo for nome_campo, instancia_campo in  self.fields.items() if not instancia_campo.dump_only]
        for campo in campos_atualizaveis:
            setattr(obj, campo, novos_dados.get(campo))

        return obj

        