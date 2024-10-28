""" This module contains the class Part that represents a Part of a Vehicle

Created by:
    Emanuel Trias
"""

from sqlalchemy import Column, String, Integer
from models.common import Common


class Part(Common):
    """ Defines a Part of a Vehicle """

    __tablename__    = 'parts'
    self.name        = Column(String(30), nullable=False)
    self.description = Column(String(160), nullable=False)
    self.size        = Column(Integer, nullable=False)

    def __init__(self, name, brand, description, model, size, workhop):
        """ Initializes a Part6
            - name: Part's name
            - brand: Part's brand
            - description: Part's description
            - model: Part's model
            - size: Part's size
        """
        super().__init__(workhop)

        self.name = name
        self.brand = brand
        self.description = description
        self.model = model
        self.size = size

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
