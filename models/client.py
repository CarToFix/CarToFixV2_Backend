"""This module contains the class client which represents the client of the car workshops
"""
from models.common import Common


class Client(Common):
    """ Defines the Client class"""
    version = '0.1.1'

    def __init__(self, name, mail, tel):
        """Initialise the class client with all 
        the data from the common class"""
        self.name = name
        self.mail = mail
        self.tel = tel
        self.vehicle = None
        super().__init__()

        self.save_version('Client', Client.version)

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
