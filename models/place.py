#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String, Integer, Float, ForeignKey, Table)
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


place_amenity = Table('association', Base.metadata,
                      Column('places.id', Integer, ForeignKey('places.id')),
                      Column('amenities.id', Integer,
                             ForeignKey('amenities.id'))
                      )


class Place(BaseModel, Base):
    """ Is a class to hold a place """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    price_by_night = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False)


@property
def reviews(self):
    """getter attribute returns the list of Review instances
    """
    all_reviews = models.storage.all(Review)
    review = [review for review in all_reviews if review.place_id == self.id]
    return review


@property
def amenities(self):
    """getter attribute returns the list of Amenity instances
    """
    from models.amenity import Amenity
    all_amenities = models.storage.all(Amenity)
    amenity = [amenaty for amenaty in all_amenities
               if amenity.place_id == self.id]
    return amenity
