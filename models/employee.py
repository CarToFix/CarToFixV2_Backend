""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Employee(WhorkshopHolderMixin):
    """ Defines an Employee """

    version = "1.1.1"

    __tablename__ = "employees"
    name = Column(String(20), nullable=False)
    mail = Column(String(20), nullable=False)
    phone = Column(String(10), nullable=False)
    pic = Column(String(50))
    workshop = Column(String(20), ForeignKey("workshop.name"))
    specialization = relationship("specializations", backref="employees")

    def to_dict(self):
        """ Returns the dictionary representation for the instance """
        return self.__dict__
