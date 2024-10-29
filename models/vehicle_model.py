""" This module contains the class vehicle model that represents the model of a Vehicle

Created by:
    Leonardo Rodriguez
"""
from sqlalchemy import Column, String


from models.common import Common


class VehicleModel(Common):
    """the class vehicle brand that represents the model of a Vehicle"""

    __tablename__ = 'vehicle_models'
    name = Column(String, nullable=False)

    def __init__(self, name):
        """
        initialice a brand of a vehicle
        -workshop: From which workshop it is the data
        -name: it represents the name of model of a vehicle one example is
        Mach V of speed racer which V is the model name
        """
        self.name = name
        super().__init__()

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
