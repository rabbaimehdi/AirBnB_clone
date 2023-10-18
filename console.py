#!/usr/bin/python3
"""Defines the AiRBNB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    return [i.strip(",") for i in str.split(arg)]
# def parse(arg):
#     braces = re.search(r"\((.*?)\)", arg)
#     if braces is None:
#         return [i.strip(",") for i in str.split(arg)]
#     else:
#         no_braces = arg[:braces.span()[0]]
#         splited_word = no_braces.split(".")
#         return splited_word[::-1]


class HBNBCommand(cmd.Cmd):
    """Defines the AiRBNB command interpreter.

    Attributes:
        prompt (str): The command.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd when no input is provided"""
        argdict = {
            "all": self.do_all
        }
        re_match = re.search(r"\.", arg)
        if re_match is not None:
            arguments = [arg[:re_match.span()[0]], arg[re_match.span()[1]:]]
            re_match = re.search(r"\((.*?)\)", arguments[1])
            if re_match is not None:
                command = arguments[1][:re_match.span()[0]]
                if command in argdict.keys():
                    model_call = "{} ".format(arguments[0])
                    return argdict[command](model_call)
    

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
    
    def do_create(self, arg):
        """Creates a new class instance then prints its id."""
        arguments = parse(arg)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arguments[0])().id)
            storage.save()

    def do_show(self, arg):
        """Displays the string representation of a class instance provided its id."""
        arguments = parse(arg)
        dictionary = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in dictionary:
            print("** no instance found **")
        else:
            print(dictionary["{}.{}".format(arguments[0], arguments[1])])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        arguments = parse(arg)
        dictionary = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in dictionary.keys():
            print("** no instance found **")
        else:
            del dictionary["{}.{}".format(arguments[0], arguments[1])]
            storage.save()

    def do_all(self, arg):
        """ Display string representations of all instances of a given class.
        If no class is specified, displays all objectsects."""
        arguments = parse(arg)
        if len(arguments) > 0 and arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectsectslist = []
            for objects in storage.all().values():
                if len(arguments) > 0 and arguments[0] == objects.__class__.__name__:
                    objectsectslist.append(objects.__str__())
                elif len(arguments) == 0:
                    objectsectslist.append(objects.__str__())
            print(objectsectslist)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arguments = parse(arg)
        dictionary = storage.all()

        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arguments) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arguments[0], arguments[1]) not in dictionary.keys():
            print("** no instance found **")
            return False
        if len(arguments) == 2:
            print("** attribute name missing **")
            return False
        if len(arguments) == 3:
            try:
                type(eval(arguments[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arguments) == 4:
            objects = dictionary["{}.{}".format(arguments[0], arguments[1])]
            if arguments[2] in objects.__class__.__dict__.keys():
                valuetype = type(objects.__class__.__dict__[arguments[2]])
                objects.__dict__[arguments[2]] = valuetype(arguments[3])
            else:
                objects.__dict__[arguments[2]] = arguments[3]
        elif type(eval(arguments[2])) == dict:
            objects = dictionary["{}.{}".format(arguments[0], arguments[1])]
            for k, v in eval(arguments[2]).items():
                if (k in objects.__class__.__dict__.keys() and
                        type(objects.__class__.__dict__[k]) in {str, int, float}):
                    valuetype = type(objects.__class__.__dict__[k])
                    objects.__dict__[k] = valuetype(v)
                else:
                    objects.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """ Print the number of instances of a class."""
        arguments = parse(arg)
        counter = 0
        for obj in storage.all().values():
            if arguments[0] == obj.__class__.__name__:
                counter += 1
        print(counter)

if __name__ == "__main__":
    HBNBCommand().cmdloop()