#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String, Integer, Float, ForeignKey, Table)
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


# Add an instance of SQLAlchemy Table called place_amenity
# for creating the relationship Many-To-Many between Place and Amenity:
class Place_amenity(Base):
    __tablename__ = "place_amenity"
    place_id = Column(
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True)
    amenity_id = Column(
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True)



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
    reviews = relationship("Review", backref="place")
    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        backref="place_amenities",
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
        amenity = [amenaty for amenaty in all_amenities if amenity.place_id == self.id]
        return amenity
