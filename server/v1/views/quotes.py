""" This module contians the routes for the Quote class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.quote import Quote

router = APIRouter()  # creates a route


class CreateQuote(BaseModel):
    """defines the Quote class"""
    price: int
    created_by: str
    work: str
    paymeth: str
    garanty: str
    quotes: int
    ddprice: int
    sent: bool
    activated: bool
    confirm: bool
    vehicle: str
    workshop: str


@router.post("/quotes", status_code=201)
async def create_quote(client_request: CreateQuote):
    """Create and saves the Quote"""
    quote = Quote(price=client_request.price, created_by=client_request.created_by, work=client_request.work, paymeth=client_request.paymeth, garanty=client_request.garanty,
                  quotes=client_request.quotes, ddprice=client_request.ddprice, sent=client_request.sent, activated=client_request.activated, confirm=client_request.confirm, vehicle=client_request.vehicle)

    quote.save()

    qdict = quote.to_dict(
        {'show': ['price', 'created_by', 'work', 'paymeth', 'garanty', 'quotes', 'ddprice', 'sent', 'activated', 'confirm', 'vehicle']})

    return {"message": "the Quote has been created successfully"}.update(qdict)
