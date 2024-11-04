""" Task class that represents a workshop Task

Created by:
    Emanuel Trias
"""
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from models.common import Common


class Task(Common):
    """ Defines a Task """
    __tablename__ = 'tasks'

    done              = Column(Boolean, default=False)
    title             = Column(String, nullable=False)
    description       = Column(String, nullable=True)
    notes             = Column(String, nullable=True)
    workshop_id       = Column(UUID(as_uuid=True), ForeignKey('workshops.id'), nullable=False)  # Foreign key referencing workshops

    # Relationship
    workshop      = relationship("Workshop", foreign_keys=[workshop_id], back_populates="tasks")  # Establishes relationship to Workshop

    def __init__(self, vehicle, title, desc, notes, parts, workshop_id, emps, quote):
        """ Initializes a Task
            - vehicle .... vehicle in which to carry the task on
            - title ...... task title
            - desc ....... task description
            - notes ...... task ntoes
            - parts ...... required vehicle parts to complete the task
            - workshop_id ...... workshop issuing the task
            - emps ....... employees who will participate in the task completion
        """
        self.done              = False
        self.vehicle           = vehicle
        self.title             = title
        self.description       = desc
        self.notes             = notes
        self.parts             = parts
        self.workshop_id          = workshop_id
        self.employees         = emps
        self.quote             = quote
        self.fully_initialised = False

        super().__init__()

    def to_dict(self, hors={}):
        """ Returns a dictionary representation of the class 
            - hors: hidde or show, dictionary that defines which attributes to return
        """
        dic = {}

        for k, v in self.__dict__.items():
            # Check if the key should be shown or hidden
            if k in hors.get('show', []) or k not in hors.get('hide', []):
                dic[k.split('__', 1)[-1]] = v  # Use everything after the first '__'


        return dic