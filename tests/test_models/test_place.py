#!/usr/bin/python3
"""
Contains the TestPlace class

"""

from datetime import datetime
from models import place
from models.base_model import BaseModel
import unittest
Place = place.Place


class TestPlace(unittest.TestCase):
    """testing the subclass Place"""
    def test_subclass(self):
        """Testing if City inherits of BaseModel"""
        ins = Place()
        self.assertIsInstance(ins, BaseModel)
        self.assertTrue(hasattr(ins, "id"))
        self.assertTrue(hasattr(ins, "created_at"))
        self.assertTrue(hasattr(ins, "updated_at"))

    def test_str(self):
        """testing the correct output with a subclass"""
        instancia = Place()
        string = "[Place] ({}) {}".format(instancia.id, instancia.__dict__)
        self.assertEqual(string, str(instancia))

    def test_name(self):
        """testing if a subclass had a ins(name) and if this is empty"""
        inst = Place()
        self.assertEqual(inst.name, "")
        self.assertTrue(hasattr(inst, "name"))

    def test_city_id(self):
        """testing if a subclass had a ins(city_id) and if this is empty"""
        c = Place()
        self.assertEqual(c.city_id, "")
        self.assertTrue(hasattr(c, "city_id"))

    def test_user_id(self):
        """testing if a subclass had a ins(user_id) and if this is empty"""
        s = Place()
        self.assertEqual(s.user_id, "")
        self.assertTrue(hasattr(s, "user_id"))

    def test_description(self):
        """testing if a subclass had a ins(user_id) and if this is empty"""
        x = Place()
        self.assertTrue(hasattr(x, "description"))
        self.assertEqual(x.description, "")

    def test_number_rooms(self):
        """testing  if a subclass had a ins(number_rooms)
         and if this is a int=0"""
        v = Place()
        self.assertEqual(type(v.number_rooms), int)
        self.assertEqual(v.number_rooms, 0)
        self.assertTrue(hasattr(v, "number_rooms"))

    def test_number_bathrooms(self):
        """testing if a subclass had a ins(number_bathrooms)
      and if this is a int=0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(type(place.number_bathrooms), int)

    def test_max_guest(self):
        """testing if a subclass had a ins(max_guest)
      and if this is a int=0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(type(place.number_bathrooms), int)

    def test_price_by_night(self):
        """testing if a subclass had a ins(price_by_night)
      and if this is a int=0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(type(place.price_by_night), int)

    def test_latitude(self):
        """testing if a subclass had a ins(latitude)
      and if this is a float=0.0"""
        place = Place()
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(type(place.latitude), float)
        self.assertTrue(hasattr(place, "latitude"))

    def test_longitude(self):
        """testing the attr longitude that inherits  of class:place"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)
        # dictonary = Place().__dict__()
        # self.assertEqual('longitude' in dictonary)

    def test_amenity_ids(self):
        """testing the attr amenity id that inherits  of class:place"""
        place = Place()
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(type(place.amenity_ids), list)
        self.assertTrue(hasattr(place, "amenity_ids"))

        # self.assertIsInstance(place.amenity_ids, list)

    def test_dict(self):
        """testing the type of a instance"""
        instancia = Place()
        dicc = instancia.to_dict()
        self.assertEqual(type(dicc), dict)

    def test_methodworks(self):
        """ Check the instance"""
        instancia = Place()
        time = instancia.updated_at
        instancia.save()
        self.assertTrue(time != instancia.updated_at)
        self.assertTrue(type(instancia.__str__()) is str)
        self.assertTrue(type(instancia.to_dict()) is dict)
