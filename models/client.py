"""This module contains the class client which represents the client of the car workshop
"""
from models.common import Common


class Client(Common):
    """ Defines the Client class"""

    def __init__(self, name, mail, tel, veh, oid, creat_at, upt_at):
        """Initialise the class client with all 
        the data from the common class"""
        self.__name = name
        self.__mail = mail
        self.__tel = tel
        self.__vehiculo = veh
        super.__init__(oid, creat_at, upt_at)

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
        if isinstance(newtel, str):
            self.__tel = newtel
        raise TypeError(
            f"The Telephone should be of type String, not {type(newtel)}")

    @veh.setter
    def veh(self, newtel):
        """the setter method of tel"""
        self.veh = newtel

    def to_dict(self):
        """The method to return a dictionary of the class"""
        dic = {"Name": self.name, "Mail": self.mail, "Telephone": self.tel}
        return dic

    def save(self):
        """saves any changes in the actual instance
        and saves it in the class also it updates the updated_at value
        to the actual time it was updated"""

    def delete(self):
        """This method will be used for deleting the current instance of
        the class from the storage"""
