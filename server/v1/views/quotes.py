from fastapi import APIRouter, Query, HTTPException

from models.quote import Quote
from .script_generate_tasks import gen_quotes


router = APIRouter()

@router.get("/dashboard/recent_confirmed_workshop_quote_tasks")
async def get_workshop_last_confirmed_quote_tasks(workshop_name: str = Query(..., description="The workshop's name")):
    confirmed_quotes = [q for q in gen_quotes() if q.confirmed is not None]
    if confirmed_quotes:
        quote = max(confirmed_quotes, key=lambda quote: quote.confirmed)
        return {str(quote.public_oid): [t.to_dict() for t in quote.tasks]}
