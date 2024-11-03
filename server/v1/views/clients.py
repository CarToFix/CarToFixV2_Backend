""" This module contians the routes for the Client class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter

from models.client import Client


router = APIRouter()  # Create router

# First get routes
# Then put routes


class CreateClient(BaseModel):
    """ Defines the Client attributes required for the request """
    name: str
    phone_number: str
    mail: str


@router.post("/clients", status_code=201)
async def create_cat(client_request: CreateClient):
    """ Creates and saves a new Client instance """
    # Instance of client is created
    client = Client(
        name=client_request.name,
        phone_number=client_request.phone_number,
        mail=client_request.mail
    )

    # Client is saved
    client.save()

    # Define a dictionary of client containing the chosen attributes
    cdict = client.to_dict(
        {'show': ['name', 'phone_number', 'mail', 'public_oid']})

    # Add the client dictionary to the message dictionary
    return {"message": "Client was created successfully!"}.update(cdict)
