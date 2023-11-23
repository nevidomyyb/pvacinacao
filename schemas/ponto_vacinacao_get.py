from marshmallow import Schema, fields
from marshmallow.base import SchemaABC
from models import Bairro, PontoVacinacao
from uuid import uuid4
from validators import BairroValidador
from db import db
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError



class PontoVacinacaoGetSchema(Schema):
     bairro = fields.Function(serialize=lambda obj: Bairro.pegar_bairro(obj.bairro).value, deserialize= lambda value: Bairro.pegar_bairro(value) )