""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""

from models.workshop_holder_mixin import WhorkshopHolderMixin


class Employee(WhorkshopHolderMixin):
    """ Defines an Employee """

    version = "1.1.1"

    def __init__(self, name, mail, workshop, spe, phone_number, pic=None):
        """ Initialises an Employee instance
            - name: Employee's name
            - mail: Employee's mail
            - workshop: Employee's workhop
            - spe: Employee's specialiastion
            - phone_number: Employee's phone_number
            - pic: Employee's path to picture
        """

        self.name = name
        self.mail = mail
        self.spe = spe
        self.phone_number = phone_number
        self.pic = pic

        super().__init__(workshop)

    def to_dict(self):
        """ Returns the dictionary representation for the instance """
        return self.__dict__
