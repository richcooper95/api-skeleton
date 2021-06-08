from flask import Flask
from flask_restx import Api

from .controller import api as airline_api


BASE_ROUTE = "airlines"


def register_routes(api: Api, app: Flask, root: str) -> None:
    """Register routes defined within the Airline API.

    Arguments:
        api -- The {Api} instance to add a {Namespace} containing routes to.
        app -- The {Flask} app instance.
        root -- The root route.
    """
    api.add_namespace(airline_api, path=f"/{root}/{BASE_ROUTE}")
