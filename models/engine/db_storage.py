#!/usr/bin/python3
""" Make your code running without knowing how it’s stored. """
from sqlalchemy.engine.url import URL
from models.base_model import Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, scoped_session)
import os


class DBStorage:
    """This is for manage the enginee """
    __engine = None
    __session = None

    def __init__(self):
        """ Init the variable to init the enginee """
        # Retrive variables
        db_connect = {
            'drivername': 'mysql',
            'username': os.getenv('HBNB_MYSQL_USER'),
            'password': os.getenv('HBNB_MYSQL_PWD'),
            'host': os.getenv('HBNB_MYSQL_HOST'),
            'database': os.getenv('HBNB_MYSQL_DB')
        }

        self.__engine = create_engine(URL(**db_connect), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ create all tables in the database and
        create the current database session (self.__session) from the
        engine (self.__engine)"""

        # all classes who inherit from Base
        # must be imported before calling Base.metadata.create_all(engine)
        Session_m = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # autoflush=True
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(Session_m)
        self.__session = Session()

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def all(self, cls=None):
        """ This method is for retrive information from
        other data base"""

        if cls:
            for state in session.query(cls).order_by('id').all():
                print('{}: {}'.format(cls.id, cls.name))
        else:
            return {}

        # key = <class-name>.<object-id>
        # value = object
