"""Orchestrates routes, services and schemas for Airline entities."""

from flask import jsonify, request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response

from typing import List

from .interface import AirlineInterface
from .model import Airline
from .schema import AirlineSchema
from .service import AirlineService


api = Namespace("Airline", description="An operating airline.")


@api.route("/")
class AirlineResource(Resource):
    """Airline resource."""

    @responds(schema=AirlineSchema(many=True))
    def get(self) -> List[Airline]:
        """Get all Airlines."""
        return AirlineService.get_all()


    @accepts(schema=AirlineSchema, api=api)
    @responds(schema=AirlineSchema)
    def post(self) -> Airline:
        """Create a single Airline."""
        return AirlineService.create(request.parsed_obj)


@api.route("/<int:airlineId>")
@api.param("airlineId", "Airline database ID")
class AirlineIdResource(Resource):
    """Airline resource by Airline ID."""

    @responds(schema=AirlineSchema)
    def get(self, airlineId: int) -> Airline:
        """Get a single Airline."""
        return AirlineService.get_by_id(airlineId)


    def delete(self, airlineId: int) -> Response:
        """Delete a single Airline."""
        _id = AirlineService.delete_by_id(airlineId)

        return jsonify(dict(status="Success", id=_id))


    @accepts(schema=AirlineSchema, api=api)
    @responds(schema=AirlineSchema)
    def put(self, airlineId: int) -> Airline:
        """Update a single Airline."""
        changes: AirlineInterface = request.parsed_obj

        airline = AirlineService.get_by_id(airlineId)

        return AirlineService.update(airline, changes)
