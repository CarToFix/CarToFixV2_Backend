""" This module contains the class Employee that represents a workshop employee

created by Leonardo Rodriguez
"""

from models.common import Common


class Quote(Common):
    """Define a quote"""
    version = "1.0.0"

    def __init__(self, price, created_by, work, paymeth, garanty, quotes, limitday, sent, activated, confirm, inspect):
        """Inicialice the quote
        price: the price of all the work
        Creatby: the token of the employee which created the quote
        work: the work to do in the vehicle
        paymeth: the method of payment
        garanty: the garanty of the payment
        quotes: the number of quotes to pay
        limitday: the limit day to pay the price 
        sent: if a mail was sent to the owner
        activated: if the customer acepted the payment
        confirm: if the the payment has been confirmed
        inspect: the data of the vehicle at the time of delivery
        """
        self.price = price
        self.created_by = created_by
        self.work = work
        self.paymeth = paymeth
        self.garanty = garanty
        self.quotes = quotes
        self.limitday = limitday
        self.sent = sent
        self.activated = activated
        self.confirm = confirm
        self.inspect = inspect
        super().__init__()

    def to_dict(self):
        """ Returns the dictionary representation for the instance """
        return self.__dict__
