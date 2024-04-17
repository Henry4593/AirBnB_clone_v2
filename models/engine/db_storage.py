#!/usr/bin/python3
"""Database Storage Management for AirBnB
Connects to the MySQL database and provides functions to interact
with the data using SQLAlchemy. This class employs a single database
session for efficiency and manages the connection to the engine.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Facilitates interactions with the MySQL database.
    Attributes:
        __engine (sqlalchemy.engine.Engine): The underlying connection to the
                        database.
        __session (sqlalchemy.orm.session.Session): The current active database
                        session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the connection to the MySQL database."""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        mysql_env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_pwd, mysql_host, mysql_db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        
        """DROP ALL TABLES"""
        if mysql_env == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Retrieves all or specific objects from the database.
        Args:
            cls (class, optional): The class of objects to retrieve.
                If None, returns all classes. Defaults to None.

        Returns:
            dict: A dictionary containing the retrieved objects in the format
                <class name>.<obj id> = obj.
        """
        if cls:
            objs = self.__session.query(cls).all()

        else:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for cls in classes:
                objs += self.__session.query(cls)

        """create and save data"""
        new_dict = {}

        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """Schedules an object to be added to the database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all pending changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Schedules an object to be removed from the database session.
        Args:
            obj (object, optional): The object to be deleted. Defaults to None
            (no deletion).
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Terminates the current database session."""
        self.__session.close()

    def reload(self):
        """Creates all database tables (if needed) and starts a new session."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

