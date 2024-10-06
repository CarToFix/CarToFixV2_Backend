""" This module contians the routes for the Employee class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.employee import Employee

route = APIRouter()  # creates a route


class CreateEmployee(BaseModel):
    """defines the employee class"""
    name = str
    mail = str
    phone_number = str
    speciality = str
    picture = str
    workshop = str


@route.post("/employees", status_code=201)
async def create_employee(client_request: CreateEmployee):
    """Create and saves the Employee"""
    employee = Employee(name=client_request.name, mail=client_request.mail,
                        phone_number=client_request.phone_number, spe=client_request.speciality, pic=client_request.picture, workshop=client_request.workshop)

    employee.save()

    edict = employee.to_dict(
        {'show': ['name', 'mail', 'phone_number', 'spe', 'pic', 'workshop']})

    return {"message": "the employee has been created successfully"}.update(wdict)
