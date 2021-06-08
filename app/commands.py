from flask import Flask

from .airlines.model import Airline
from .database import db


def register_commands(app: Flask) -> None:
    """Register a set of `flask ...` commands to support.

    Arguments:
        app -- The {Flask} app instance to register commands on.
    """
    @app.cli.command("reset-db")
    def reset_db() -> None:
        print("Dropping tables...")
        db.drop_all()

        print("Creating all tables...")
        db.create_all()

        print("Seeding tables...")
        things = [
            {"name": "easyjet", "country": "gb"},
            {"name": "ryanair", "country": "gb"},
            {"name": "airfrance", "country": "fr"},
        ]
        db.session.bulk_insert_mappings(Airline, things)

        print("Committing...")
        db.session.commit()

        print("DB successfully seeded")
