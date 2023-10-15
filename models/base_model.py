#!/usr/bin/python3
import uuid
import datetime
import models

# Write a class BaseModel that defines all
# common attributes/methods for other classes:


class BaseModel:
    """The BaseModel of the AiRBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.\
                            strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the class name of the object __class__.
        """
        dictionnary = self.__dict__.copy()
        dictionnary["created_at"] = self.created_at.isoformat()
        dictionnary["updated_at"] = self.updated_at.isoformat()
        dictionnary["__class__"] = self.__class__.__name__
        return dictionnary
