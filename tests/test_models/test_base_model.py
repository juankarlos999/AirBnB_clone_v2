#!/usr/bin/python3
"""Unittest for the test"""
import unittest
from models.base_model import BaseModel
import time
from datetime import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)


    @unittest.skip("demonstrating skipping")
    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
    def test_id0(self):
        """this will test the id attribute"""
        # [<class name>] (<self.id>) <self.__dict__>
        a = BaseModel().id
        self.assertTrue(type(a) == str)
        self.assertTrue(type(BaseModel().id) == str)

    def test_id1(self):
        """ This will test the id attribute"""
        self.assertGreater(len(BaseModel().id), 35)

    def test_create0(self):
        """ This will test the variable created"""
        a = BaseModel()
        a.save()
        self.assertFalse(isinstance(type(a.created_at), type(datetime.now())))

    def test_create1(self):
        """ This will test the variable created"""
        self.assertFalse(
            isinstance(type(BaseModel().created_at), type(datetime.now()))
            )

    def test_updated0(self):
        """ This will test the variable update"""
        a = BaseModel()
        self.assertEqual(type(a.updated_at), type(datetime.now()))

    def test_updated1(self):
        """ This will test the variable update"""
        self.assertFalse(type(BaseModel().updated_at) == str)

    def test_save0(self):
        """check the erros in the method"""
        with self.assertRaises(AttributeError):
            BaseModel.save([1, 2, 3])

    def test_save1(self):
        """check the erros in the method"""
        with self.assertRaises(AttributeError):
            BaseModel.save("HELLO MUNDO")

    def test_str(self):
        '''Testing str method : correct output'''
        i = BaseModel()
        string = "[BaseModel] ({}) {}".format(i.id, i.__dict__)
        self.assertEqual(string, str(i))

    def test_format_dict(self):
        '''test that the return values are correct of      to_dict()
        '''
        j = BaseModel()
        new = j.to_dict()
        self.assertEqual(new["__class__"], "BaseModel")
        self.assertEqual(type(new["created_at"]), str)
        self.assertEqual(type(new["updated_at"]), str)
        self.assertNotEqual(new["created_at"], j.created_at)
        self.assertNotEqual(new["updated_at"], j.updated_at)

    def test_insta(self):
        """ testing the models of the class """
        model = BaseModel()
        self.assertTrue(model, BaseModel)



    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        f = "%Y-%m-%dT%H:%M:%S.%f"
        ins = BaseModel()
        new_d = ins.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        # self.assertEqual(new_d["created_at"], ins.created_at.strftime(f))
        # self.assertEqual(new_d["updated_at"], ins.updated_at.strftime(f))

    def test_dict(self):
        '''testing conversion dict to json'''
        model = BaseModel()
        model.name = 'hbtn'
        model.number = 18
        dictionary = model.to_dict()
        attrs = ['id',
                 "created_at",
                 "updated_at",
                 "name",
                 "number",
                 "__class__"]
        # self.assertCountEqual(a.keys(), attrs) TODO
        for attr in attrs:
            self.assertTrue(attr in dictionary)
        # self.assertDictEqual(a, attrs)
        # self.assertTrue(type(BaseModel().to_dict()) == type(dict))
        self.assertTrue(isinstance(model, BaseModel))
        self.assertEqual(dictionary['__class__'], "BaseModel")
        self.assertEqual(dictionary['name'], 'hbtn')
        self.assertEqual(dictionary['number'], 18)
        with self.assertRaises(TypeError):
            model.to_dict(attrs)

    def test_time(self):
        """testing mode time"""
        model = BaseModel()
        self.assertIsNotNone(model.updated_at)
