from flask_smorest import Blueprint, abort
from db import db
from models import PontoVacinacao, Bairro
from schemas import PontoVacinacaoGetSchema, PontoVacinacaoSchema
from flask.views import MethodView
from flask import request, jsonify
from sqlalchemy import or_

blp = Blueprint('pontos_vacinacao', __name__, description= 'Operações de pontos de vacinação')

@blp.route('/pontos/')
class Pontos(MethodView):

    @blp.arguments(PontoVacinacaoGetSchema, location='query')
    @blp.response(200, PontoVacinacaoSchema(many=True))
    def get(self, args):
        if 'bairro' in args and args['bairro'] == None:
            return {}
        if 'bairro' in args and args.get('bairro'):
            if PontoVacinacao.query.filter_by(bairro=args['bairro']).count() == 0:
                bairro_instancia = Bairro(args['bairro'])
                b = Bairro.encontrar_proximos(bairro=bairro_instancia)
                or_f = or_(PontoVacinacao.bairro == b["acima"]["instancia"].name, PontoVacinacao.bairro == b['abaixo']['instancia'].name)
                pontos = PontoVacinacao.query.filter(or_f).all()
                json_ = {
                    "message": f"Não foram encontrados pontos de vacinação no bairro {bairro_instancia.value}, procurando também nos bairros próximos de acordo com a Região Administrativa: {b['acima']['instancia'].value} e {b['abaixo']['instancia'].value}. ",
                    "pontos_de_vacinacao": PontoVacinacaoSchema(many=True).dump(pontos)
                }
                return jsonify(json_), 200
            else:
                return PontoVacinacao.query.filter_by(bairro=args['bairro']).all()
        else:
            return PontoVacinacao.query.all()
    
    @blp.arguments(PontoVacinacaoSchema)
    @blp.response(201, PontoVacinacaoSchema)
    def post(self, ponto_data):
        ponto = PontoVacinacaoSchema.novo_ponto(ponto_data)
        return ponto

@blp.route('/ponto/<uuid:uuid_>/')
class PontoUnico(MethodView):

    @blp.response(200, PontoVacinacaoSchema)
    def get(self, uuid_):
        ponto = PontoVacinacao.query.get_or_404(uuid_)
        return ponto
    
    @blp.arguments(PontoVacinacaoSchema, location='json')
    @blp.response(204, PontoVacinacaoSchema)
    def put(self, dados,uuid_):
        ponto = PontoVacinacao.query.get_or_404(uuid_)
        try:
            ponto_ = PontoVacinacaoSchema().update(ponto, dados)
            db.session.add(ponto_)
            db.session.commit()
        except Exception as e:
            print(e)
        
        return ponto_
    
    blp.response(200)
    def delete(self, uuid_):
        ponto = PontoVacinacao.query.get_or_404(uuid_)
        try:   
            db.session.delete(ponto)
            db.session.commit()
        except Exception as e:
            print(e)
        return {}

        
        

    
