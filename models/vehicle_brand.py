""" This module contains the class vehicle brand that represents the brand of a Vehicle

Created by:
    Leonardo Rodriguez
"""
from sqlalchemy import Column, String

from models.common import Common

class VehicleBrand(Common):
    """ Defines a Vehicle Brand"""

    __tablename__ = 'vehicle_brands'
    name          = Column(String, nullable=False)

    def __init__(self, name, workshop):
        """ Initialises a Brand
            - name ....... Brand name
            - workshop ... Workshop
        """
        self.name = name
        super().__init__()

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
