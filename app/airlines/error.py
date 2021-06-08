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
            payload={"airlineId": airline_id},
        )


def register_errorhandlers(app: Flask) -> None:
    """Register any Airline-specific error handling here."""
    pass
