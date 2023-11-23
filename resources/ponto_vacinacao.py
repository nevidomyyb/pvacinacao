from flask_smorest import Blueprint, abort
from db import db
from models import PontoVacinacao, Bairro
from schemas import PontoVacinacaoGetSchema, PontoVacinacaoSchema
from flask.views import MethodView
from flask import request


blp = Blueprint('pontos_vacinacao', __name__, description= 'Operações de pontos de vacinação')

@blp.route('/pontos/')
class Pontos(MethodView):

    @blp.arguments(PontoVacinacaoGetSchema, location='query')
    @blp.response(200, PontoVacinacaoSchema(many=True))
    def get(self, args):
        if 'bairro' in args and args['bairro'] == None:
            return {}
        if 'bairro' in args and args.get('bairro'):
            return PontoVacinacao.query.filter_by(bairro=args['bairro']).all()
        else:
            return PontoVacinacao.query.all()
    
    @blp.arguments(PontoVacinacaoSchema)
    @blp.response(201, PontoVacinacaoSchema)
    def post(self, ponto_data):
        ponto = PontoVacinacaoSchema.novo_ponto(ponto_data)
        return ponto

@blp.route('/ponto/<uuid_>/')
class PontoUnico(MethodView):

    @blp.response(200, PontoVacinacaoSchema)
    def get(self, uuid_):
        ponto = PontoVacinacao.query.get_or_404(uuid_)
        return ponto
    
    @blp.arguments(PontoVacinacaoSchema)
    @blp.response(204, PontoVacinacaoSchema)
    def patch(self, uuid_):
        ponto = PontoVacinacao.query.get_or_404(uuid_)
        
        

    
