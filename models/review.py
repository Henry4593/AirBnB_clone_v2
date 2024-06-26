#!/usr/bin/python3
"""This module defines the `Review` class, which represents a user review for
a place in the application.

The `Review` class inherits from the `BaseModel` class and provides data
validation for review data.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from os import getenv


class Review(BaseModel, Base):
    """Represents a user review for a place in the application.

    Attributes:
        text (str): The content of the review.
        place_id (str): The ID of the associated place.
        user_id (str): The ID of the user who wrote the review.
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=True)
        text = Column(String(1024), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
