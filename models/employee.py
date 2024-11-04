""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from models.common import Common


class Employee(Common):
    """ Defines an Employee """

    __tablename__ = 'employees'
    name         = Column(String(60), nullable=False)
    mail         = Column(String(60), nullable=False)
    phone_number = Column(String(10), nullable=False)
    workshop_id  = Column(UUID(as_uuid=True), ForeignKey('workshops.id'), nullable=False)

    # Relationship
    workshop = relationship("Workshop", foreign_keys=[workshop_id], back_populates="employees")

    def __init__(self, name, mail, workshop_id, spe, phone_number, pic=None):
        """ Initialises an Employee instance
            - name: Employee's name
            - mail: Employee's mail
            - workshop_id: Employee's workhop
            - spe: Employee's specialiastion
            - phone_number: Employee's phone_number
            - pic: Employee's path to picture
        """
        super().__init__()

        self.name = name
        self.mail = mail
        self.spe = spe
        self.phone_number = phone_number
        self.workshop_id = workshop_id
        self.pic = pic

    def to_dict(self, hors={}):
        """ Returns a dictionary representation of the class 
            - hors: hidde or show, dictionary that defines which attributes to return
        """
        dic = {}

        show_keys = set(hors.get('show', []))
        hide_keys = set(hors.get('hide', []))

        for k, v in self.__dict__.items():
            # If 'show' is provided, only include those keys unless they're also in 'hide'
            if show_keys:
                if k in show_keys and k not in hide_keys:
                    dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'
            else:
                # If 'show' is not provided, hide those in 'hide'
                if k not in hide_keys:
                    dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'

        return dic
