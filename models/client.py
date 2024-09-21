""" This module contains the class client which represents the client of the car workshops
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from models.common import Common, Base


class Client(Common, Base):
    """ Defines a Client """

    __tablename__ = 'clients'
    oid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    __name = Column("name", String(60), nullable=False)  # Use internal attributes
    __mail = Column("mail", String(60), nullable=False)
    __phone_number = Column("phone_number", String(10), nullable=False)

    # Vehicles not available yet
    #__vehicles = relationship("vehicles", backref="clients", cascade="all, delete, delete-orphan")

    def __init__(self, name, mail, phone_number):
        """ Initializes a Client instance. """
        self.__name = name
        self.__mail = mail
        self.__phone_number = phone_number
        self.__vehicles = []
        super().__init__()

    @property
    def name(self):
        """ Getter method for name """
        return self.__name

    @property
    def mail(self):
        """ Getter method for mail """
        return self.__mail

    @property
    def phone_number(self):
        """ Getter method for phone number """
        return self.__phone_number

    @property
    def vehicles(self):
        """ Getter method for vehicles """
        return self.__vehicles

    @name.setter
    def name(self, nname):
        """ Setter method for name """
        if not isinstance(nname, str):
            raise TypeError(
                f"The name should be of type String, not {type(nname)}")
        if any(c in nname for c in "!@#$%^&*()_+={}[]|\\:;\"'<>,.?/0123456789±÷×∑√∫∞≠∇∆\n\t"):
            raise ValueError(f"The provided name '{nname}' contains invalid char/s")

        self.__name = nname

    @mail.setter
    def mail(self, newmail):
        """ Setter method for mail """
        if not isinstance(newmail, str):
            raise TypeError(
                f"The mail should be of type String, not {type(newmail)}")
        if '@' not in newmail or '.' not in newmail:
            raise ValueError("A mail should contain the simbol '@' and '.'")
        if any(c in newmail for c in "!#$%^&*()_+={}[]| \:;\"'<>,?/±÷×∑√∫∞≠∇∆\n\t"):
            raise ValueError("The provided mail '{newmail}' contains invalid char/s")
        
        self.__mail = newmail

    @phone_number.setter
    def phone_number(self, newtel):
        """ Setter method for tel """
        if len(newtel) < 8:
            raise ValueError("phone_number should have at least 8 digits")
        if not isinstance(newtel, str):
            raise TypeError(
                f"phone_number should be of type String, not {type(newtel)}")
        invalid = "!@#$%^&*()_+={ }[]|\\:;\"'<>,.?/abcdefghijklmnoprstuvwxyz±÷×∑√∫∞≠∇∆\n\t"
        if any(c in newtel for c in invalid) or any(c in newtel for c in invalid.upper()):
            raise ValueError(f"phone_number '{newtel}' contains invalid char/s")

        self.__phone_number = newtel

    @vehicles.setter
    def vehicles(self, newveh):
        """ Getter method for veh """
        if isinstance(newveh, list):
            for x in newveh:
                if not x.__class__.__name__ == "Vehicle":
                    raise TypeError(
                        f"The Vehicle should be of type Vehicle, not {type(newveh)}")
            self.__vehicles.extend(newveh)
        else:
            raise TypeError(
                f"The Vehicle should be of type List, not {type(newveh)}")

    def to_dict(self, hors):
        """ Returns a dictionary representation of the class 
            - hors: hidde or show, dictionary that defines which attributes to return
        """
        dic = {}
        
        for k, v in self.__dict__.items():
            # Check if the key should be shown or hidden
            if k in hors.get('show', []) and k not in hors.get('hide', []):
                dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'
        
        return dic