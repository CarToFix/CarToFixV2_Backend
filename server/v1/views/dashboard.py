from fastapi import APIRouter, Query, HTTPException

from models.quote import Quote
from .script_generate_tasks import gen_quotes, generate_fake_plate, get_brand, get_model


router = APIRouter()

@router.get("/dashboard/recent_confirmed_workshop_quote_tasks")
async def get_workshop_last_confirmed_quote_tasks(workshop_name: str = Query(..., description="The workshop's name")):
    confirmed_quotes = [q for q in gen_quotes() if q.confirmed is not None]
    if confirmed_quotes:
        quote = max(confirmed_quotes, key=lambda quote: quote.confirmed)
        task_hide = {"hide": ["oid", "vehicle", "workshop", "quote"]}

        selb = get_brand()
        selm = get_model(selb)

        return {
            "quote_public_oid": quote.public_oid,
            "vehicle_brand": selb,
            "vehicle_model": selm,
            "vehicle_plate": generate_fake_plate(),
            "tasks": [t.to_dict(task_hide) for t in quote.tasks]
        }
