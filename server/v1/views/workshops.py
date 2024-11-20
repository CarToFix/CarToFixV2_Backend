""" This module contians the routes for the Workshop class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.workshop import Workshop

route = APIRouter()  # creates a route


class CreateWorkshop(BaseModel):
    """defines the workshop class"""
    mail: str
    name: str
    tel: str

@route.post("/workshop", status_code=201)
async def create_workshop(client_request: CreateWorkshop):
    """Create and saves the workshop"""
    workshop = Workshop(mail=client_request.mail, name=client_request.name, tel=client_request.tel)

    workshop.save()

    wdict = workshop.to_dict({'show': ['mail', 'name', 'tel', 'id']})
    print(wdict)
    return {"message": "the workshop has been created successfully"} | wdict
