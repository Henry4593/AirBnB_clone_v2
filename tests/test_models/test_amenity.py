#!/usr/bin/python3
"""this is a amenity class """
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test for amenity """

    def __init__(self, *args, **kwargs):
        """Initialize the TestAmenity instance. """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test the type of the name attribute in the Amenity instance. """
        new = self.value()
        new.name = "amenity"
        self.assertEqual(type(new.name), str)
