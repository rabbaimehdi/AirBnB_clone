#!/usr/bin/python3
import uuid
import datetime

#Write a class BaseModel that defines all common attributes/methods for other classes:

class BaseModel:
    
    def __init__(self):
        pass

    id = uuid.uuid4()
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        print(f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        dictionnary = self.__dict__
        dictionnary["__class__"] = type(self).__name__
        dictionnary["created_at"] = self.created_at.isoformat()
        dictionnary["updated_at"] = self.updated_at.isoformat()
