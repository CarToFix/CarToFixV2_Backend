""" This module contains the class Part that represents a Part of a Vehicle

Created by:
    Emanuel Trias
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String, Integer


class Part(WhorkshopHolderMixin):
    """ Defines a Part of a Vehicle """

    version = "2.0.1"

    __tablename__ = "parts"
    name = Column(String(20), nullable=False)
    brand = Column(String(20), nullable=False)
    description = Column(String(120), nullable=False)
    model = Column(String(20), nullable=False)
    size = Column(Integer, nullable=False)

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
