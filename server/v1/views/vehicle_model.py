""" This module contians the routes for the Vehicle Model class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.vehicle_model import VehicleModel

router = APIRouter()  # creates a route


class CreateVehicleModel(BaseModel):
    """defines the Vehicle Model class"""
    name = str


@router.post("/vehicle_models", status_code=201)
async def create_vehicle_brand(client_request: CreateVehicleModel):
    """Create and saves the Vehicle Model"""
    model = VehicleModel(name=client_request.name,
                         workshop=client_request.workshop)

    model.save()

    mdict = model.to_dict(
        {'show': ['name', 'workshop']})

    return {"message": "Vehicle Model has been created successfully"}.update(mdict)
