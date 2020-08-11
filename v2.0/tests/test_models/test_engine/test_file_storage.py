#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

import unittest
from datetime import datetime
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

FileStorage = file_storage.FileStorage
clases = {"Amenity": Amenity, "BaseModel": BaseModel,
          "City": City, "Place": Place, "Review": Review,
          "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class"""
    def test_all_returns_dict(self):
        """Testing that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_d = storage.all()
        self.assertEqual(type(new_d), dict)
        self.assertIs(new_d, storage._FileStorage__objects)

    def test_new(self):
        """testing that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        test_dict = {}
        for key, value in clases.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        storage._FileStorage__objects = {}
