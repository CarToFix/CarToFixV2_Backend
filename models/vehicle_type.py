""" This module contains the class vehicle type that represents the type of a Vehicle

Created by:
    Leonardo Rodriguez
"""
from sqlalchemy import Column, String

from models.common import Common


class VehicleType(Common):
    """the class vehicle brand that represents the type of a Vehicle"""

    __tablename__ = 'vehicle_types'
    name          = Column(String, nullable=False)

    def __init__(self, name, workshop):
        """
        initialice a brand of a vehicle
        -name: The type of vehicle name examples bike or car
        -workshop: From which workshop it is the data
        """
        self.name = name
        super().__init__()

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
