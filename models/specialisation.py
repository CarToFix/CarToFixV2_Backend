""" This module contains the class specialisation that represents the specialisation of a worker

Created by:
    Leonardo Rodriguez
"""
from sqlalchemy import Column, String, JSONB

from common import Common


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

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
