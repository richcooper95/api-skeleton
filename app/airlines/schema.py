"""Serialization/deserialization of airline entities."""

from marshmallow import fields, Schema

class AirlineSchema(Schema):
    """Airline schema."""
    airlineId = fields.Number(attribute="airline_id")
    name = fields.Str(attribute="name")
    country = fields.Str(attribute="country")
