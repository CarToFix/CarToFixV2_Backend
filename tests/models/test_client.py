""" This module contains the test for class client

Tested by: Emanuel Trias
"""

import inspect

import pytest

from . import Client
from . import Vehicle


class TestClient:
    """ This class defines the tests for client class """

    @pytest.fixture(autouse=True)
    def test_setup(self):
        """ Sets up the necessary variables for the execution of future tests """
        self.client = Client("Elizabeth", "el@gmail.com", "032900938")

    def test_docstrings(self):
        """ Checks for docstrings present in module, class and methods of Client 
            - docstrings must be present
            - docstrings lines must equals or greater than number of parameters + 1
        """

        def count_parameters(method):
            """ Counts the number of parameters for a given method but self """
            parameters = inspect.signature(method).parameters
            return len([param for param in parameters.values() if param.name != 'self'])

        # Getting class docstrings
        class_docstring = inspect.getdoc(Client)
        class_docstring_lines = len(class_docstring.split('\n')) if class_docstring else 0

        # Getting methods docstrings and count of parameters
        mname = []
        mdocs_lines = []
        param_counts = []
        for name, method in inspect.getmembers(Client, predicate=inspect.isfunction):
            method_docs = inspect.getdoc(method)
            mdocs_lines.append(len(method_docs.split('\n')) if method_docs else 0)

            params_count = count_parameters(method)
            param_counts.append(params_count)
            mname.append(name)

        # Client has enough docstring lines
        no_lines = "Client class docstring has no enough lines"
        assert class_docstring_lines >= 1, no_lines

        # Client methods have enough docstrings
        for mname, mdocs, params in zip(mname, mdocs_lines, param_counts):
            mno_docs = f"Method {mname} has {mdocs} lines of docstring, were expected: at least {params + 1}"
            assert mdocs >= params + 1, mno_docs

    def test_methods(self):
        """ Checks for the methods to work as expected """
        client = self.client

        # Setter methods
        nname = "Jane Doe"
        nmail = "janedoe@gmail.com"
        nphone = "34593485934"
        nvehicle = [Vehicle()]

        client.name = nname
        client.mail = nmail
        client.tel = nphone
        client.vehicles = nvehicle

        # Assertions for all methods
        assert client.name == nname, "New name coudln't be set for Client"
        assert client.mail == nmail, "New mail coudln't be set for Client"
        assert client.tel == nphone, "New phone coudln't be set for Client"
        assert client.vehicles == nvehicle, "New vehicles coudln't be set for Client"
        assert isinstance(client.to_dict(), dict), "Client to_dict method is not returning a dict"

    def test_set_strings(self):
        """ Checks whether attributes can be set as strings """
        self.client.name = "A NAME"
        self.client.mail = "amail@gmail.com"
        self.client.tel = "230948098"

        with pytest.raises(TypeError):
            self.client.vehicles = str([Vehicle()])

    def test_set_ints(self):
        """ Checks that attributes cannot be set as ints """
        with pytest.raises(TypeError):
            self.client.vehicles = 92
        with pytest.raises(TypeError):
            self.client.tel = 89
        with pytest.raises(TypeError):
            self.client.mail = 998
        with pytest.raises(TypeError):
            self.client.name = 82

    def test_set_symbols(self):
        """ Checks that attributes cannot be set as strings with symbols """
        with pytest.raises(ValueError):
            self.client.name = "!@#$%^&*()_+= {}[]|\\:;Anna\"'<>,.?/0123456789±÷×∑√∫∞≠∇∆\n\t"
        with pytest.raises(ValueError):
            self.client.tel = "!@#$%^&*()_+={ }[]|\\:;\"'<>,.?/abcdefghijklmnoprstuvwxyz±÷×∑√∫∞≠∇∆\n\t"
        with pytest.raises(ValueError):
            self.client.tel = "!@#$%^&*()_+={ }[]|\\:;\"'<>,.?/abcdefghijklmnoprstuvwxyz±÷×∑√∫∞≠∇∆\n\t".upper()
        with pytest.raises(ValueError):
            self.client.mail = "!#$%^&*()_+={}[]|\\:;\"'<>,?/±÷×∑√∫∞≠∇∆\n\t@."

    def test_set_invalid_email(self):
        """ Checks that invalid email raises error """
        with pytest.raises(ValueError):
            self.client.mail = "annasmail@gmailcom"
        with pytest.raises(ValueError):
            self.client.mail = "annasmailgmail.com"
