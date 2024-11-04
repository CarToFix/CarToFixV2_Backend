"""This module contains the class vehicle that represents the Vehicle

Created by:
    Leonardo Rodriguez"""
    
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


from models.common import Common

class Vehicle(Common):
    """the class vehicle that represents the Vehicle"""

    __tablename__ = 'vehicles'
    plate         = Column(String, nullable=False, unique=True)
    color         = Column(String, nullable=False)
    miles         = Column(Integer, nullable=False)
    info          = Column(String, nullable=True)
    workshop_id   = Column(UUID(as_uuid=True), ForeignKey('workshops.id'), nullable=False)

    # Relationship
    workshop      = relationship("Workshop", foreign_keys=[workshop_id], back_populates="vehicles")  # Allows access to the workshop from a vehicle

    def __init__(self, workshop_id, plate, vtype, brand, model, color, miles, owner, info):
        """
        initialice a vehicle
        -workshop: From which workshop it is the data
        -plate: the licence plate of the vehicle
        -vtype: the type of the vehicle this means if it is a car, bike or something else
        -brand: the brand of the vehicle an example could be Ferrari or Ford
        -model: this is the model of a car an example could be Dodge of the chevrolet brand
        -color: the color of the vehicle
        -miles: the miles a vehicle has when they enter in the workshop
        -owner: the owner of the vehicle
        -info: extra info like for example if the vehicle came with a scratch
        """
        self.plate = plate
        self.vtype = vtype
        self.brand = brand
        self.model = model
        self.color = color
        self.miles = miles
        self.owner = owner
        self.work  = None
        self.info  = info
        self.workshop_id = workshop_id
        super().__init__()

    def to_dict(self, hors={}):
        """ Returns a dictionary representation of the class 
            - hors: hidde or show, dictionary that defines which attributes to return
        """
        dic = {}

        show_keys = set(hors.get('show', []))
        hide_keys = set(hors.get('hide', []))

        for k, v in self.__dict__.items():
            # If 'show' is provided, only include those keys unless they're also in 'hide'
            if show_keys:
                if k in show_keys and k not in hide_keys:
                    dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'
            else:
                # If 'show' is not provided, hide those in 'hide'
                if k not in hide_keys:
                    dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'

        return dic
