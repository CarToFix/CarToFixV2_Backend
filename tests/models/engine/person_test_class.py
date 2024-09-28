"""
This module defines the SQLAlchemy models for the application.

It includes:
  - Gender enumeration for gender types.
  - Person model representing a person with various attributes.
"""

import uuid
from enum import Enum as PyEnum

from sqlalchemy import Column, String, Date, Enum, Integer
from models.common import Base


class Gender(PyEnum):
    """ Enumeration for gender """
    MALE = "Male"
    FEMALE = "Female"

class TestPerson(Base):
    """ Person class inherits from Base """
    __test__ = False
    __tablename__ = 'test_persons'

    oid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=False, nullable=False)
    phone_number = Column(String(20))
    birth_date = Column(Date)
    gender = Column(Enum(Gender))
    address = Column(String(255))
    city = Column(String(100))
    state = Column(String(50))

    def full_name(self):
        """
        Returns the full name of the person, combining first and last name.

        Returns:
            str: The full name of the person.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """ String representation for a person """
        return f"{self.first_name}-{self.last_name}"


class TestCat(Base):
    """ Cat class inherits from Base """
    __test__ = False
    __tablename__ = 'test_cats'

    oid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    breed = Column(String(50))
    age = Column(Integer)
    birth_date = Column(Date)
    gender = Column(Enum(Gender))
    owner_name = Column(String(100))

    def __eq__(self, other):
        """ Defines a custom comparison operator """
        if not isinstance(other, self.__class__):
            return False

        sdict = {k: v for k, v in self.__dict__.items() if k != '_sa_instance_state'}
        odict = {k: v for k, v in other.__dict__.items() if k != '_sa_instance_state'}

        return sdict == odict
