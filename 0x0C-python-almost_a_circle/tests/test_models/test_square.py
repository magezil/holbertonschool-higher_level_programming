#!/usr/bin/python3
"""Unittests for Square class"""
import io
import sys
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    def test_init_empty(self):
        """Initialize with no arguments"""
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_init_size(self):
        """Initialize wtih one argument"""
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_init_size_xy(self):
        """Initialize with size, x, y"""
        s1 = Square(7, 8, 9)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_init_all(self):
        """Initialize with size, x, y, id"""
        s1 = Square(7, 8, 9, 21)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)
        self.assertEqual(s1.id, 21)

    def test_init_toomany(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            s1 = Square(7, 8, 9, 21, 22)

    def test_str_size(self):
        """Test __str__() function, intialize with size only"""
        s1 = Square(1)
        s1.id = 3
        self.assertEqual(s1.__str__(), "[Square] (3) 0/0 - 1")

    def test_str_xy(self):
        """Test __str__() function, initialize x, y"""
        s1 = Square(7, 8, 9)
        s1.id = 4
        self.assertEqual(s1.__str__(), "[Square] (4) 8/9 - 7")

    def test_str_all(self):
        """Test __str__() function, initialize all attributes"""
        s1 = Square(7, 8, 9, 21)
        self.assertEqual(s1.__str__(), "[Square] (21) 8/9 - 7")

    def test_display(self):
        """Test inherited display"""
        captured = io.StringIO()
        sys.stdout = captured
        s1 = Square(4)
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "####\n####\n####\n####\n")

    def test_displayxy(self):
        """Test inherited display with x, y values"""
        captured = io.StringIO()
        sys.stdout = captured
        s1 = Square(3, 2, 1)
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n  ###\n  ###\n  ###\n")

    def test_area(self):
        """Test inherited area()"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_size_property(self):
        """Test setter and getter for size"""
        s1 = Square(3)
        self.assertEqual(s1.size, 3)
        s1.size = 9
        self.assertEqual(s1.size, 9)

    def test_size_property_invalid_value(self):
        """Test if size setter raises ValueException('width must be > 0')"""
        s1 = Square(3)
        with self.assertRaisesRegex(ValueError, "width"):
            s1.size = -3

    def test_size_property_invalid_type(self):
        """Test if size setter raises
        TypeException('width must be an integer')
        """
        s1 = Square(3)
        with self.assertRaisesRegex(TypeError, "width"):
            s1.size = "3"

    def test_update_args(self):
        """Test if update args correctly with too many parameters"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(89, 2, 3, 4, 5)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

    def test_update_all_args(self):
        """Test if update args correctly"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        """Test if update kw args correctly"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(y=1, size=21, id=99, x=7)
        self.assertEqual(s1.__str__(), "[Square] (99) 7/1 - 21")

    def test_update_args_kwargs(self):
        """Test update args and kwargs (kwargs should not update)"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(10, id=7, size=3)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")
