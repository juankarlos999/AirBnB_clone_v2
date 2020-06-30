#!usr/bin/python3
""" This is the main class """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Is the main class """

    time = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """ is where the instacne Attribute is init"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if (key == "updated_at" or key == "created_at"):
                        value = datetime.strptime(value, self.time)
                    setattr(self, key, value)

        # if hasattr(self, "created_at") and type(self.created_at) is str:
        #     self.created_at =
        #   datetime.strptime(kwargs["created_at"], self.time)
        # if hasattr(self, "updated_at") and type(self.updated_at) is str:
        #     self.updated_at =
        #   datetime.strptime(kwargs["updated_at"], self.time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ It will return the information of the class object"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """ It will update the data time of the current directory """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ It will return a dictionary """
        # hace una nueva copia del dictionario
        new_dict = {**self.__dict__}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
