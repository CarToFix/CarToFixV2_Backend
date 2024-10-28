""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""

from sqlalchemy import Column, String
from models.Common import Common


class Employee(Common):
    """ Defines an Employee """

    __tablename__ = 'employees'
    name          = Column(String(60), nullable=False)
    mail          = Column(String(60), nullable=False)
    phone_number  = Column(String(10), nullable=False)
    #spe = Column()
    #pic = Column()
    #workshop = Column()

    def __init__(self, name, mail, workshop, spe, phone_number, pic=None):
        """ Initialises an Employee instance
            - name: Employee's name
            - mail: Employee's mail
            - workshop: Employee's workhop
            - spe: Employee's specialiastion
            - phone_number: Employee's phone_number
            - pic: Employee's path to picture
        """
        super().__init__()

        self.name = name
        self.mail = mail
        self.spe = spe
        self.phone_number = phone_number
        self.workhop = workhop
        self.pic = pic

    def to_dict(self):
        """ Returns the dictionary representation for the instance """
        return self.__dict__
