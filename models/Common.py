""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

    requires:
"""

from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Common:
    """ Defines a Common class """

    def __init__(self):
        """ Initializes a Common class """
        self.__oid = uuid.uuid4()
        self.__created_at = datetime.utcnow()
        self.__updated_at = datetime.utcnow()

    def __setattr__(self, name, value):
        """ Changes the updated_at attribute when model changes 
            - name: name of the attribute to be updated
            - value: value to be set
        """
        super().__setattr__(name, value)
        super().__setattr__('_Common__updated_at', datetime.utcnow())

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
