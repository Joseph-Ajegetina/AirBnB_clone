#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""__init__ magic method for models directory"""

from models.engine.file_storage import FileStorage

file_storage = FileStorage()
file_storage.reload()
