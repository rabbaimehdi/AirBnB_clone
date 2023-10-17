#!/usr/bin/python3
from models.base_model import BaseModel

# Write a class User that inherits from BaseModel
class User(BaseModel):
    """User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""