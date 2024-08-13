""" This module contains the class Part that represents a Part of a Vehicle

Created by:
    Emanuel Trias
"""

from models.workshop_holder_mixin import WorkshopHolderMixin


class Part(WorkshopHolderMixin):
    """ Defines a Part of a Vehicle """

    version = "1.0.0"

    def __init__(self, name, brand, description, model, size, workhop):
        """ Initializes a Part
            - name: Part's name
            - brand: Part's brand
            - description: Part's description
            - model: Part's model
            - size: Part's size
        """
        self.name = name
        self.brand = brand
        self.description = description
        self.model = model
        self.size = size

        super().__init__(workhop)

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
