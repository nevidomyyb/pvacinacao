import os
from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv
from flask_migrate import Migrate

from db import db

from resources import blp as ponto_blp

def create_app(db_url=None):
    app = Flask(__name__, instance_path=os.getcwd())
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, 'flaskenv'))
    
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_NAME = os.environ.get("DB_NAME")

    app.config["PROPAGATION_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "PROJETO INTEGRADOR REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{db_user}:{db_password}@localhost/{db_name}".format(db_user=DB_USER, db_password=DB_PASSWORD, db_name=DB_NAME)

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)

    api.register_blueprint(ponto_blp)

    return app