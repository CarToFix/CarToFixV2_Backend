from pprint import pprint

from models.employee import Employee
from models.workshop import Workshop
from models.specialisation import Specialisation
from models.part import Part

emp = Employee("Darwanzio", "darwanzio@gmail.com", Workshop(), Specialisation(), "098709738450", pic="/path/to/pic")
pprint(emp.__dict__)
print()
part = Part("espirochet", "superbranc", "this is a super important part of the equation", "modelmodel", "enormous")
pprint(part.__dict__)
print()

