#!/usr/bin/python3
""" Unit tests for the User class from the models module."""
from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class test_User(test_basemodel):
    """ Test suite for the User class, inheriting from TestBaseModel."""

    def __init__(self, *args, **kwargs):
        """ Initialize the TestUser instance."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test the first_name attribute of the User class."""
        new = self.value()
        new.first_name = "Abissa"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test the last_name attribute of the User class."""
        new = self.value()
        new.last_name = "Abissa"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test the email attribute of the User class."""
        new = self.value()
        new.email = "a.sani@alustudent.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test the password attribute of the User class."""
        new = self.value()
        new.password = "123aashja"
        self.assertEqual(type(new.password), str)
