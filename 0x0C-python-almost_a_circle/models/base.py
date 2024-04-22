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

    @classmethod
    def load_from_file(cls):
        """ Load from file method """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dict = cls.from_json_string(f.read())
            list_inst = []
            for dict in list_dict:
                list_inst.append(cls.create(**dict))
            return list_inst
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to file csv method """
        filename = cls.__name__ + ".csv"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file_csv(cls):
        """ Load from file csv method """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                list_dict = cls.from_json_string(f.read())
            list_inst = []
            for dict in list_dict:
                list_inst.append(cls.create(**dict))
            return list_inst
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()
        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()
