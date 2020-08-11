#!/usr/bin/python3
"""
Contains the Test_StateState classes
"""

from datetime import datetime
from models import state
from tests.test_models.test_base_model import test_basemodel
import unittest
State = state.State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
    def test_subclass(self):
        """Testing if State inherits of BaseModel"""
        ins = State()

        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_methodworks(self):
        """ Check the instance"""
        instancia = State()
        time = instancia.updated_at
        instancia.save()

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