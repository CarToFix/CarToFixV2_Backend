""" This module contains the class vehicle model that represents the model of a Vehicle

Created by:
    Leonardo Rodriguez
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String


class VehicleModel(WhorkshopHolderMixin):
    """the class vehicle brand that represents the model of a Vehicle"""

    version = "2.0.0"

    __table__ = "vehicle_models"
    model_name = Column(String(30), nullable=False)

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
