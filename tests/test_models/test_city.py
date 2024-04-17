#!/usr/bin/python3
""" Unit tests for the City class from the models module. """
from models.state import State
from tests.test_models.test_base_model import TestBasemodel
from models.city import City


class test_City(test_basemodel):
    """Test suite for the City class, inheriting from test_basemodel"""

    def __init__(self, *args, **kwargs):
        """ Initialize the test_City instance."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test the state_id attribute of the City class."""
        state = State()
        new = self.value()
        new.state_id = state.id
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Test the name attribute of the City class."""
        new = self.value()
        new.name = "Batch"
        self.assertEqual(type(new.name), str)
