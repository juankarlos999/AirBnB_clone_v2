#!/usr/bin/python3
"""
Contains the Test_StateState classes
"""

from datetime import datetime
from models import state
from models.base_model import BaseModel
import unittest
State = state.State


class Test_StateState(unittest.TestCase):
    """Testing class StateState"""

    def test_subclass(self):
        """Testing if State inherits of BaseModel"""
        ins = State()
        self.assertIsInstance(ins, BaseModel)
        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_methodworks(self):
        """ Check the instance"""
        instancia = State()
        time = instancia.updated_at
        instancia.save()
        self.assertTrue(time != instancia.updated_at)
        self.assertTrue(type(instancia.__str__()) is str)
        self.assertTrue(type(instancia.to_dict()) is dict)

    def test_name(self):
        """testing the attr name"""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "name"))

    def test_dicts(self):
        """This willl test the dicts"""
        stado = State()
        dictonary = stado.to_dict()
        self.assertTrue(type(dictonary) == dict)
        self.assertTrue(dictonary['__class__'] == 'State')
        self.assertTrue(type(dictonary["id"]) == str)
        self.assertTrue(type(dictonary["created_at"]) == str)
        self.assertTrue(type(dictonary["updated_at"]) == str)
        # stado.save()
        # self.assertEqual(type(stado.created_at), datetime)
        # self.assertEqual(type(stado.update_at), datetime)

    def test_dictonary(self):
        """This will test the kward"""
        new_dict = {'id': 'Un id super random',
                    'email': 'holberton@gmail.perro', 'age': 1}
        stado = State(**new_dict)
        self.assertEqual(stado.id, 'Un id super random')

    def test_str(self):
        """testing the correct output with a subclass"""
        instancia = State()
        string = "[State] ({}) {}".format(instancia.id, instancia.__dict__)
        self.assertEqual(string, str(instancia))

    def test_dict(self):
        """testing the type of a instance"""
        instancia = State()
        dicc = instancia.to_dict()
        self.assertEqual(type(dicc), dict)
