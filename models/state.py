#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import (Column, ForeignKey, String)
from sqlalchemy.orm import relationship
from models.city import City
import os
from models import storage


class State(BaseModel):
    """ State class
    returns the list of City instances with state_id equals to the
    current State.id"""
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        @cities.setter
        def cities(self):
            """This function: getter attribute cities that returns the list of
            City instances with state_id equals to the current State.id => It
            will be the FileStorage relationship between State and"""
            cities = storage.all(City)
            result = []
            for city in cities.values():
                if self.id == city.state_id:
                    result.append(city)

            return result
