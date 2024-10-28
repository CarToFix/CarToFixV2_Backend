""" This module contians the routes for the Workshop class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.workshop import Workshop

route = APIRouter()  # creates a route


class CreateWorkshop(BaseModel):
    """defines the workshop class"""
    mail = str
    password = str
    name = str
    tel = str
    veh = str
    work = str
    part = str
    emp = str
    owner = str


@route.post("/workshop", status_code=201)
async def create_work(client_request: CreateWorkshop):
    """Create and saves the workshop"""
    workshop = Workshop(mail=client_request.mail,
                        password=client_request.password, name=client_request.name,
                        tel=client_request.tel, veh=client_request.veh, work=client_request.work,
                        part=client_request.part, emp=client_request.emp, owner=client_request.owner)

    workshop.save()

    wdict = workshop.to_dict(
        {'show': ['mail', 'password', 'name', 'tel', 'veh', 'work', 'part', 'emp', 'owner']})

    return {"message": "the workshop has been created successfully"}.update(wdict)
