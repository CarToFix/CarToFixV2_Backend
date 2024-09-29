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

    _oid = Column(PGUUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    _created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    _updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self):
        self.oid = uuid.uuid4()
        self.public_oid = self.__hash_uuid(self.oid)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    @property
    def oid(self):
        """ oid getter method """
        return self._oid

    @property
    def public_oid(self):
        """ public oid getter method """
        return self._public_oid

    @property
    def created_at(self):
        """ created_at getter method """
        return self._created_at

    @property
    def updated_at(self):
        """ updated_at getter method """
        return self._updated_at

    @oid.setter
    def oid(self, newid):
        """ oid setter method """
        if not isinstance(newid, uuid.UUID):
            raise TypeError(f"New id must be of type uuid.UUID, not {type(newid)}")

        self._oid = newid

    @public_oid.setter
    def public_oid(self, newid):
        """ public oid setter method """
        self._public_oid = newid

    @created_at.setter
    def created_at(self, newca):
        """ created_at setter method """
        if not isinstance(newca, datetime):
            raise TypeError(f"New created_at must be of type datetime, not {type(newca)}")

        self._created_at = newca

    @updated_at.setter
    def updated_at(self, newaa):
        """ updated_at setter method """
        if not isinstance(newaa, datetime):
            raise TypeError(f"New updated_at must be of type datetime, not {type(newaa)}")
        self._updated_at = newaa

    @abstractmethod
    def to_dict(self, hide):
        """ Returns a dictionary representation for the instance """

    def save(self):
        """ Saves the instance to the database """
        models.storage.new(self)   # Instance is added to the session
        models.storage.save()  # Instance is saved to the db

        print(f"New instance {self._public_oid} of type: {type(self).__name__} was created!")

    def __hash_uuid(self, input_uuid):
        """ Encodes an UUID using SHA256 algorithm """
        # Convert the UUID to a string and encode it to bytes
        uuid_str = str(input_uuid).encode()

        # Hash the UUID using SHA-256
        hash_object = hashlib.sha256(uuid_str)

        # Return the hexadecimal digest of the hash
        return hash_object.hexdigest()

    def __setattr__(self, name, value):
        """ Changes the updated_at attribute when model changes
            - name: name of the attribute to be updated
            - value: value to be set
        """
        if name != '_Common__updated_at':
            super().__setattr__('_Common__updated_at', datetime.utcnow())
        super().__setattr__(name, value)

    def __eq__(self, other):
        """ Defines a custom comparison operator """
        if not isinstance(other, self.__class__):
            return False

        # Checks both objects have the same attributes and their values are equal
        return self.__dict__ == other.__dict__
