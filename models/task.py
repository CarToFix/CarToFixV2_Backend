""" Task class that represents a workshop Task

Created by:
    Emanuel Trias
"""

from models.common import Common


class Task(Common):
    """ Defines a Task """

    version = "1.0.0"

    def __init__(self, vehicle, title, desc, notes, parts, wshop, emps, quote):
        """ Initializes a Task
            - vehicle: vehicle in which to carry the task on
            - title: task title
            - desc: task description
            - notes: task ntoes
            - parts: required vehicle parts to complete the task
            - wshop: workshop issuing the task
            - emps: employees who will participate in the task completion
        """
        self.done = False
        self.vehicle = vehicle
        self.title = title
        self.description = desc
        self.notes = notes
        self.parts = parts
        self.workshop = wshop
        self.employees = emps
        self.quote = quote

        super().__init__()

    def to_dict(self):
        """ Returns a dictionary representation for the Task """
        return self.__dict__
