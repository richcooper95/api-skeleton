"""Define types that make an Flight entity."""

from mypy_extensions import TypedDict


class FlightInterface(TypedDict, total=False):
    """Class defining an Flight interface.

    This is a typed definition of what's necessary to create an Flight entity.

    An Interface allows Python typechecking to be used alongside the Schema
    validation.
    """
    destination: str
    origin: str
    departure_date: str


class OfferInterface(TypedDict, total=False):
    """Class defining an Offer interface.

    This is a typed definition of what's necessary to create an Offer entity.

    An Interface allows Python typechecking to be used alongside the Schema
    validation.
    """
    id: str
    price: str
    duration: int
