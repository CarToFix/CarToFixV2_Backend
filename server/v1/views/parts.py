""" This module contians the routes for the Part class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.part import Part

router = APIRouter()  # creates a route


class CreatePart(BaseModel):
    """defines the Part class"""
    name: str
    brand: str
    description: str
    model: str
    size: str
    workshop: str
    status: str


@router.post("/parts", status_code=201)
async def create_part(client_request: CreatePart):
    """Create and saves the Part"""
    part = Part(name=client_request.name, brand=client_request.brand, description=client_request.description,
                model=client_request.model, size=client_request.size, status=client_request.status, workhop=client_request.workshop)

    part.save()

    # pdict = part.to_dict(
    #    {'show': ['name', 'brand', 'description', 'model', 'size', 'status' 'workshop']})
    pdict = part.to_dict()
    return {"message": "the part has been created successfully"}.update(pdict)
