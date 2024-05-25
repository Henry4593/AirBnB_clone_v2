#!/usr/bin/python3
"""State Module for HBNB project. This module defines the `State` class
representing a state in the application.
"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """Represents a state in the application.

    Attributes:
        name (str): The name of the state. (Required)
        cities (list[City], read-only): List of City instances belonging
        to the state.
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Returns the list of City
            """
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
