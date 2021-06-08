from flask import Flask
from flask_restx import Api

from .controller import api as airline_api


BASE_ROUTE = "airlines"


def register_routes(api: Api, app: Flask, *, root: str = "api") -> None:
    api.add_namespace(airline_api, path=f"/{root}/{BASE_ROUTE}")
