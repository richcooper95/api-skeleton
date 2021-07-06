"""Perform CRUD and manipulation of Flight entities."""

from typing import List

from app.database import db

from .error import FlightIDNotFoundError
from .interface import FlightInterface
from .model import Flight


class FlightService:
    """Flight service class.

    This class provides APIs for all supported operations on the Flight
    resource (i.e. the sqlite database).
    """
    @staticmethod
    def get_all() -> List[Flight]:
        """Get all entries in the Flight database.

        Returns:
            List[Flight] -- All entries in the Flight database.
        """
        return Flight.query.all()
