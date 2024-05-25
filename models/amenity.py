#!/usr/bin/python3
""" Anenity class definition """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Represents an amenity offered by places in the application.

    Attributes:
        name (str): The name of the amenity. (Required)
        place_amenities (list[Place], read-only): List of Place instances
        associated with the amenity. (Many-to-Many)
    """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
