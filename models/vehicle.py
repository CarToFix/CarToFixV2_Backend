"""This module contains the class vehicle that represents the Vehicle

Created by:
    Leonardo Rodriguez"""

from models.common import Common

class Vehicle(Common):
    """the class vehicle that represents the Vehicle"""

    __tablename__ = 'vehicles'
    plate         = Column(String, nullable=False, unique=True)
    color         = Column(String, nullable=False)
    miles         = Column(Integer, nullable=False)
    info          = Column(String, nullable=True)

    def __init__(self, workshop, plate, vtype, brand, model, color, miles, owner, work, info):
        """
        initialice a vehicle
        -workshop: From which workshop it is the data
        -plate: the licence plate of the vehicle
        -vtype: the type of the vehicle this means if it is a car, bike or something else
        -brand: the brand of the vehicle an example could be Ferrari or Ford
        -model: this is the model of a car an example could be Dodge of the chevrolet brand
        -color: the color of the vehicle
        -miles: the miles a vehicle has when they enter in the workshop
        -owner: the owner of the vehicle
        -work: the work that this vehicle needs now and the history of works
        -info: extra info like for example if the vehicle came with a scratch
        """
        self.plate = plate
        self.vtype = vtype
        self.brand = brand
        self.model = model
        self.color = color
        self.miles = miles
        self.owner = owner
        self.work  = work
        self.info  = info
        super().__init__(workshop)

    def to_dict(self):
        """ Returns a dictionary representation for the instance """
        return self.__dict__
