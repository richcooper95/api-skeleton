"""Serialization/deserialization of Airline entities."""

from marshmallow import fields, Schema


class AirlineSchema(Schema):
    """Airline schema.

    This defines the translation beween the external schema (in camelCase) and
    the internal attributes of the Airline class (in snake_case).

    The external schema must be obeyed by incoming requests, and is used to
    ensure the responses are well-constructed.

    The schema is associated with a Resource in the Airline controller module,
    and used to validate and (de-)serialize all input/output for the Resource.
    """
    airlineId = fields.Number(attribute="airline_id")
    name = fields.Str(attribute="name")
    country = fields.Str(attribute="country")
