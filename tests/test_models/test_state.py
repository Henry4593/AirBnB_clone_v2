#!/usr/bin/python3
""" Unit tests for the State class from the models module"""
from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class test_state(test_basemodel):
    """ Test suite for the State class, inheriting from TestBaseModel."""

    def __init__(self, *args, **kwargs):
        """ Initialize the TestState instance."""
        super().__init__(*args, **kwargs)
        self.name = "Carlifornia"
        self.value = State

    def test_name3(self):
        """ Test the name attribute of the State class."""
        new = self.value()
        new.name = "Arizona"
        self.assertEqual(type(new.name), str)
