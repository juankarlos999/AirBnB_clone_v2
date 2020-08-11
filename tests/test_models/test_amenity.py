#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel
import unittest


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


    def test_subclass(self):
        """Testing if Amenity inherits of BaseModel"""
        ins = Amenity()
        self.assertIsInstance(ins, BaseModel)
        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_str(self):
        """testing the correct output with a subclass"""
        instancia = Amenity()
        string = "[Amenity] ({}) {}".format(instancia.id, instancia.__dict__)
        self.assertEqual(string, str(instancia))

    def test_name(self):
        """testing if a subclass had a ins(name) and if this is empty"""
        inst = Amenity()
        self.assertEqual(inst.name, "")
        self.assertTrue(hasattr(inst, "name"))

    def test_dict(self):
        """testing the type of a instance"""
        instancia = Amenity()
        dicc = instancia.to_dict()
        self.assertEqual(type(dicc), dict)