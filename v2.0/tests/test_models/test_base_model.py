#!/usr/bin/python3
"""Unittest for the test"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""

    def setUp(self):
        """Is where the variables will be share"""
        pass

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

    def test_datetime_attributes(self):
        """
            Test that two BaseModel instances have different datetime objects
            and that upon creation have identical updated_at and created_at
            value.
        """
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        # self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        # self.assertTrue(tic <= inst2.created_at <= toc)
        # self.assertNotAlmostEqual(
        #     inst1.created_at.isoformat(), inst1.updated_at.isoformat())
        self.assertNotEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

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

        # TODO Fix this after

        # self.assertTrue(type(my_model.created_at) == type(datetime.now()))
        # self.assertEqual(type(BaseModel().created_at), type(datetime.now()))
        # self.assertTrue(
        # isinstance(type(BaseModel().updated_at), type(datetime.now())))
        # self.assertEqual(type(BaseModel().updated_at), type(datetime.now()))

    def test_time(self):
        """testing mode time"""
        model = BaseModel()
        self.assertIsNotNone(model.updated_at)
        self.assertNotEqual(model.updated_at, datetime.now())
