from flask.app import Flask

from app.error import ExternalError


def register_errorhandlers(app: Flask) -> None:
    """Register any Flight-specific error handling.

    Arguments:
        app -- The {Flask} app instance to register error handlers on.
    """
    # None currently required.
    pass
