#!/usr/bin/python3
""" Class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances. """
import json


class FileStorage:
    """ Class that serializes and deserializes JSON file. """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary. """
        return type(self).__objects

    def new(self, obj):
        """ add a dictionary """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """ Serializes to JSON file. """
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        '''Deserializes JSON file to dict with obj instances if file exists'''
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, mode='r') as f:
                json_to_dict = json.load(f)
            for key, value in json_to_dict.items():
                new = BaseModel(**value)
                self.__objects[key] = new
        except FileNotFoundError:
            pass
