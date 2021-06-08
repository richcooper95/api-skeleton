from flask import Flask
from flask_restx import Api

from . import airlines


def register_routes(api: Api, app: Flask, root: str) -> None:
    """Register routes on a given {Flask} app instance.

    Arguments:
        app -- The {Flask} app instance to register routes on.
    """
    airlines.register_routes(api, app, root)
