from flask import jsonify
from typing import Any

from flask.app import Flask

from app.error import ExternalError


class AirlineIDNotFoundError(ExternalError):
    """Airline ID could not be found."""
    def __init__(self, airline_id: int) -> None:
        super().__init__(
            f"Airline ID {airline_id} could not be found",
            404,
        )


def register_errorhandlers(app: Flask) -> None:
    @app.errorhandler(ExternalError)
    def handle_external_error(error: ExternalError) -> Any:
        response = jsonify(error.to_dict())
        response.status_code = error.status_code

        return response
