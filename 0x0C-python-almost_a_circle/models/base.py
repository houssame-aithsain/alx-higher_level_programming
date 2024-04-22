#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To json string method """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to file method """
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dict))
