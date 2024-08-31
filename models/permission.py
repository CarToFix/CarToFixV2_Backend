""" This module contains the class Employee that represents a workshop employee

Created by:
    Emanuel Trias
"""

from models.common import Common
from sqlalchemy import Column, String, Boolean


class Permission(Common):
    """ Defines the permissions to which an Employee can access """

    version = "2.0.1"

    __tablename__ = "permissions"
    name = Column(String(20), nullable=False)
    description = Column(String(120), nullable=False)
    allowed = Column(Boolean)
