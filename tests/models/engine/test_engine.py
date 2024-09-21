""" Tests for the class DBStorage

Requires:
    - Pylint

Created By:
    - Emanuel Trias
"""

import pytest
import random
from datetime import datetime

from .person_test_class import TestPerson, TestCat, Gender


class TestDBStorage:
    """ Defines all the test for DBStorage """

    def test_hasattr(self, dbstorage):
        """ Checks for the expected attributes and methods to be present in DBStorage """
        assert hasattr(dbstorage, "_DBStorage__engine")
        assert hasattr(dbstorage, "new")
        assert hasattr(dbstorage, "all")
        assert hasattr(dbstorage, "save")
        assert hasattr(dbstorage, "delete")
        assert hasattr(dbstorage, "reload")
        assert hasattr(dbstorage, "get")
        assert hasattr(dbstorage, "close")
        assert hasattr(dbstorage, "count")

    def test_new_save(self, dbstorage, dbstorage2, person):
        """ Checks new() method meets expected behavior """

        person_before = dbstorage.get_session().query(TestPerson).all()
        dbstorage.new(person)
        person_now = dbstorage.get_session().query(TestPerson).all()

        # Assert there is exactly one person more in the list
        assert len(person_now) == len(person_before) + 1
        
        # First person in the list
        person = person_now[0]

        # Assert the string representation matches "John-Doe"
        assert str(person) == "John-Doe"

        # Assert person was saved in the db
        dbstorage.save()
        db_persons = dbstorage2.get_session().query(TestPerson).filter_by(oid=person.oid).all()

        # Assert that the person is now in the database
        assert len(dbstorage2.get_session().query(TestPerson).all()) == len(person_now)
        assert str(db_persons[0]) == "John-Doe"

    def test_all(self, dbstorage, cat, person):
        """ Checks all method returns all the instances of a table """
        # All the objects in the db
        dbstorage.new(cat)
        dbstorage.new(person)
        dbstorage.save()

        all_instances = dbstorage.all()
        classes = {inst.__class__.__name__ for _, inst in all_instances.items()}

        # Length of the dictionary returned by dbstorage.all must be greater than 2
        assert len(all_instances) > 1

        # There must be at least two different classes within the dictionary
        assert len(all_instances) > 1

    def test_get(self, dbstorage, dbstorage2, cat):
        """ Checks get method fetches only one element by class and id """
        dbstorage.new(cat)
        dbstorage.save()

        # Random object is retireved from session, and fetched by get method
        obj = random.choice(dbstorage2.get_session().query(cat.__class__).all())
        dup_obj = dbstorage.get(obj.__class__, obj.oid)

        assert obj == dup_obj, "Objects are not equal"

    def test_delete(self, dbstorage, dbstorage2, person):
        """ Tests for delete method """
        dbstorage.new(person)
        dbstorage.save()

        # Person must exist
        assert dbstorage2.get_session().query(TestPerson).filter_by(oid=person.oid).all()

        dbstorage.delete(person)
        dbstorage.save()

        # Person has been removed
        assert not dbstorage2.get_session().query(TestPerson).filter_by(oid=person.oid).all()

    def test_count(self, dbstorage):
        """ Tests for count method """
        for _ in range(10):
            nperson = TestPerson(
                first_name=random.choice(["John", "Michael", "David", "James", "Robert"]),
                last_name=random.choice(["Doe", "Smith", "Johnson", "Brown", "Davis"]),
                email=random.choice([
                    "john.doe@example.com",
                    "james.brown@example.com",
                ]),
                phone_number=random.choice([
                    "123-456-7890", 
                    "567-890-1234"
                ]),
                birth_date=random.choice([
                    datetime(1990, 5, 21),
                    datetime(1992, 11, 30),
                ]),
                gender=random.choice([Gender.MALE, Gender.FEMALE]),
                address=random.choice([
                    "123 Main St", 
                    "202 Cedar Ln"
                ]),
                city=random.choice([
                    "Springfield", 
                    "Lincoln"
                ]),
                state=random.choice([
                    "state1", 
                    "state5"
                ]),
            )

            dbstorage.new(nperson)

        dbstorage.save()

        assert dbstorage.count(TestPerson) == 10 + 2

    def test_close(self, dbstorage, dbstorage2, cat):
        """ Tests for close method """
        prevcats = dbstorage.count(TestCat)
        dbstorage2.new(cat)
        dbstorage2.close()
        dbstorage2.save()

        assert dbstorage.count(TestCat) == prevcats
