import uuid
from fastapi import APIRouter
from pydantic import BaseModel
from models.task import Task

router = APIRouter()


class CreateTask(BaseModel):
    """defines the employee class"""
    vehicle: str
    title: str
    description: str
    note: str
    part: str
    employee: str
    quote: str
    workshop_id: str


@router.post("/tasks", status_code=201)
async def create_task(client_request: CreateTask):
    """Create and saves the Tasks"""
    task = Task(vehicle=client_request.vehicle, title=client_request.title, desc=client_request.description, notes=client_request.note,
                parts=client_request.part, workshop_id=uuid.UUID(client_request.workshop_id), emps=client_request.employee, quote=client_request.quote)
    task.save()

    tdict = task.to_dict({'show': ['done', 'title', 'description', 'notes', 'part', 'workshop_id', 'employee', 'vehicle', 'budget', 'id']})

    return {"message": "the task has been created successfully"} | tdict
