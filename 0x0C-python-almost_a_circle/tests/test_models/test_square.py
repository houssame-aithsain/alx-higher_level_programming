#!/usr/bin/python3
"""Unittest for Square class"""

import unittest
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test Square class"""

    def setUp(self):
        """Set up for all methods"""
        Base._Base__nb_objects = 0

    def test_square(self):
        """Test square"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Square(2, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)

    def test_square_update(self):
        """Test square update"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(10, 2)
        self.assertEqual(s1.size, 2)
        s1.update(10, 2, 3)
        self.assertEqual(s1.x, 3)
        s1.update(10, 2, 3, 4)
        self.assertEqual(s1.y, 4)

    def test_square_update_kwargs(self):
        """Test square update kwargs"""
        s1 = Square(5)
        s1.update(size=10)
        self.assertEqual(s1.size, 10)
        s1.update(size=10, id=1)
        self.assertEqual(s1.id, 1)
        s1.update(x=1, y=1)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)

    def test_square_to_dictionary(self):
        """Test square to dictionary"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_square_save_to_file(self):
        """Test square save to file"""
        s1 = Square(10, 2, 1)
        s2 = Square(2, 0, 0)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"id": 1, "size": 10, "x": 2, "y": 1},
                                                        {"id": 2, "size": 2, "x": 0, "y": 0}])

    def test_square_load_from_file(self):
        """Test square load from file"""
        s1 = Square(10, 2, 1)
        s2 = Square(2, 0, 0)
        Square.save_to_file([s1, s2])
        list_squares = Square.load_from_file()
        self.assertEqual([s1.__str__(), s2.__str__()], [str(s) for s in list_squares])

    def test_square_save_to_file_csv(self):
        """Test square save to file csv"""
        s1 = Square(10, 2, 1)
        s2 = Square(2, 0, 0)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "1,10,2,1\n2,2,0,0\n")

    def test_square_load_from_file_csv(self):
        """Test square load from file csv"""
        s1 = Square(10, 2, 1)
        s2 = Square(2, 0, 0)
        Square.save_to_file_csv([s1, s2])
        list_squares = Square.load_from_file_csv()
        self.assertEqual([s1.__str__(), s2.__str__()], [str(s) for s in list_squares])

    def test_square_create(self):
        """Test square create"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertFalse(s1 is s2)

    def test_square_load_from_file_csv(self):
        """Test square load from file csv"""
        s1 = Square(10, 2, 1)
        s2 = Square(2, 0, 0)
        Square.save_to_file_csv([s1, s2])
        list_squares = Square.load_from_file_csv()
        self.assertEqual([s1.__str__(), s2.__str__()], [str(s) for s in list_squares])
