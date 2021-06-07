"""Python representation of airline entities."""

from sqlalchemy import Integer, Column, String

from app import db

class Airline(db.Model):
    """Class representing an airline."""
    airline_id: Column(Integer(), primary_key=True)
    name: Column(String(length=255))
    country: Column(String(length=255))
