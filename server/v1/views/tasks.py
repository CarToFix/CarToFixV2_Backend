from fastapi import APIRouter, Query, HTTPException
import random

from models.task import Task
from .script_generate_tasks import gen_tasks, gen_quotes


router = APIRouter()

@router.get("/dashboard/active_workshop_tasks")
async def get_workshop_active_tasks(workshop_name: str = Query(..., description="The workshop's name")):
    return [{t.title: t.__dict__} for t in random.choice(gen_quotes()).tasks if t.done == True]
    #return [{t.title: t.__dict__} for t in gen_tasks() if t.done == True]
