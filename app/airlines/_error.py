from flask import jsonify
from typing import Any, Dict, Optional

from flask.app import Flask


class ExternalError(Exception):
    """External-facing error."""
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        payload: Optional[Dict] = None,
    ) -> None:
        self.message = message
        self.payload = payload
        self.status_code = status_code

    def to_dict(self) -> Dict:
        data = dict(self.payload or ())
        data["message"] = self.message

        return data


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
