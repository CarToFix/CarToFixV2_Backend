""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

Created by:
    Emanuel Trias
"""

import hashlib
from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Common(ABC):
    """ Defines a Common class """

    def __init__(self):
        """ Initializes a Common class """
        self.oid = uuid.uuid4()
        self.public_oid = self.__hash_uuid(self.oid)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    @property
    def oid(self):
        """ oid getter method """
        return self.__oid

    @property
    def public_oid(self):
        """ public oid getter method """
        return self.__public_oid

    @property
    def created_at(self):
        """ created_at getter method """
        return self.__created_at

    @property
    def updated_at(self):
        """ updated_at getter method """
        return self.__updated_at

    @property
    def version_saved(self):
        """ updated_at getter method """
        return self.__version_saved

    @oid.setter
    def oid(self, newid):
        """ oid setter method """
        if not isinstance(newid, uuid.UUID):
            raise TypeError(f"New id must be of type uuid.UUID, not {type(newid)}")

        self.__oid = newid

    @public_oid.setter
    def public_oid(self, newid):
        """ public oid setter method """
        self.__public_oid = newid

    @created_at.setter
    def created_at(self, newca):
        """ created_at setter method """
        if not isinstance(newca, datetime):
            raise TypeError(f"New created_at must be of type datetime, not {type(newca)}")

        self.__created_at = newca

    @updated_at.setter
    def updated_at(self, newaa):
        """ updated_at setter method """
        if not isinstance(newaa, datetime):
            raise TypeError(f"New updated_at must be of type datetime, not {type(newaa)}")
        self.__updated_at = newaa

    @abstractmethod
    def to_dict(self, hide):
        """ Returns a dictionary representation for the instance """

    def __hash_uuid(self, input_uuid):
        """ Encodes an UUID using SHA256 algorithm """
        # Convert the UUID to a string and encode it to bytes
        uuid_str = str(input_uuid).encode()

        # Hash the UUID using SHA-256
        hash_object = hashlib.sha256(uuid_str)

        # Return the hexadecimal digest of the hash
        return hash_object.hexdigest()

    def __setattr__(self, name, value):
        """Changes the updated_at attribute when model changes
            - name: name of the attribute to be updated
            - value: value to be set
        """
        if name != '_Common__updated_at':
            super().__setattr__('_Common__updated_at', datetime.utcnow())
        super().__setattr__(name, value)
