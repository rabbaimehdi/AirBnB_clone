#!/usr/bin/python3
import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects
    
    def new(self, obj):
        class_name = obj.__class__.__name__
        object_id = obj.id
        self.__objects[f"{class_name}.{object_id}"] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dumb(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass