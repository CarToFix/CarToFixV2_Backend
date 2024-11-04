""" This module contians the routes for the Vehicle class """

import uuid

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.vehicle import Vehicle

router = APIRouter()  # creates a route


class CreateVehicle(BaseModel):
    """defines the Vehicle class"""
    plate: str
    vtype: str
    brand: str
    model: str
    color: str
    miles: int
    owner: str
    info: str
    workshop_id: str


@router.post("/vehicles", status_code=201)
async def create_vehicle(client_request: CreateVehicle):
    """Create and saves the Vehicle"""
    vehicles = Vehicle(
        plate=client_request.plate, vtype=client_request.vtype, brand=client_request.brand,
        model=client_request.model, color=client_request.color, miles=client_request.miles,
        owner=uuid.UUID(client_request.owner), info=client_request.info, workshop_id=uuid.UUID(client_request.workshop_id))

    vehicles.save()

    vdict = vehicles.to_dict({'show': ['plate', 'vtype', 'brand', 'model', 'color', 'miles', 'owner', 'info', 'workshop_id', 'id']})
    return {"message": "the Vehicle has been created successfully"} | vdict
