from flask import Flask
from flask_restx import Api

from .controller import api as flights_api


BASE_ROUTE = "flights"


def register_routes(api: Api, app: Flask, root: str) -> None:
    """Register routes defined within the Flights API.

    Arguments:
        api -- The {Api} instance to add a {Namespace} containing routes to.
        app -- The {Flask} app instance.
        root -- The root route.
    """
    api.add_namespace(flights_api, path=f"/{root}/{BASE_ROUTE}")
