""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

Created by:
    Emanuel Trias
"""

import hashlib
import uuid
from abc import ABCMeta, abstractmethod
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

import models

# SQLAlchemy Base
Base = declarative_base()

class AbstractDeclarativeMeta(ABCMeta, DeclarativeMeta):
    """ Custom metaclass combining ABCMeta and DeclarativeMeta """

class Common(Base, metaclass=AbstractDeclarativeMeta):
    """ Defines an abstract Common class """
    __abstract__ = True  # Prevents the creation of a Common table

    id         = Column(PGUUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self):
        self.id = uuid.uuid4()  # Set the private attribute directly
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    @abstractmethod
    def to_dict(self, hors):
        """ Returns a dictionary representation for the instance """

    def save(self):
        """ Saves the instance to the database """
        models.storage.new(self)   # Instance is added to the session
        models.storage.save()      # Instance is saved to the db

        print(f"New instance {self.id} of type: {type(self).__name__} was created!")

    def __eq__(self, other):
        """ Defines a custom comparison operator """
        if not isinstance(other, self.__class__):
            return False

        # Checks both objects have the same attributes and their values are equal
        return self.__dict__ == other.__dict__
