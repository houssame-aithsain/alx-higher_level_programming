#!/usr/bin/python3
""" Base Module """


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

	@staticmethod
	def from_json_string(json_string):
		""" From json string method """
		if json_string is None or json_string == "":
			return []
		return json.loads(json_string)

	@classmethod
	def create(cls, **dictionary):
		""" Create method """
		if cls.__name__ == "Rectangle":
			dummy = cls(1, 1)
		if cls.__name__ == "Square":
			dummy = cls(1)
		dummy.update(**dictionary)
		return dummy

	@classmethod
	def load_from_file(cls):
		"""Return a list of classes."""
		filename = str(cls.__name__) + ".json"
		try:
			with open(filename, "r") as jsonfile:
				list_dicts = Base.from_json_string(jsonfile.read())
				return [cls.create(**d) for d in list_dicts]
		except IOError:
			return []
