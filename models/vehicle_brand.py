""" This module contains the class vehicle brand that represents the brand of a Vehicle

Created by:
    Leonardo Rodriguez
"""
from sqlalchemy import Column, String

from models.common import Common


class VehicleBrand(Common):
    """ Defines a Vehicle Brand"""

    __tablename__ = 'vehicle_brands'
    name = Column(String, nullable=False)

    def __init__(self, name):
        """ Initialises a Brand
            - name ....... Brand name
            - workshop ... Workshop
        """
        self.name = name
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
