""" This module contians the routes for the permission class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter

from models.permission import Permission


router = APIRouter()  # Create router

# First get routes
# Then put routes


class CreatePermission(BaseModel):
    """ Defines the permission class """
    name: str
    description: str
    allowed: bool


@router.post("/permissions", status_code=201)
async def create_permission(client_request: CreatePermission):
    """ Creates and saves a new permission instance """
    # Instance of client is created
    per = Permission(name=client_request.name,
                     desc=client_request.description, allowed=client_request.allowed)

    # Client is saved
    per.save()

    # Define a dictionary of client containing the chosen attributes
    pdict = per.to_dict(
        {'show': ['name', 'tel', 'mail']})

    # Add the client dictionary to the message dictionary
    return {"message": "Client was created successfully!"}.update(pdict)
