#!/usr/bin/python3
"""Chooses and instantiates a storage engine based on environment.
If 'HBNB_TYPE_STORAGE' is set to 'db', uses a database storage engine.
Otherwise, defaults to a file system storage engine.
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
