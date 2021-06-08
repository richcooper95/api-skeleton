"""Python representation of airline entities."""

from sqlalchemy import Integer, Column, String

from app.database import db

from .interface import AirlineInterface


class Airline(db.Model):
    """Class representing an airline."""

    __tablename__ = "airline"

    airline_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    country = Column(String(255))


    def update(self, changes: AirlineInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self
