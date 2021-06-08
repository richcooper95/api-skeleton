from flask import Flask
from flask_restx import Api

from .commands import register_commands
from .config import get_config
from .error import register_errorhandlers
from .database import db
from .routes import register_routes


def create_app(env: str) -> Flask:
    """Create a {Flask} app instance.

    Arguments:
        env -- The environment the app is being run in, used to set config.
    """
    app = Flask(__name__)

    app.config.from_object(get_config(env))

    register_errorhandlers(app)

    register_commands(app)

    api = Api(app, title="Airline API", version="0.1.0")

    register_routes(api, app, "api")

    db.init_app(app)

    return app
