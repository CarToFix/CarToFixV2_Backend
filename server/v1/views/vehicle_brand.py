""" This module contians the routes for the Vehicle Brand class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.vehicle_brand import VehicleBrand

router = APIRouter()  # creates a route


class CreateVehicleBrand(BaseModel):
    """defines the Vehicle Brand class"""
    name = str


@router.post("/vehicle_brand", status_code=201)
async def create_vehicle_brand(client_request: CreateVehicleBrand):
    """Create and saves the Vehicle Brand"""
    brand = VehicleBrand(name=client_request.name,
                         workshop=client_request.workshop)

    brand.save()

    bdict = brand.to_dict(
        {'show': ['name', 'workshop']})

    return {"message": "the Vehicle Brand has been created successfully"}.update(bdict)
