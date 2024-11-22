""" This module contians the routes for the Part class """

import uuid
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.part import Part
from models.workshop import Workshop
from models import storage

router = APIRouter()  # creates a route


class CreatePart(BaseModel):
    """defines the Part class"""
    name: str
    brand: str
    description: str
    model: str
    size: int
    workshop_id: str
    status: str


@router.post("/parts", status_code=201)
async def create_part(client_request: CreatePart):
    """Create and saves the Part"""
    part = Part(name=client_request.name, brand=client_request.brand, description=client_request.description,
                model=client_request.model, size=client_request.size, status=client_request.status, workshop_id=uuid.UUID(client_request.workshop_id))

    part.save()

    pdict = part.to_dict({'show': [
                         'name', 'brand', 'description', 'model', 'size', 'status' 'workshop_id', 'id']})
    return {"message": "the part has been created successfully"} | pdict


@router.get("/workshop<workshop_id>", status_code=200)
async def list_parts(workshop):
    """a function to search the parts of a workshop"""
    work = storage.get(Workshop, workshop)
    if work is not Workshop:
        return ("error: the workshop can`t be found")
    part = work.to_dict({'show': ['parts']})
    parts = [part.todict({'show': ['name']})
             for part in Workshop.parts]
    return (parts)
