""" This module contians the routes for the Vehicle Model class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.vehicle_type import VehicleType

router = APIRouter()  # creates a route


class CreateVehicleType(BaseModel):
    """defines the Vehicle Type class"""
    name = str


@router.post("/vehicle_types", status_code=201)
async def create_vehicle_type(client_request: CreateVehicleType):
    """Create and saves the Vehicle Type"""
    vtype = VehicleType(name=client_request.name,
                        workshop=client_request.workshop)

    vtype.save()

    vtdict = vtype.to_dict(
        {'show': ['name', 'workshop']})

    return {"message": "Vehicle Type has been created successfully"}.update(vtdict)
