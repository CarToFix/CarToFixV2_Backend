#!/usr/bin/python
"""this is a file to make testing about the class common"""
from datetime import datetime
import uuid
import pytest
from models.here import Here


@pytest.fixture
def setup_data():
    """Set up variables or resources here"""
    her = Here()
    return her


def test_attr_exist(setup_data):
    """this is a test to make sure the attributes exists"""
    assert hasattr(setup_data, "oid")
    assert hasattr(setup_data, "created_at")
    assert hasattr(setup_data, "updated_at")
    assert hasattr(setup_data, "to_dict")


def test_correct_attr(setup_data):
    """this is test to make sure the attributes are correct"""
    assert isinstance(setup_data.oid, uuid.UUID)
    assert isinstance(setup_data.created_at, datetime)
    assert isinstance(setup_data.updated_at, datetime)


def test_todic(setup_data):
    """a test to check if the method to dic works"""
    assert isinstance(setup_data.to_dict(), dict)


def test_return(setup_data):
    """a test to check if the creation of the common class can be done"""
    with pytest.raises(AttributeError):
        setup_data.updated_at = datetime.now()
    value1 = setup_data.created_at.strftime('%Y-%m-%d %H:%M')
    value2 = setup_data.updated_at.strftime('%Y-%m-%d %H:%M')
    assert value1 == value2
    fecha = setup_data.created_at = datetime.now()
    uid = setup_data.oid = uuid.uuid4()
    assert setup_data.oid == uid
    assert setup_data.created_at.strftime(
        '%Y-%m-%d %H:%M') == fecha.strftime('%Y-%m-%d %H:%M')


def test_change_setattr(setup_data):
    """Check if the time of updated at change when you update something"""
    value1 = setup_data.updated_at
    setup_data.oid = uuid.uuid4()
    setup_data.created_at = datetime.now()
    setup_data.size = 25
    val2 = setup_data.updated_at
    assert value1 != val2


def test_border_cases1(setup_data):
    """checks if the attributes in limit values"""
    setup_data.oid = "hola"
    setup_data.created_at = "21/06/23"
    assert setup_data.oid == "hola"
    assert setup_data.created_at == "21/06/23"
    setup_data.oid = 17
    assert setup_data.oid == 17
    setup_data.created_at = "hola"
    assert setup_data.created_at == "hola"
