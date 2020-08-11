#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    def _init_(self, **kwargs):
        """
        Method constructor with **kwargs
        """
        for key, value in kwargs.items():

            if key == "_class_":
                continue

            if key in "created_at" or key in "updated_at":
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

            if key not in "_class_":
                setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()

        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
