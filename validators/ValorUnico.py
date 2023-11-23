from marshmallow import validate
from marshmallow.exceptions import ValidationError

class ValorUnico(validate.Validator):

    def __init__(self, model, campo):
        self.model = model
        self.campo = campo

    def __call__(self, valor):
        query = {self.campo: valor}
        ponto_vacinacao = self.model.query.filter_by(**query).first()
        if ponto_vacinacao: raise ValidationError("Ponto de vacinacao com esse valor já cadastrado.")