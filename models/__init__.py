#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models import storage
from models.engine.file_storage import FileStorage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage.__class__ = DBStorage
else:
    from models.engine.file_storage import FileStorage
    storage.__class__ = FileStorage

storage.reload()
