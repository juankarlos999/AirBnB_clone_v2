#!usr/bin/python3
""" This is the main class """
import uuid
from datetime import datetime
import models

time = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel():
    """ Is the main class """

    def __init__(self, *args, **kwargs):
        """ is where the instacne Attribute is init"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
            # if key == 'updated_at' and value is not str:
            # value = datetime.strptime#(value,
            # '%Y-%m-%dT%H:%M:%S.%f')
            # if key == 'created_at' and value is not str:
            # value = datetime.strptime#(value,
            # '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """ It will return the information of the class object"""
        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                          self.__dict__))

    def save(self):
        """ It will update the data time of the current directory """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ It will return a dictionary """
        new_dict = self.__dict__
        if 'created_at' in new_dict:
            if type(new_dict["created_at"]) is not str:
                new_dict["created_at"] = new_dict["created_at"].strftime(time)
            else:
                new_dict["created_at"] = new_dict["created_at"]
        if 'updated_at' in new_dict:
            if type(new_dict["updated_at"]) is not str:
                new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
            else:
                new_dict["updated_at"] = new_dict["updated_at"]
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

# self.__dict__['__class__'] = #self.__class__.__name__
# self.__dict__['created_at'] = self.created_at.isoformat()
# self.__dict__['updated_at'] = #self.updated_at.isoformat()
# return self.__dict__
