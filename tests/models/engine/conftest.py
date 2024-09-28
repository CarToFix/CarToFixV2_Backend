import pytest
from datetime import datetime
from models.engine.db_storage import DBStorage
from .person_test_class import TestPerson, TestCat, Gender
from sqlalchemy import text

DBStorage.classes["TestPerson"] = TestPerson
DBStorage.classes["TestCat"] = TestCat


@pytest.fixture(scope='function', autouse=True)
def dbstorage():
    """Fixture for DBStorage"""
    dbstorage = DBStorage()

    yield dbstorage

    dbstorage.close()

@pytest.fixture(scope='function', autouse=True)
def dbstorage2():
    """Fixture for DBStorage"""
    dbstorage = DBStorage()

    yield dbstorage

    dbstorage.close()

@pytest.fixture(scope='function', autouse=True)
def person():
    """Fixture for TestPerson"""
    return TestPerson(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone_number="123-456-7890",
        birth_date=datetime(1990, 5, 21),
        gender=Gender.MALE,
        address="123 Main St",
        city="Springfield",
        state="IL",
    )

@pytest.fixture(scope='function', autouse=True)
def cat():
    """Fixture for TestCat"""
    return TestCat(
        name='Whiskers',
        breed='Siamese',
        age=3,
        birth_date=datetime(2020, 6, 15),
        gender=Gender.FEMALE,
        owner_name='Alice',
    )

@pytest.fixture(scope="session", autouse=True)
def clean_db():
    """ Ensures the database is cleaned after each test """
    yield
    dbstorage = DBStorage()

    dbstorage.get_session().query(TestPerson).delete()
    dbstorage.get_session().query(TestCat).delete()

    dbstorage.save()
