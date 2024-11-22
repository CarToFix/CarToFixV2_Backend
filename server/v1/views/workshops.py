""" This module contians the routes for the Workshop class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.workshop import Workshop
from models import storage

route = APIRouter()  # creates a route


class CreateWorkshop(BaseModel):
    """defines the workshop class"""
    mail: str
    password: str
    name: str
    tel: str
    city: str
    address: str


@route.post("/workshop", status_code=201)
async def create_workshop(client_request: CreateWorkshop):
    """Create and saves the workshop"""
    workshop = Workshop(mail=client_request.mail,
                        name=client_request.name, tel=client_request.tel, password=client_request.password, address=client_request.address, city=client_request.city)

    workshop.save()

    wdict = workshop.to_dict({'show': ['mail', 'name', 'tel', 'id']})
    print(wdict)
    return {"message": "the workshop has been created successfully"} | wdict


@route.get("/workshop<workshop_id>", status_code=200)
async def search_workshop(workshop):
    """a function to search a workshop:
        workshop = the id of the workshop that I want to look for
    """
    work = storage.get(Workshop, workshop)

    if work is not Workshop:
        return ("error: the workshop can`t be found")
    return (work.to_dict({'show': ['mail', 'name', 'tel']}))


@route.post("/workshop{}", status_code=201)
async def log_in(email, password):
    """a function to log in the user"""


@route.patch("/workshop<new_password>", status_code=201)
async def update_password(new_password):
    """a function to update the password of the workshop"""


@route.patch("/workshop<new_name>", status_code=201)
async def update_name(new_name):
    """a function to update only the name of the workshop"""
