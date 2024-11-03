from fastapi import APIRouter, Query, HTTPException
import random
from pydantic import BaseModel
from models.task import Task
from .script_generate_tasks import gen_tasks, gen_quotes


router = APIRouter()


class CreateTask(BaseModel):
    """defines the employee class"""
    vehicle: str
    title: str
    description: str
    note: str
    part: str
    workshop: str
    employee: str
    quote: str
    workshop: str


@router.get("/dashboard/active_workshop_tasks")
async def get_workshop_active_tasks(workshop_name: str = Query(..., description="The workshop's name")):
    return [{t.title: t.__dict__} for t in random.choice(gen_quotes()).tasks if t.done == True]
    # return [{t.title: t.__dict__} for t in gen_tasks() if t.done == True]


@router.post("/tasks", status_code=201)
async def create_task(client_request: CreateTask):
    """Create and saves the Tasks"""
    task = Task(vehicle=client_request.vehicle, title=client_request.title, desc=client_request.description, notes=client_request.note,
                parts=client_request.part, wshop=client_request.workshop, emps=client_request.employee, quote=client_request.quote)
    task.save()

    tdict = task.to_dict(
        {'show': ['done', 'title', 'description', 'notes', 'part', 'workshop', 'employee', 'vehicle', 'budget']})

    return {"message": "the task has been created successfully"}.update(tdict)
