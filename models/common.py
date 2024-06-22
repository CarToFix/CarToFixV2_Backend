""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

    requires: no installation of external library
"""

from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Common(ABC):
    """ Defines a Common class """

    def __init__(self):
        """ Initializes a Common class """
        self.__oid = uuid.uuid4()
        self.__created_at = datetime.utcnow()
        self.__updated_at = datetime.utcnow()

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
        self.__oid = newid

    @created_at.setter
    def created_at(self, newca):
        """ oid setter method """
        self.__created_at = newca

    @abstractmethod
    def to_dict(self):
        """ Returns a dictionary representation for the instance """

    def __setattr__(self, name, value):
        """Changes the updated_at attribute when model changes
            - name: name of the attribute to be updated
            - value: value to be set
        """
        if name != '__updated_at':
            super().__setattr__('__updated_at', datetime.utcnow())
        super().__setattr__(name, value)
