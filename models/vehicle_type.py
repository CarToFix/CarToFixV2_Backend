""" This module contains the class vehicle type that represents the type of a Vehicle

Created by:
    Leonardo Rodriguez
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin


class VehicleType(WhorkshopHolderMixin):
    """the class vehicle brand that represents the type of a Vehicle"""

    version = "1.0.0"

    def __init__(self, name, workshop):
        """
        initialice a brand of a vehicle
        -name: The type of vehicle name examples bike or car
        -workshop: From which workshop it is the data
        """
        self.name = name
        super().__init__(workshop)

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
