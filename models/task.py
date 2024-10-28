""" Task class that represents a workshop Task

Created by:
    Emanuel Trias
"""
from sqlalchemy import Column, String, Boolean

from models.common import Common


class Task(Common):
    """ Defines a Task """
    __tablename__ = 'tasks'

    done              = Column(Boolean, default=False)
    title             = Column(String, nullable=False)
    description       = Column(String, nullable=True)
    notes             = Column(String, nullable=True)
    fully_initialised = Column(Boolean, default=False)

    def __init__(self, vehicle, title, desc, notes, parts, wshop, emps, quote):
        """ Initializes a Task
            - vehicle .... vehicle in which to carry the task on
            - title ...... task title
            - desc ....... task description
            - notes ...... task ntoes
            - parts ...... required vehicle parts to complete the task
            - wshop ...... workshop issuing the task
            - emps ....... employees who will participate in the task completion
        """
        self.done              = False
        self.vehicle           = vehicle
        self.title             = title
        self.description       = desc
        self.notes             = notes
        self.parts             = parts
        self.workshop          = wshop
        self.employees         = emps
        self.quote             = quote
        self.fully_initialised = False

        super().__init__()

    def to_dict(self, hide):
        """ Returns a dictionary representation for the Task
            - hide: determines which attributes to hide or return
        """
        task_dict = {}
        hide_keys = hide.get("hide", []) if hide else []
        show_keys = hide.get("show", []) if hide else []

        for k, value in self.__dict__.items():
            hide_match = any(hide_key in k for hide_key in hide_keys)
            show_match = any(show_key in k for show_key in show_keys)

            if hide_match or (show_keys and not show_match):
                continue

            task_dict[k] = value

        return task_dict