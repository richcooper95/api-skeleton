"""Python representation of Airline entities."""

from sqlalchemy import Integer, Column, String

from app.database import db

from .interface import AirlineInterface


class Airline(db.Model):
    """Class representing an Airline entity.

    This entity is a {SQLAlchemy.Model} which defines the sqlite table which
    Airline entities are stored in, and the columns in that table.
    """

    __tablename__ = "airline"

    airline_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    country = Column(String(255))


    def update(self, changes: AirlineInterface):
        """Update this instance with a set of new values.

        This starts a database transaction and updates the data. The
        transaction must be separately committed.

        Arguments:
            changes {AirlineInterface}
                -- The new values for each attribute. Note that changes to
                   the Airline ID are ignored.
        """
        for key, val in changes.items():
            if key != "airline_id":
                setattr(self, key, val)

        return self
