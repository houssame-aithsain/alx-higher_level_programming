#!/usr/bin/python3
"""Unittest for Rectangle class"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def setUp(self):
        """Set up for all methods"""
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """Test rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r3.id, 0)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_rectangle_update(self):
        """Test rectangle update"""
        r1 = Rectangle(10, 2)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_rectangle_update_kwargs(self):
        """Test rectangle update kwargs"""
        r1 = Rectangle(10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)

    def test_rectangle_to_dictionary(self):
        """Test rectangle to dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                         'width': 10})

    def test_rectangle_save_to_file(self):
        """Test rectangle save to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"x": 2, "y": 8, "id": 1,
                                                        "height": 7, "width": 10},
                                                       {"x": 0, "y": 0, "id": 2,
                                                        "height": 4, "width": 2}])

    def test_rectangle_load_from_file(self):
        """Test rectangle load from file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual([r.to_dictionary() for r in list_input],
                         [r.to_dictionary() for r in list_output])

    def test_rectangle_csv(self):
        """Test rectangle csv"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "1,10,7,2,8\n2,2,4,0,0\n")

    def test_rectangle_create(self):
        """Test rectangle create"""
        r1 = Rectangle(3, 5, 1, 2)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_rectangle_load_from_file_csv(self):
        """Test rectangle load from file csv"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual([r1.__str__(), r2.__str__()], [str(r) for r in list_rectangles])

    def test_rectangle_create_empty(self):
        """Test rectangle create empty"""
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_rectangle_create_empty_dict(self):
        """Test rectangle create empty dict"""
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**{})
        self.assertNotEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_rectangle_create_no_args(self):
        """Test rectangle create no args"""
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create()
        self.assertNotEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_rectangle_create_no_args(self):
        """Test rectangle create no args"""
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create()
        self.assertNotEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_rectangle_create_no_args(self):
        """Test rectangle create no args"""
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create()
        self.assertNotEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)
 