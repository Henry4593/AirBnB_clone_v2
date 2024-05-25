#!/usr/bin/python3
"""File Storage Management System
Provides an abstraction layer for storing and retrieving application objects.
Uses JSON format to serialize and deserialize data to a file.
"""
import models
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Facilitates object persistence using a JSON file.
    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary holding all instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Retrieves all or specific objects from storage.
        Args:
            cls (class, optional): The class of objects to retrieve.
                If None, returns all objects. Defaults to None.

        Returns:
            dict: A dictionary containing the retrieved objects.
                If a class is specified, only objects of that class are
                returned.
        """
        if cls is None:
            return self.__objects
        else:
            my_dict = {}
            for key in self.__objects:
                name = key.split('.')
                if name[0] == cls.__name__:
                    my_dict[key] = self.__objects[key]
            return my_dict

    def new(self, obj):
        """Schedules an object to be added to the storage.
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes all objects in storage to the JSON file."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Loads objects from the JSON file back into storage
        (if it exists).
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Schedules an object to be removed from storage (if it exists)."""
        if obj:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def close(self):
        """Reloads objects from the JSON file on program termination."""
        self.reload()
