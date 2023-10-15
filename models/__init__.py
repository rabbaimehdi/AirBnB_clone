#!/usr/bin/python3
"""__init__ for initializing already created objects"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
