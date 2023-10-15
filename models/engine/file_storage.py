#!/usr/bin/python3
import json

class FileStorage:
    __file_path = '../../../file.json'
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
        objects ={}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
            
        with open(self.__file_path, 'w',) as file:
            json.dump(objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                dict = json.load(file)
            for item in dict.values():
                class_name = item["__class__"]
                # del item["__class__"]
                self.new(eval(class_name)(**item))
        except:
            pass