"""This module contains the class client which represents the client of the car workshops
"""
from models.workshop_holder_mixin import WhorkshopHolderMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Client(WhorkshopHolderMixin):
    """ Defines the Client class"""
    version = '1.1.2'

    __tablename__ = 'clients'
    names = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    telephone = Column(String(10), nullable=False)
    vehicles = relationship("vehicles", backref="clients",
                            cascade="all, delete, delete-orphan")

    @property
    def name(self):
        """the getter method of name"""
        return self.__name

    @property
    def mail(self):
        """the getter method of mail"""
        return self.__mail

    @property
    def tel(self):
        """the getter method of tel"""
        return self.__tel

    @property
    def veh(self):
        """the getter method of tel"""
        return self.vehicle

    @name.setter
    def name(self, newname):
        """the setter method of name"""
        if isinstance(newname, str):
            self.__name = newname
        else:
            raise TypeError(
                f"The name should be of type String, not {type(newname)}")

    @mail.setter
    def mail(self, newmail):
        """the setter method of mail"""
        if isinstance(newmail, str):
            if '@' in newmail:
                self.__mail = newmail
            else:
                raise ValueError("A mail should contain the simbol @")
        else:
            raise TypeError(
                f"The mail should be of type String, not {type(newmail)}")

    @tel.setter
    def tel(self, newtel):
        """the setter method of tel"""
        if len(newtel) < 8:
            raise ValueError("a Telephone should have at least 8 digits")
        if not isinstance(newtel, str):
            raise TypeError(
                f"The Telephone should be of type String, not {type(newtel)}")
        self.__tel = newtel

    @veh.setter
    def veh(self, newveh):
        """the setter method of tel"""
        if isinstance(newveh, list):
            for x in newveh:
                if not x.__class__ == "Vehicle":
                    raise TypeError(
                        f"The Vehicle should be of type Vehicle, not {type(newveh)}")
            self.vehicle = newveh
        else:
            raise TypeError(
                f"The Vehicle should be of type List, not {type(newveh)}")

    def to_dict(self):
        """The method to return a dictionary of the class"""
        dic = {"Name": self.__name, "Mail": self.__mail,
               "Telephone": self.__tel, "Vehicle": self.vehicle}
        return dic
