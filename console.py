#!/usr/bin/python3
"""Defines the HBNBCommand class."""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Represents the HBNBCommand class."""
    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True

    def do_create(self, arg):
        """Usage: create <class name>
        Create a new <class name> instance.
        """
        if arg[0]:
            print("** class name missing **")
        elif arg[1] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def postloop(self):
        print

if __name__ == '__main__':
    HBNBCommand().cmdloop()
