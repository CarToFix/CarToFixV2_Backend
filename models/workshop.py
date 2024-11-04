"""This module contains the class workshop that represents the workshop

Created by:
    Leonardo Rodriguez"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from models.common import Common
from models.employee import Employee


class Workshop(Common):
    """the class workshop that represents the workshop"""

    __tablename__ = 'workshops'
    mail = Column(String, nullable=False)
    name = Column(String, nullable=False)
    tel = Column(String, nullable=False)

    # Reference to the owner (single Employee)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('employees.id'))  # Assuming employees.id is the primary key

    # Relationships
    owner = relationship("Employee", foreign_keys=[owner_id], backref="owned_workshop")
    vehicles = relationship("Vehicle", back_populates="workshop")
    tasks = relationship("Task", back_populates="workshop")
    parts = relationship("Part", back_populates="workshop")
    employees = relationship("Employee", foreign_keys=[Employee.workshop_id], back_populates="workshop")  # Specify foreign key

    def __init__(self, mail, name, tel):
        """
        initialice a workshop
        name: name of the workshop
        tel: contact phone
        veh: list of vehicles of the workshop
        part: list of parts on the workshop
        emp: list of employees of the worshop
        owner: the owner of the workshop
        """
        self.mail      = mail
        self.name      = name
        self.tel       = tel
        self.vehicles  = []
        self.tasks     = [] 
        self.parts     = [] 
        self.employees = []
        self.owner     = None

        super().__init__()

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
