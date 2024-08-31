""" This module contains the class Employee that represents a workshop employee

created by Leonardo Rodriguez
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship


class Quote(WhorkshopHolderMixin):
    """Define a quote"""

    version = "2.0.0"

    __tablename__ = "quotes"
    price = Column(Integer, nullable=False)
    pay_method = Column(String(10), nullable=False)
    garanty = Column(DateTime, nullable=False)
    quote = Column(Integer, nullable=False)
    deadline = Column(DateTime, nullable=False)
    sent = Column(Boolean)
    confirm = Column(Boolean)
    creator_code = Column(Integer, nullable=False)
    works = relationship("services", backref="quotes")
    vehicle = relationship("vehicle", backref="quotes")

    def to_dict(self):
        """ Returns the dictionary representation for the instance """
        return self.__dict__
