""" This module contains the class client which represents the client of the car workshops
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, validates

from models.common import Common


class Client(Common):
    """ Defines a Client """

    __tablename__ = 'clients'
    name          = Column(String(60), nullable=False)
    mail          = Column(String(60), nullable=False)
    phone_number  = Column(String(10), nullable=False)

    def __init__(self, name, mail, phone_number):
        """ Initialises a Client instance 
            - name ....... Client's name
            - mail ....... Client's mail
            - tel ........ Client's phone number
        """
        super().__init__()

        self.name = name
        self.mail = mail
        self.phone_number = phone_number
        self.vehicles = []

    @validates('name')
    def validate_name(self, key, nname):
        """ Validate name """
        if not isinstance(nname, str):
            raise TypeError(f"The name should be of type String, not {type(nname)}")
        if any(c in nname for c in "!@#$%^&*()_+={}[]|\\:;\"'<>,.?/0123456789±÷×∑√∫∞≠∇∆\n\t"):
            raise ValueError(f"The provided name '{nname}' contains invalid char/s")
        return nname

    @validates('mail')
    def validate_mail(self, key, newmail):
        """ Validate mail """
        if not isinstance(newmail, str):
            raise TypeError(f"The mail should be of type String, not {type(newmail)}")
        if '@' not in newmail or '.' not in newmail:
            raise ValueError("A mail should contain the simbol '@' and '.'")
        if any(c in newmail for c in "!#$%^&*()_+={}[]| \\:;\"'<>,?/±÷×∑√∫∞≠∇∆\n\t"):
            raise ValueError(f"The provided mail '{newmail}' contains invalid char/s")
        return newmail

    @validates('phone_number')
    def validate_phone_number(self, key, newtel):
        """ Validate phone number """
        if len(newtel) < 8:
            raise ValueError("phone_number should have at least 8 digits")
        if not isinstance(newtel, str):
            raise TypeError(f"phone_number should be of type String, not {type(newtel)}")
        invalid = "!@#$%^&*()_+={ }[]|\\:;\"'<>,.?/abcdefghijklmnoprstuvwxyz±÷×∑√∫∞≠∇∆\n\t"
        if any(c in newtel for c in invalid) or any(c in newtel for c in invalid.upper()):
            raise ValueError(f"phone_number '{newtel}' contains invalid char/s")
        return newtel

    """
    @vehicles.setter
    def vehicles(self, newveh):
        \"\"\" Getter method for veh \"\"\"
        if isinstance(newveh, list):
            for x in newveh:
                if not x.__class__.__name__ == "Vehicle":
                    raise TypeError(
                        f"The Vehicle should be of type Vehicle, not {type(newveh)}")
            self.__vehicles.extend(newveh)
        else:
            raise TypeError(
                f"The Vehicle should be of type List, not {type(newveh)}")
    """

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
