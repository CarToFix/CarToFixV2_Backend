""" This module contains the class Common,
    that defines all the attributes and methods
    all classes must have

    requires: no installation of external library
"""

from models.common import Common


class Here(Common):
    """ Defines a try class """

    def __init__(self):
        """ Initializes a try class """
        self.__size = 0
        super().__init__()

    @property
    def size(self):
        """ oid getter method """
        return self.__size

    @size.setter
    def size(self, newsize):
        """ oid setter method """
        self.__size = newsize

    def to_dict(self):
        """A method that should return a dictionary of the object"""
        return {}
