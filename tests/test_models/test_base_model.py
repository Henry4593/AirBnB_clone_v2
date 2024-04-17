#!/usr/bin/python3
""" Unit test suite for the BaseModel class from the models module."""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Test suite for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """ Initialize the TestBaseModel instance."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up the test case environment."""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ This test ensures that a new instance is of type BaseModel."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test instantiation with keyword arguments."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test instantiation with an integer as a keyword argument key."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_todict(self):
        """ Test the to_dict method of the BaseModel class."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test instantiation with None as a keyword argument key."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ Test the id attribute of the BaseModel class."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test the created_at attribute of the BaseModel class."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test the updated_at attribute of the BaseModel class."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertAlmostEqual(new.created_at.timestamp(),
                               new.updated_at.timestamp(), delta=1)
