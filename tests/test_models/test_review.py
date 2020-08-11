#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel

from models import review
from datetime import datetime
from models.base_model import BaseModel
import unittest
Review = review.Review

class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_subclass(self):
        """Testing if Review inherits of BaseModel"""
        ins = Review()
        self.assertIsInstance(ins, BaseModel)
        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_str(self):
        """testing the correct output with a subclass"""
        instancia = Review()
        string = "[Review] ({}) {}".format(instancia.id, instancia.__dict__)
        self.assertEqual(string, str(instancia))

    def test_user_id(self):
        """testing if a subclass had a ins(user_id) and if this is empty"""
        inst = Review()
        self.assertEqual(inst.user_id, "")
        self.assertTrue(hasattr(inst, "user_id"))

    def test_place_id(self):
        """testing atrr place_id"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_dict(self):
        """testing the type of a instance"""
        instancia = Review()
        dicc = instancia.to_dict()
        self.assertEqual(type(dicc), dict)

    def test_text(self):
        """ Testing the attribute txt"""
        instance = Review()
        self.assertTrue(type(instance.text) is str)
        self.assertEqual(instance.text, '')
        self.assertTrue(hasattr(instance, "text"))

    def test_methodworks(self):
        """ Check the instance"""
        instancia = Review()
        time = instancia.updated_at
        instancia.save()
        self.assertTrue(time != instancia.updated_at)
        self.assertTrue(type(instancia.__str__()) is str)
        self.assertTrue(type(instancia.to_dict()) is dict)