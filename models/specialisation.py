"""This module contains the class specialisation that represents the specialisation of a worker

Created by:
    Leonardo Rodriguez"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Specialisation(WhorkshopHolderMixin):
    """the class Specialisation that represents the specialisation of a worker"""

    version = "2.0.0"

    __tablename__ = "specialisations"
    area = Column(String(30), nullable=False)
    employee = relationship("employees", backref="specialisations")
    permission = relationship("permissions", backref="specialisations")

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
