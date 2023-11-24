from flask import Flask
import click
from flask.cli import FlaskGroup
from models import PontoVacinacao
from schemas import PontoVacinacaoSchema
import os
from db import db
from dotenv import load_dotenv

app = Flask(__name__, instance_path=os.getcwd())

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'))

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DEBUG = os.environ.get("DEBUG")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{db_user}:{db_password}@localhost/{db_name}".format(db_user=DB_USER, db_password=DB_PASSWORD, db_name=DB_NAME)

db.init_app(app)

@click.command()
def dump():
    with app.app_context():
        import json
        data = []
        for instance in PontoVacinacao.query.all():
            data.append(instance.to_dict())

        with open('dump.json', 'w') as file:
            json.dump(data, file, indent=2)

@click.command()
def load():
    import uuid
    with app.app_context():
        import json
        with open('dump.json', 'r') as file:
            fixtures = json.load(file)
        pontos = []
        for item in fixtures:
            ponto_vacinacao = PontoVacinacaoSchema().load(item)
            p = PontoVacinacaoSchema.novo_ponto(ponto_vacinacao)
            db.session.add(p)
            db.session.commit()

cli = FlaskGroup(app)
cli.add_command(dump)
cli.add_command(load)

if __name__  == "__main__":
    cli()
