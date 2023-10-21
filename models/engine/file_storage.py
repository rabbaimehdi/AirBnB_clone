#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Abstracted storage engine.

    Attributes:
        __file_path (str): The file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        object_id = obj.id
        FileStorage.__objects[f"{class_name}.{object_id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = FileStorage.__objects
        new_objects_dict = {}
        for key in objects_dict.keys():
            new_objects_dict[key] = objects_dict[key].to_dict()

        with open(FileStorage.__file_path, 'w',) as file:
            json.dump(new_objects_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, no exception"""
        try:
            with open(FileStorage.__file_path) as file:
                dict = json.load(file)
                for item in dict.values():

                    class_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            pass
