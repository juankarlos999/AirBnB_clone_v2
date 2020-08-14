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
                      Column('places.id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenities.id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Is a class to hold a place """
 
    amenity_ids = []
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
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances
            """
            all_reviews = models.storage.all(Review)
            amenity_ids = [review for review in all_reviews
                      if review.place_id == self.id]
            return amenity_ids

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances
            """
            from models.amenity import Amenity
            result = []
            all_amenities = models.storage.all().items()
            for key, val in all_amenities:
                if  val.__class__.__name__ == "Amenity":
                    if val.place_id == self.id:
                        result.append(val)
            return result

        @amenities.setter
        def amenities(self, amenity_):
            """
            Setter attribute amenities
            """
            from models.amenity import Amenity
            if isinstance(amenity_, Amenity):
                self.amenity_ids.append(amenity_.id)
