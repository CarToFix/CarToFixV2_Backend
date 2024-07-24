"""This module contains the class client which represents the client of the car workshop
"""
from models.common import Common
from models.vehicle import Vehicle


class Client(Common):
    """ Defines the Client class"""
    version = '0.1.0'

    def __init__(self, name, mail, tel, veh):
        """Initialise the class client with all 
        the data from the common class"""
        self.__name = name
        self.__mail = mail
        self.__tel = tel
        self.__vehiculo = veh
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
        return self.__vehiculo

    @name.setter
    def name(self, newname):
        """the setter method of name"""
        if isinstance(newname, str):
            self.__name = newname
        raise TypeError(
            f"The name should be of type String, not {type(newname)}")

    @mail.setter
    def mail(self, newmail):
        """the setter method of mail"""
        if isinstance(newmail, str):
            self.__mail = newmail
        raise TypeError(
            f"The mail should be of type String, not {type(newmail)}")

    @tel.setter
    def tel(self, newtel):
        """the setter method of tel"""
        if len(newtel) < 8:
            raise ValueError("a Telephone should have at least 8 digits")
        if isinstance(newtel, str):
            self.__tel = newtel
        raise TypeError(
            f"The Telephone should be of type String, not {type(newtel)}")

    @veh.setter
    def veh(self, newveh):
        """the setter method of tel"""
        if isinstance(newveh, list):
            for x in newveh:
                if not isinstance(x, Vehicle):
                    raise TypeError(
                        f"The Vehicle should be of type Vehicle, not {type(newveh)}")
        raise TypeError(
            f"The Vehicle should be of type List, not {type(newveh)}")

    def to_dict(self):
        """The method to return a dictionary of the class"""
        dic = {"Name": self.name, "Mail": self.mail,
               "Telephone": self.tel, "Vehicle": self.veh}
        return dic
