#!/usr/bin/python
"""testing the class"""
from models.client import Client
import pytest


@pytest.fixture
def set_up():
    """testing the class"""
    cliente = Client("hola", "veh@gmail.com", "09999999", "auto")
    return cliente


def test_attr(set_up):
    """testring attr"""
    assert hasattr(set_up, "name")
    assert hasattr(set_up, "mail")
    assert hasattr(set_up, "tel")
    assert hasattr(set_up, "veh")
