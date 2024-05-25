#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

time = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Core data object for hbnb, offering lifecycle management.

    Attributes:
        id (str): Unique identifier (UUID). (Primary Key)
        created_at (datetime): Creation timestamp (UTC).
        updated_at (datetime): Last update timestamp (UTC).
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializes a new model instance.

        Args:
            kwargs (dict, optional): Key-value pairs for attributes.
                If not provided, sets id, created_at, and updated_at to
                current values.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{:s}] ({:s}) {}'.format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates updated_at and saves the instance."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance.
        Includes type information, formatted timestamps, and removes internal
        attributes.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        if "created_at" in dictionary:
            dictionary['created_at'] = self.created_at.isoformat()
        if "updated_at" in dictionary:
            dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Deletes the instance from storage."""
        from models import storage
        storage.delete(self)
