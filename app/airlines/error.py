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
    """Register any Airline-specific error handling.

    Arguments:
        app -- The {Flask} app instance to register error handlers on.
    """
    # None currently required.
    pass
