""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""


class Permission():
    """ Defines the permissions to which an Employee can access """

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

    def to_dict(self, hors={}):
        """ Returns a dictionary representation of the class 
            - hors: hidde or show, dictionary that defines which attributes to return
        """
        dic = {}

        for k, v in self.__dict__.items():
            # Check if the key should be shown or hidden
            if k in hors.get('show', []) or k not in hors.get('hide', []):
                dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'

        return dic
