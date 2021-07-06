"""Serialization/deserialization of Flight entities."""

from marshmallow import fields, Schema


class FlightSchema(Schema):
    """Flight schema.

    This defines the translation beween the external schema (in camelCase) and
    the internal attributes of the Flight class (in snake_case).

    The external schema must be obeyed by incoming requests, and is used to
    ensure the responses are well-constructed.

    The schema is associated with a Resource in the Flight controller module,
    and used to validate and (de-)serialize all input/output for the Resource.
    """
    destination = fields.Number(attribute="destination")
    origin = fields.Str(attribute="origin")
    departure_date = fields.Str(attribute="departure_date")
