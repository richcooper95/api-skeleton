from flask.app import Flask
from . import airlines


def register_errorhandlers(app: Flask) -> None:
    airlines.register_errorhandlers(app)
