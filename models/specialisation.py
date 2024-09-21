"""This module contains the class specialisation that represents the specialisation of a worker

Created by:
    Leonardo Rodriguez"""

from models.workshop_holder_mixin import WhorkshopHolderMixin


class Specialisation(WhorkshopHolderMixin):
    """the class Specialisation that represents the specialisation of a worker"""

    version = "1.0.0"

    def __init__(self, workshop, area, employee, permission):
        """
        initialice a specialisation
        area: this is the area of specialization for example mechanic
        employee: this is represents the list of employees who have this specialization 
        permission: this is a list of permissions of every specialization
        """
        self.area = area
        self.employee = employee
        self.permission = permission
        super().__init__(workshop)

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
