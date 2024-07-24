""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

    requires: no installation of external library
"""

from abc import ABC, abstractmethod
from datetime import datetime
import json
import uuid

from server.v1.utils.version_manager import VersionManager


class Common(ABC):
    """ Defines a Common class """
    version = '0.1.0'

    def __init__(self):
        """ Initializes a Common class """
        self.__oid = uuid.uuid4()
        self.__created_at = datetime.utcnow()
        self.__updated_at = datetime.utcnow()

        self.save_version('Common', Common.version)

    @property
    def oid(self):
        """ oid getter method """
        return self.__oid

    @property
    def created_at(self):
        """ created_at getter method """
        return self.__created_at

    @property
    def updated_at(self):
        """ updated_at getter method """
        return self.__updated_at

    @oid.setter
    def oid(self, newid):
        """ oid setter method """
        if not isinstance(newid, uuid.UUID):
            raise TypeError(f"New id must be of type uuid.UUID, not {type(newid)}")

        self.__oid = newid

    @created_at.setter
    def created_at(self, newca):
        """ created_at setter method """
        if not isinstance(newca, datetime):
            raise TypeError(f"New created_at must be of type datetime, not {type(newca)}")

        self.__created_at = newca

    @abstractmethod
    def to_dict(self):
        """ Returns a dictionary representation for the instance """

    def __setattr__(self, name, value):
        """Changes the updated_at attribute when model changes
            - name: name of the attribute to be updated
            - value: value to be set
        """
        if name != '_Common__updated_at':  # Check the correct mangled name
            super().__setattr__('_Common__updated_at', datetime.utcnow())
        super().__setattr__(name, value)

    def save_version(self, c, v):
        with open('./server/versions.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        data[c] = v

        with open('./server/versions.json', 'w', encoding='utf-8') as f:
            data = json.dump(data, f, indent=4)      
