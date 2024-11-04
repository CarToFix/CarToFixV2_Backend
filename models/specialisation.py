""" This module contains the class specialisation that represents the specialisation of a worker

Created by:
    Leonardo Rodriguez
"""
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSONB

from models.common import Common


class Specialisation(Common):
    """ Specialisation of a employee """

    __tablename__ = 'specialisations'
    area          = Column(String, nullable=False)
    permissions   = Column(JSONB, nullable=True)

    def __init__(self, workshop, area, employee, permission):
        """ Initialises a Specialisation
            - area .......... area of specialisation
            - employee ...... list of employees who have this specialisation 
            - permission .... list of permissions of each specialisation
        """
        self.area       = area
        self.employee   = employee
        self.permission = permission

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
