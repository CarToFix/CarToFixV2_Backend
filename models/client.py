""" This module contains the class client which represents the client of the car workshops
"""


from models.common import Common


class Client(Common):
    """ Defines a Client """
    version = '0.3.1'

    def __init__(self, name, mail, tel):
        """ Initialises a Client instance 
            - name: Client's name
            - mail: Client's mail
            - tel: Client's phone number
        """
        self.name = name
        self.mail = mail
        self.tel = tel
        self.vehicles = []
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
    def tel(self):
        """ Getter method for tel """
        return self.__tel

    @property
    def vehicles(self):
        """ Getter method for veh """
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

    @tel.setter
    def tel(self, newtel):
        """ Setter method for tel """
        if len(newtel) < 8:
            raise ValueError("a Telephone should have at least 8 digits")
        if not isinstance(newtel, str):
            raise TypeError(
                f"The Telephone should be of type String, not {type(newtel)}")
        invalid = "!@#$%^&*()_+={ }[]|\\:;\"'<>,.?/abcdefghijklmnoprstuvwxyz±÷×∑√∫∞≠∇∆\n\t"
        if any(c in newtel for c in invalid) or any(c in newtel for c in invalid.upper()):
            raise ValueError(f"New phone '{newtel}' contains invalid char/s")

        self.__tel = newtel

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

    def to_dict(self):
        """ Returns a dictionary representation of the class """
        dic = {"Name": self.__name, "Mail": self.__mail,
               "Telephone": self.__tel, "Vehicle": self.__vehicles}
        return dic
