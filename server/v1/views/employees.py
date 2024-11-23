""" This module contians the routes for the Employee class """

import uuid

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.employee import Employee
from models.workshop import Workshop
from models import storage

route = APIRouter()  # creates a route


class CreateEmployee(BaseModel):
    """defines the employee class"""
    name: str
    mail: str
    phone_number: str
    speciality: str
    picture: str
    workshop_id: str


@route.post("/employees", status_code=201)
async def create_employee(client_request: CreateEmployee):
    """Create and saves the Employee"""
    employee = Employee(name=client_request.name, mail=client_request.mail,
                        phone_number=client_request.phone_number, spe=client_request.speciality, pic=client_request.picture, workshop_id=uuid.UUID(client_request.workshop_id))

    employee.save()

    edict = employee.to_dict(
        {'show': ['name', 'mail', 'phone_number', 'spe', 'pic', 'workshop_id', 'id']})
    print(edict)
    return {"message": "the employee has been created successfully"} | edict


@route.get("/employees<workshop_id>", status_code=200)
async def search_workshop_employee(workshop):
    """a function to search the employees of a workshop and the owner"""
    work = storage.get(Workshop, workshop)
    if work is not Workshop:
        return ("error: the workshop can`t be found")
    emp = work.to_dict({'show': ['employees']})
    employees = [emp.todict({'show': ['name']})
                 for emp in Workshop.employees]
    return (employees)
