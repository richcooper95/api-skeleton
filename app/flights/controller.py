"""Orchestrates routes, services and schemas for Flight entities."""

from flask import jsonify, request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response

from typing import List

from .interface import FlightInterface, OfferInterface
from .schema import FlightSchema
from .service import FlightService


api = Namespace("Flight", description="Airline flights.")


@api.route("/search")
class FlightResource(Resource):
    """Flight resource."""

    @accepts(schema=FlightSchema, api=api)
    @responds(schema=OfferSchema, many=True)
    def post(self) -> List[Offer]:
        """Create a single Flight."""
        flight_data: FlightInterface = request.parsed_obj

        offers: List[Offer] = FlightService.search(flight_data)

        
