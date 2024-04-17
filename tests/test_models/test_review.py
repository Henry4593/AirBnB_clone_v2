#!/usr/bin/python3
""" Unit tests for the Review class from the models module."""
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place
from models.user import User
from models.review import Review


class test_review(test_basemodel):
    """ Test suite for the Review class, inheriting from TestBaseModel"""

    def __init__(self, *args, **kwargs):
        """ Initialize the TestReview instance."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test the place_id attribute of the Review class."""
        new = self.value()
        place = Place()
        new.place_id = place.id
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test the user_id attribute of the Review class."""
        new = self.value()
        user = User()
        new.user_id = user.id
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test the text attribute of the Review class."""
        new = self.value()
        new.text = ""
        self.assertEqual(type(new.text), str)
