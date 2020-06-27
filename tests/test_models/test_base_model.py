#!/usr/bin/python3
"""Unittest for the test"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""

    def setUp(self):
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
        self.assertTrue(type(a.created_at) == type(datetime.now()))

    def test_create1(self):
        """ This will test the variable updated"""
        self.assertFalse(type(BaseModel().created_at) == str)

    def test_updated0(self):
        """ This will test the variable update"""
        a = BaseModel()
        self.assertEqual(type(a.updated_at), type(datetime.now()))

    def test_updated1(self):
        """ This will test the variable update"""
        self.assertTrue(type(BaseModel().updated_at) == str)

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
        self.assertEqual(new["created_at"], j.created_at)
        self.assertEqual(new["updated_at"], j.updated_at)

    def test_insta(self):
        """ testing the models of the class """
        model = BaseModel()
        new_model = BaseModel()
        self.assertTrue(model is new_model)

    def test_dict(self):
        '''testing conversion dict to json'''
        model = BaseModel()
        model.name = 'hbtn'
        model.number = 18
        a = model.to_dict()
        attrs = ['id',
                 "created_at",
                 "updated_at",
                 "name",
                 "my_number",
                 "__class__"]
        self.assertCountEqual(a.keys(), attrs)
        self.assertDictEqual(a, attrs)
        self.assertTrue(type(BaseModel.to_dict()) == type(dict))
        self.assertTrue(type(model) == type(dict))
        self.assertEqual(a['__class__'], "BaseModel")
        self.assertEqual(a['name'], 'hbtn')
        self.assertEqual(a['number'], 18)
        with self.assertRaises(AttributeError):
            model.to_dict()['Hello'] = 1
        with self.assertRaises(TypeError):
            model.to_dict(attrs)
        my_model = BaseModel
        self.assertTrue(type(my_model.created_at) is type(datetime.now()))
        self.assertEqual(type(my_model.created_at), type(datetime.now()))
        self.assertTrue(type(my_model.updated_at) is type(datetime.now()))
        self.assertEqual(type(my_model.updated_at), type(datetime.now()))

    try:
        def test_time(self):
            model = BaseModel()
            model.created_at = '2017-09-28T21:03:54.05230'
            self.assertEqual(model.created_at, '2017-09-28T21:03:54.05230')
            self.assertNotEqual(model.created_at, datetime.now().isoformat())
            model.save()
            self.assertNotEqual(model.created_at, datetime.now())
            self.assertEqual(model.updated_at, datetime.now().isoformat())

            with open(self.__file_path, 'r') as json_file:
                complete_json = json.load(json_file)
                for key in complete_json:

                    if type(complete_json[key]['updated_at']) is str:
                        complete_json[key]['updated_at'] = datetime.strptime(
                            complete_json[key]['updated_at'], time)

                    if type(complete_json[key]['created_at']) is str:
                        complete_json[key]['created_at'] = datetime.strptime(
                            complete_json[key]['created_at'], time)
                self.__objects = complete_json
    except:
        pass
