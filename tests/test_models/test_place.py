#!/usr/bin/python3
""" """
from models.city import City
from models.user import User
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test suite for the Place class, inheriting from TestBaseModel."""

    def __init__(self, *args, **kwargs):
        """ Initialize the TestPlace instance."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test the city_id attribute of the Place class."""
        new = self.value()
        city = City()
        new.city_id = city.id
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test the user_id attribute of the Place class."""
        new = self.value()
        user = User()
        new.user_id = user.id
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test the name attribute of the Place class."""
        new = self.value()
        new.name = "Place"
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test the description attribute of the Place class."""
        new = self.value()
        new.description = ""
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test the number_rooms attribute of the Place class."""
        new = self.value()
        new.number_rooms = 4
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test the number_bathrooms attribute of the Place class."""
        new = self.value()
        new.number_bathrooms = 2
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test the max_guest attribute of the Place class."""
        new = self.value()
        new.max_guest = 8
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test the price_by_night attribute of the Place class."""
        new = self.value()
        new.price_by_night = 18
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test the latitude attribute of the Place class."""
        new = self.value()
        new.latitude = -123.085222
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test the longitude attribute of the Place class."""
        new = self.value()
        new.longitude = -120.08522
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ Test the amenity_ids attribute of the Place class."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
