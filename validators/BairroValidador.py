from marshmallow import validate
from marshmallow.exceptions import ValidationError
from models import Bairro

class BairroValidador(validate.Validator):

    def __call__(self, valor):
        validos = [i.value for i in Bairro]
        if valor not in validos:
            raise ValidationError("Bairro inválido.")