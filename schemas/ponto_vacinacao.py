from marshmallow import Schema, fields
from models import Bairro

class PontoVacinacaoSchema(Schema):
    idpontovacinacao = fields.Str(dump_only=True)
    nome = fields.Str(required=True)
    bairro = fields.Str(validate=lambda s: s in Bairro._value2member_map_, required=True)
    horario_expediente = fields.Str(required=True)
    faixa_etaria = fields.Str(required=True)

    