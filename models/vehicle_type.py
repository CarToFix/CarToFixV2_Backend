""" This module contains the class vehicle type that represents the type of a Vehicle

Created by:
    Leonardo Rodriguez
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String


class VehicleType(WhorkshopHolderMixin):
    """the class vehicle brand that represents the type of a Vehicle"""

    version = "2.0.0"

    __tablename__ = "vehicle_types"
    name = Column(String(10), nullable=False)

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
