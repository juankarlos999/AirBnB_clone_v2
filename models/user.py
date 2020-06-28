#!/usr/bin/python3
""" Is a class """
from models.base_model import BaseModel


class User(BaseModel):
    """ class that inrhent """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
