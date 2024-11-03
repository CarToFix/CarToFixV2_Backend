""" This module contians the routes for the Quote class """

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from models.quote import Quote
from datetime import datetime
router = APIRouter()  # creates a route


class CreateQuote(BaseModel):
    """defines the Quote class"""
    price: int
    task: str
    created_by: str
    payment: str
    warranty: str
    instalments: int
    ddprice: datetime
    sent: bool
    active: bool
    confirmed: bool
    vehicle: str
    workshop: str


@router.post("/quotes", status_code=201)
async def create_quote(client_request: CreateQuote):
    """Create and saves the Quote"""
    quote = Quote(price=client_request.price, created_by=client_request.created_by, tasks=client_request.task, payment=client_request.payment, warranty=client_request.warranty,
                  installments=client_request.instalments, ddprice=client_request.ddprice, sent=client_request.sent, active=client_request.active, confirmed=client_request.confirmed, vehicle=client_request.vehicle)

    quote.save()

    # qdict = quote.to_dict(
    #   {'show': ['price', 'created_by' 'task', 'payment', 'warranty', 'installments', 'ddprice', 'sent', 'active', 'confirmed', 'vehicle']})
    qdict = quote.to_dict()
    return {"message": "the Quote has been created successfully"}.update(qdict)
