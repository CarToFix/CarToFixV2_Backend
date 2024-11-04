""" This module contians the routes for the Specialisation class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.specialisation import Specialisation

router = APIRouter()  # creates a route


class CreateSpecialization(BaseModel):
    """defines the Specialisation class"""
    area: str
    employee: str
    permision: str
    workshop: str


@router.post("/specialisations", status_code=201)
async def create_specialisation(client_request: CreateSpecialization):
    """Create and saves the Specialisation"""
    specialisation = Specialisation(
        area=client_request.area, employee=client_request.employee, permission=client_request.permision, workshop=client_request.workshop)

    specialisation.save()

    sdict = specialisation.to_dict({'show': ['area', 'employee', 'permision', 'workshop', 'id']})
    return {"message": "the Quote has been created successfully"} | sdict
