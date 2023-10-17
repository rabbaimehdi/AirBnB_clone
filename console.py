#!/usr/bin/python3
"""Defines the AiRBNB console."""
import cmd
from models import storage

def parse(arg):
    return [i.strip(",") for i in str.split(arg)]


class HBNBCommand(cmd.Cmd):
    """Defines the AiRBNB command interpreter.

    Attributes:
        prompt (str): The command.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line."""
        pass

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
        If no class is specified, displays all objects."""
        arguments = parse(arg)
        if len(arguments) > 0 and arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectslist = []
            for obj in storage.all().values():
                if len(arguments) > 0 and arguments[0] == obj.__class__.__name__:
                    objectslist.append(obj.__str__())
                elif len(arguments) == 0:
                    objectslist.append(obj.__str__())
            print(objectslist)


if __name__ == "__main__":
    HBNBCommand().cmdloop()