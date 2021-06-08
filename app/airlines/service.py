"""Perform CRUD and manipulation of Airline entities."""

from typing import List

from app.database import db

from .error import AirlineIDNotFoundError
from .interface import AirlineInterface
from .model import Airline


class AirlineService:
    """Airline service class.

    This class provides APIs for all supported operations on the Airline
    resource (i.e. the sqlite database).
    """
    @staticmethod
    def get_all() -> List[Airline]:
        """Get all entries in the Airline database.

        Returns:
            List[Airline] -- All entries in the Airline database.
        """
        return Airline.query.all()


    @staticmethod
    def get_by_id(airline_id: int) -> Airline:
        """Get a specific Airline by its Airline ID.

        Arguments:
            airline_id -- The Airline ID to retrieve.

        Returns:
            Airline -- The Airline found in the database.

        Raises:
            AirlineIDNotFoundError -- The Airline ID is not in the database.
        """
        airline = Airline.query.get(airline_id)

        if airline is None:
            raise AirlineIDNotFoundError(airline_id)

        return airline


    @staticmethod
    def update(
        airline: Airline,
        updates: AirlineInterface,
    ) -> Airline:
        """Update an Airline in the database.

        Note that this assumes the Airline is present in the database.

        Arguments:
            airline -- The Airline to update.
            updates -- The new data to store for this Airline.

        Returns:
            Airline -- The newly-updated Airline.
        """
        airline.update(updates)
        db.session.commit()

        return airline


    @staticmethod
    def delete_by_id(airline_id: int) -> int:
        """Deletes an Airline from the database by its Airline ID.

        If the Airline is already not present in the database, this is treated
        as success.

        Arguments:
            airline_id -- The Airline ID to delete.

        Returns:
            int -- The Airline ID requested to be deleted.
        """
        # Query the DB for the airline to delete.
        airline = Airline.query.filter(
            Airline.airline_id == airline_id
        ).first()

        if airline:
            # Airline exists in the DB, so delete it.
            db.session.delete(airline)
            db.session.commit()

        return airline_id


    @staticmethod
    def create(attrs: AirlineInterface) -> Airline:
        """Create a new Airline in the database.

        Arguments:
            attrs -- The attributes for the Airline to create.

        Returns:
            Airline -- The newly-created Airline.
        """
        # Ignore any airlineId provided by the request - the DB will provide
        # the next-highest ID value automatically.
        airline = Airline(
            name=attrs["name"],
            country=attrs["country"],
        )

        db.session.add(airline)
        db.session.commit()

        return airline
