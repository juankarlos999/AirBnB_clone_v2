#!/usr/bin/python3
"""
Contains the TestCity class

"""

from datetime import datetime
from models import city
from models.base_model import BaseModel
import unittest
City = city.City


class TestCity(unittest.TestCase):
    """testing the subclass City"""
    def test_subclass(self):
        """Testing if City inherits of BaseModel"""
        ins = City()
        self.assertIsInstance(ins, BaseModel)
        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_str(self):
        """testing the correct output with a subclass"""
        instancia = City()
        string = "[City] ({}) {}".format(instancia.id, instancia.__dict__)
        self.assertEqual(string, str(instancia))

    def test_name(self):
        """testing if a subclass had a ins(name) and if this is empty"""
        inst = City()
        self.assertEqual(inst.name, "")
        self.assertTrue(hasattr(inst, "name"))

    def test_state_id(self):
        """testing if a subclass had a ins(state_id) and if this is empty"""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertTrue(hasattr(c, "state_id"))

    def test_dict(self):
        """testing the type of a instance"""
        instancia = City()
        dicc = instancia.to_dict()
        self.assertEqual(type(dicc), dict)
