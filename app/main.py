import os

from flask import Flask
from flask_restx import Api

from typing import Optional

from app.config import config_by_name
from app.resources import db
from app.routes import register_routes


def create_app(env: Optional[str] = None) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_by_name[env or "test"])

    api = Api(app, title="Airline API", version="0.1.0")

    register_routes(api, app)

    db.init_app(app)

    return app


def run() -> None:
    app = create_app(os.getenv("FLASK_ENV"))

    app.run(debug=True)
