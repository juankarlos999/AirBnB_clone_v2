#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


if 'db' == os.getenv('HBNB_TYPE_STORAGE')
     from models.engine.file_storage import FileStorage
     storage = FileStorage()
else:
     from models.engine.db_storage import DBStorage
     storage = DBStorage()

storage.reload()
