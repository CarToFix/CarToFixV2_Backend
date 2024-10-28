"""This module contains the class workshop that represents the workshop

Created by:
    Leonardo Rodriguez"""
from sqlalchemy import Column, String

from models.common import Common


class Workshop(Common):
    """the class workshop that represents the workshop"""

    __tablename__ = 'workshops'
    mail          = Column(String, nullable=False)
    name          = Column(String, nullable=False)
    tel           = Column(String, nullable=False)

    def __init__(self, mail, password, name, tel, veh, work, part, emp, owner):
        """
        initialice a workshop
        name: name of the workshop
        tel: contact phone
        veh: list of vehicles of the workshop
        part: list of parts on the workshop
        emp: list of employees of the worshop
        owner: the owner of the workshop
        """
        self.mail     = mail
        self.name     = name
        self.tel      = tel
        self.veh      = veh
        self.work     = work
        self.part     = part
        self.emp      = emp
        self.owner    = owner
        super().__init__()

    def to_dict(self):
        """Returns a dictionary representation for the instance"""
        return self.__dict__
