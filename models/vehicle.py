"""This module contains the class vehicle that represents the Vehicle

Created by:
    Leonardo Rodriguez"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Vehicle(WhorkshopHolderMixin):
    """the class vehicle that represents the Vehicle"""

    version = "2.0.0"

    __tablename__ = "vehicles"
    plate = Column(String(8), nullable=False)
    color = Column(String(10), nullable=False)
    miles = Column(Integer, nullable=False)
    info = Column(String(120))
    vehicle_type = relationship("vehicle_types", backref="vehicles")
    vehicle_brand = relationship("vehicle_brands", backref="vehicles")
    vehicle_model = relationship("vehicle_models", backref="vehicles")
    owner = relationship("clients", backref="vehicles")
    work = relationship("services", backref="vehicles")

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
