#!/usr/bin/python3
"""Defines the class FileStorage."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents the FileStorage class.

    Attributes:
        __file_path (str): the location of the file to save the objects in.
        __objects (dict): dictionary repn of objects to be stored.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key class_name.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            odict = FileStorage.__objects
            objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                obj = json.load(f)
                for o in obj.values():
                    clsname = o["__class__"]
                    del o["__class__"]
                    self.new(eval(clsname)(**o))
        except FileNotFoundError:
            return
