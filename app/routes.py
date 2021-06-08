from flask import Flask
from flask_restx import Api

from . import airlines


def register_routes(api: Api, app: Flask, *, root: str = "api") -> None:
    airlines.register_routes(api, app)
