"""Perform CRUD and manipulation of airline entities."""

from typing import List

from app.resources import db

from .interface import AirlineInterface
from .model import Airline


class AirlineService:
    @staticmethod
    def get_all() -> List[Airline]:
        return Airline.query.all()


    @staticmethod
    def get_by_id(airline_id: int) -> Airline:
        return Airline.query.get(airline_id)


    @staticmethod
    def update(airline: Airline, updates: AirlineInterface) -> Airline:
        airline.update(updates)
        db.session.commit()

        return airline


    @staticmethod
    def delete_by_id(airline_id: int) -> List[int]:
        airline = Airline.query.filter(
            Airline.airline_id == airline_id
        ).first()

        if not airline:
            return []

        db.session.delete(airline)
        db.session.commit()

        # TODO: Why return a list containing only the deleted ID?
        return [airline_id]


    @staticmethod
    def create(attrs: AirlineInterface) -> Airline:
        airline = Airline(
            name=attrs["name"],
            country=attrs["country"],
        )

        db.session.add(airline)
        db.session.commit()

        return airline
