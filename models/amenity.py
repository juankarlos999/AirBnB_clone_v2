#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref



class Amenity(BaseModel, Base):
    """The amenaty of the place"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

