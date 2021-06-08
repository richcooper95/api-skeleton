"""Perform CRUD and manipulation of airline entities."""

from typing import List, Optional

from app.database import db

from .error import AirlineIDNotFoundError
from .interface import AirlineInterface
from .model import Airline


class AirlineService:
    @staticmethod
    def get_all() -> List[Airline]:
        return Airline.query.all()


    @staticmethod
    def get_by_id(airline_id: int) -> Airline:
        airline = Airline.query.get(airline_id)

        if airline is None:
            raise AirlineIDNotFoundError(airline_id)

        return airline


    @staticmethod
    def update(
        airline: Airline,
        updates: AirlineInterface,
    ) -> Airline:
        airline.update(updates)
        db.session.commit()

        return airline


    @staticmethod
    def delete_by_id(airline_id: int) -> int:
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
        # Ignore any airlineId provided by the request - the DB will provide
        # the next-highest ID value automatically.
        airline = Airline(
            name=attrs["name"],
            country=attrs["country"],
        )

        db.session.add(airline)
        db.session.commit()

        return airline
