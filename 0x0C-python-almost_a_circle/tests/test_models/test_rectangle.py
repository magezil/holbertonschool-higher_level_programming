#!/usr/bin/python3
"""Unittest for Base class"""
import io
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def test_init_empty(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_init_oneparam(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_init_wh(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id - r1.id, 1)

    def test_init_whxy(self):
        r1 = Rectangle(10, 2, 3, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_init_all(self):
        r1 = Rectangle(10, 2, 3, 3, 98)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_init_no_wh(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(x=3, y=3)

    def test_width_type_valid(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 0)
        with self.assertRaises(TypeError):
            r1 = Rectangle((10, ), 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle([10], 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle({10: 2}, 2)

    def test_height_type_valid(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "10")
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, (10, ))
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, [10])
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, {10: 2})

    def test_x_type_valid(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, "10", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, "10", 0)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, (10, ), 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, [10], 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, {10: 2}, 2)

    def test_y_type_valid(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, "10")
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, (10, ))
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, [10])
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, {10: 2})

    def test_width_0(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)

    def test_height_0(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 0)

    def test_xy_0(self):
        r1 = Rectangle(2, 3, 0, 0)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -3)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 2
        r1.height = 10
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(4, 6)
        r1.display()
        r1 = Rectangle(2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(),
                         '####\n####\n####\n####\n####\n####\n##\n##\n')

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_print(self):
        captured = io.StringIO()
        sys.stdout = captured
        r2 = Rectangle(5, 5, 1, id=1)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

    def test_display_xy(self):
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_0y(self):
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(3, 2, 0, 1)
        r1.display()
        self.assertEqual(captured.getvalue(), "\n###\n###\n")

    def test_display_x0(self):
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(3, 2, 1, 0)
        r1.display()
        self.assertEqual(captured.getvalue(), " ###\n ###\n")
