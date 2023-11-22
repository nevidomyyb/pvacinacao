from flask_smorest import Blueprint, abort
from db import db
from models import PontoVacinacao, Bairro
from schemas import PontoVacinacaoSchema
from flask.views import MethodView
from flask import request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint('pontos_vacinacao', __name__, description= 'Operações de pontos de vacinação')

@blp.route('/ponto')
class Pontos(MethodView):

    # @blp.arguments(PontoVacinacaoSchema, location='query')
    @blp.response(200, PontoVacinacaoSchema(many=True))
    def get(self):
        # if args.get('bairro'):
        #     return PontoVacinacao.query.filter_by(bairro=args['bairro']).all()
        # else:
            return PontoVacinacao.query.all()
    
    @blp.arguments(PontoVacinacaoSchema)
    @blp.response(201, PontoVacinacaoSchema)
    def post(self, ponto_data):
        if not ponto_data: abort(400, errors="Teste")
        ponto = PontoVacinacao(**ponto_data)

        try:
            db.session.add(ponto)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting store")
        
        return ponto



    
