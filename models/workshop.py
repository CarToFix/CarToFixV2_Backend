"""This module contains the class workshop that represents the workshop

Created by:
    Leonardo Rodriguez"""

from models.common import Common
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Workshop(Common):
    """the class workshop that represents the workshop"""

    version = "2.0.0"

    __tablename__ = "workshops"
    mail = Column(String(20), nullable=False)
    password = Column(String(10), nullable=False)
    name = Column(String(20), nullable=False)
    phone = Column(String(10), nullable=False)
    workers = relationship("employees", backref="workshops")
    vehicles = relationship("vehicles", backref="workshops")
    parts = relationship("parts", backref="workshops")
    works = relationship("services", backref="workshops")
    owner = Column(String(20), ForeignKey("employees.name"))

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
