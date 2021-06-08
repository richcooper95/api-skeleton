"""Define types that make an Airline entity."""

from mypy_extensions import TypedDict


class AirlineInterface(TypedDict, total=False):
    """Class defining an Airline interface.

    This is a typed definition of what's necessary to create an Airline entity.

    An Interface allows Python typechecking to be used alongside the Schema
    validation and Model definition.
    """
    airline_id: int
    name: str
    country: str
