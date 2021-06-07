"""Define types that make an airline entity."""

from mypy_extensions import TypedDict

class AirlineInterface(TypedDict, total=False):
    airline_id: int
    name: str
    country: str
