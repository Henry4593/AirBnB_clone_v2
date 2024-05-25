#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """Initializes the test class instance, calling the base class
        constructor and setting up test-specific attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Verifies that a newly created Amenity instance has a name attribute
        of type string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
