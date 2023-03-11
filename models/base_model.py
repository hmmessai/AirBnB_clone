#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel instance.

        Args:
            args (any): unused
            kwargs (dict): Key/Value pairs attributes of instance.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """"Saves the new instance."""
        models.storage.save()

    def to_dict(self):
        """"Returns the dictionary containing all the key/ value pairs
        of __dict__ of the instance."""
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        newdict["created_at"] = newdict["created_at"].isoformat()
        newdict["updated_at"] = newdict["updated_at"].isoformat()
        return newdict

    def __str__(self):
        """String representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))
