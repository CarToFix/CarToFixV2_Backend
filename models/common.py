""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

Created by:
    Emanuel Trias
"""

from abc import ABC, abstractmethod
from datetime import datetime
import json
import uuid

from server.v1.utils.version_manager import VersionManager
vm = VersionManager()


class Common(ABC):
    """ Defines a Common class """
    version = '0.4.3'

    def __init_subclass__(cls, **kwargs):
        """ Defines action to be performed always upon initialization of subclasses """
        vm.save_version(cls.__name__, cls.version)

    def __init__(self):
        """ Initializes a Common class """
        self.oid = uuid.uuid4()
        self.public_oid = "Not yet implemented"
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.__version_saved = False

        vm.save_version('Common', Common.version)

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
    def to_dict(self):
        """ Returns a dictionary representation for the instance """

    def __setattr__(self, name, value):
        """Changes the updated_at attribute when model changes
            - name: name of the attribute to be updated
            - value: value to be set
        """
        if name != '_Common__updated_at':
            super().__setattr__('_Common__updated_at', datetime.utcnow())
        super().__setattr__(name, value)

    def save_version(self, classname, classversion):
        """ Saves a the version of a class
            - classname
            - classversion
        """
        if not self.__version_saved:
            vm.save_version(classname, classversion)
            self.__version_saved = True
