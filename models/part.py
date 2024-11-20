""" This module contains the class Part that represents a Part of a Vehicle

Created by:
    Emanuel Trias
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from models.common import Common


class Part(Common):
    """ Defines a Part of a Vehicle """

    __tablename__ = 'parts'
    name          = Column(String(30), nullable=False)
    description   = Column(String(160), nullable=False)
    size          = Column(Integer, nullable=False)
    status        = Column(String(10))
    workshop_id   = Column(UUID(as_uuid=True), ForeignKey('workshops.id'), nullable=False)  # Foreign key referencing workshops

    # Relationship
    workshop      = relationship("Workshop", foreign_keys=[workshop_id], back_populates="parts")

    def __init__(self, name, brand, description, model, size, workshop_id, status):
        """ Initializes a Part6
            - name: Part's name
            - brand: Part's brand
            - description: Part's description
            - model: Part's model
            - size: Part's size
        """
        super().__init__()

        self.name = name
        self.brand = brand
        self.description = description
        self.model = model
        self.size = size
        self.workshop_id = workshop_id
        self.satus = status

    def to_dict(self, hors={}):
        """ Returns a dictionary representation of the class 
            - hors: hidde or show, dictionary that defines which attributes to return
        """
        dic = {}

        for k, v in self.__dict__.items():
            # Check if the key should be shown or hidden
            if k in hors.get('show', []) or k not in hors.get('hide', []):
                dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'


        return dic
