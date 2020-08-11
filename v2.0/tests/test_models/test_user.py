#!/usr/bin/python3
"""
Contains the TestUser class

"""

from datetime import datetime
from models import user
from models.base_model import BaseModel
import unittest
User = user.User


class TestUser(unittest.TestCase):
    """testing the subclass User"""
    def test_subclass(self):
        """Testing if User inherits of BaseModel"""
        ins = User()
        self.assertIsInstance(ins, BaseModel)
        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_str(self):
        """testing the correct output with a subclass"""
        instancia = User()
        string = "[User] ({}) {}".format(instancia.id, instancia.__dict__)
        self.assertEqual(string, str(instancia))

    def test_email(self):
        """testing if a subclass had a ins(email) and if this is empty"""
        inst = User()
        self.assertEqual(inst.email, "")
        self.assertTrue(hasattr(inst, "email"))

    def test_password(self):
        """testing if a subclass had a ins(password) and if this is empty"""
        c = User()
        self.assertEqual(c.password, "")
        self.assertTrue(hasattr(c, "password"))

    def test_first_name(self):
        """testing if a subclass had a ins(first_name) and if this is empty"""
        w = User()
        self.assertEqual(w.first_name, "")
        self.assertTrue(hasattr(w, "first_name"))

    def test_last_name(self):
        """testing if a subclass had a ins(last_name) and if this is empty"""
        z = User()
        self.assertTrue(hasattr(z, "last_name"))
        self.assertEqual(z.last_name, "")

    def test_dict(self):
        """testing the type of a instance"""
        instancia = User()
        dicc = instancia.to_dict()
        self.assertEqual(type(dicc), dict)
