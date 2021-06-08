from flask import Flask
from flask_restx import Api

from .commands import register_commands
from .config import config_by_name
from .error import register_errorhandlers
from .database import db
from .routes import register_routes


def create_app(env: str) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_by_name[env])

    register_errorhandlers(app)

    register_commands(app)

    api = Api(app, title="Airline API", version="0.1.0")

    register_routes(api, app)

    db.init_app(app)

    return app
