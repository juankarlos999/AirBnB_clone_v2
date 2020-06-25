#!/usr/bin/python3
""" aca es la base principal de todo """
import uuid
from datetime import datetime


class BaseModel():
    """
    la base principal de todo
    """

    # hola Peer
    def __init__(self, *args, **kwargs):
        """ Is where the class is going to init the var
        and keep track the init method """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ It will return the information of the class object"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        method that returns a dictionary (key/value)"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = self.created_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()
        return self.__dict__
