""" This module contains the class Employee that represents a workshop employee

created by Leonardo Rodriguez
"""
from sqlalchemy import Column, String, Integer, Float, Date, Boolean

from models.common import Common


class Quote(Common):
    """ Defines a Quote """

    __tablename__ = 'quotes'
    price          = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    warranty       = Column(String, nullable=True)
    installments   = Column(Integer, nullable=True)
    price_due_date = Column(Date, nullable=True)
    sent           = Column(Boolean, default=False)
    active         = Column(Boolean, default=False)
    confirmed      = Column(Boolean, default=False)

    def __init__(self, price, created_by, tasks, payment, warranty, installments, ddprice, sent, active, confirmed, vehicle):
        """ Inicialice the quote
            - price .......... price of all the work
            - created_by ..... employee who created the quote
            - tasks .......... work to be realized on the car
            - payment ........ payment method
            - warranty ....... warranty of the payment
            - installments ... number of installments to pay
            - ddprice ........ price due date
            - sent ........... determines whether the owner was notified
            - active ......... determines whether the costumer accepted the quote
            - confirmed ...... determines whether the quote has been answered
            - vehicle ........ quote's vehicle
        """
        self.price          = price
        self.created_by     = created_by
        self.tasks          = tasks
        self.payment_method = payment
        self.warranty       = warranty
        self.installments   = installments
        self.price_due_date = ddprice
        self.sent           = sent
        self.active         = activated
        self.confirmed      = confirmed
        self.vehicle        = vehicle

        super().__init__()

    def to_dict(self):
        """ Returns the dictionary representation for the instance """
        return self.__dict__
