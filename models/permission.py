""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""

from models.common import Common


class Permission(Common):
    """ Defines the permissions to which an Employee can access """

    version = "1.0.1"

    def __init__(self, name, desc, allowed=True):
        """ Initializes a Permission 
            - name: Permissions name
            - desc: A brief description for a permission
            - allowed: determines who can use the functionallity
        """
        self.name = name
        self.description = desc
        self.allowed = allowed
        super().__init__()
