#!/usr/bin/python3
"""Unittests for Rectangle class"""
import csv
import io
import json
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def test_init_empty(self):
        """Initialize with no arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_init_oneparam(self):
        """Initialize with one argument"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_init_wh(self):
        """Initialize width and height"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id - r1.id, 1)

    def test_init_whxy(self):
        """Initialize width, height, x, and y"""
        r1 = Rectangle(10, 2, 3, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_init_all(self):
        """Initialize width, height, x, y, and id"""
        r1 = Rectangle(10, 2, 3, 3, 98)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_init_toomany(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, 4, 5, 6)

    def test_init_no_wh(self):
        """Try to initialize without width and height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(x=3, y=3)

    def test_width_type_valid(self):
        """Initialize with invalid type"""
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
        """Initialize with invalid type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "10")
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, (10, ))
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, [10])
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, {10: 2})

    def test_x_type_valid(self):
        """Initialize with invalid type"""
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
        """Initialize with invalid type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, "10")
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, (10, ))
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, [10])
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, {10: 2})

    def test_width_0(self):
        """Initialize width with invalid value (0)"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)

    def test_height_0(self):
        """Initialize height with invalid value (0)"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 0)

    def test_xy_0(self):
        """Initialize x and y with valid value 0"""
        r1 = Rectangle(2, 3, 0, 0)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_negative(self):
        """Initialize with negative value (invalid)"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -3)

    def test_area(self):
        """Test area function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 2
        r1.height = 10
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        """Test display function"""
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
        """Test str function"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_print(self):
        """Test str function with print"""
        captured = io.StringIO()
        sys.stdout = captured
        r2 = Rectangle(5, 5, 1, id=1)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

    def test_display_xy(self):
        """Test display with x and y position"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_0y(self):
        """Test display with x=0 and y position"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(3, 2, 0, 1)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n###\n###\n")

    def test_display_x0(self):
        """Test display with x position and y=0"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(3, 2, 1, 0)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ###\n ###\n")

    def test_update1(self):
        """Test update first attribute (id)"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update2(self):
        """Test update first two attributes (id, width)"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_update3(self):
        """Test update id, width, height"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_update4(self):
        """Test update id, width, height, x"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_update5(self):
        """Test update id, width, height, x, y"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_toomany(self):
        """Test update with too many arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_invalid_value(self):
        """Test update with invalid value"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        with self.assertRaises(ValueError):
            r1.update(89, -1)

    def test_update_invalid_type(self):
        """Test update with invalid type"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        with self.assertRaises(TypeError):
            r1.update(89, "1")

    def test_update_kwargs1(self):
        """Test update with one keyword argument"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_kwargs2(self):
        """Test update with two keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/10")

    def test_update_kwargs3(self):
        """Test update with three keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(y=1, id=2, width=9)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 10/1 - 9/10")

    def test_update_kwargs4(self):
        """Test update with four keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(y=1, id=2, x=8, height=7)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 8/1 - 10/7")

    def test_update_kwargs5(self):
        """Test update with five keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(y=1, id=2, width=9, x=8, height=7)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 8/1 - 9/7")

    def test_update_args_kwargs(self):
        """Test update args and kwargs (kwargs should not update)"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(10, id=7)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_args(self):
        """Test update args as kwargs (should only do kwargs)"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(args=[10, 7], x=9)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 9/10 - 10/10")

    def test_to_dictionary(self):
        """Test to_dictionary()"""
        attrs = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        r1 = Rectangle(1, 2, 3, 4, 5)
        r_dict = r1.to_dictionary()
        self.assertEqual(len(attrs), len(r_dict))
        self.assertEqual(r_dict, attrs)

    def test_to_json_string(self):
        """Test inherited method test_to_json_string()"""
        r1 = Rectangle(10, 7, 2, 8, 27)
        dictionary = r1.to_dictionary()
        json_dict_str = Base.to_json_string([dictionary])
        attrs = {'id': 27, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        self.assertEqual(len(attrs), len(dictionary))
        self.assertEqual(dictionary, attrs)
        self.assertEqual(json.loads(json_dict_str),
                         json.loads(Base.to_json_string([attrs])))

    def test_save_to_file_rect(self):
        """Test inherted save_to_file()"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            rects = json.load(f)
            self.assertEqual(len(rects), 2)
            self.assertEqual(r1.to_dictionary(), rects[0])
            self.assertEqual(r2.to_dictionary(), rects[1])

    def test_save_to_file_rect_none(self):
        """Test save_to_file() with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            rects = json.load(f)
            self.assertEqual(len(rects), 0)
            self.assertEqual(rects, [])

    def test_save_to_file_rempty(self):
        """Test save_to_file() with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            rects = json.load(f)
            self.assertEqual(len(rects), 0)
            self.assertEqual(rects, [])

    def test_from_json_string(self):
        """Test inherited from_json_string()"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create_rect(self):
        """Test inherited create()"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertNotEqual(r1, r2)

    def test_load_from_file_rect(self):
        """Test inherited load_from_file()"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rect_output), len(list_rect_input))
        self.assertEqual(r1.__str__(), list_rect_output[0].__str__())
        self.assertEqual(r2.__str__(), list_rect_output[1].__str__())

    def test_save_to_file_csv_rect(self):
        """Test inherited save_to_file_csv()"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        rects = [r1, r2]
        Rectangle.save_to_file_csv(rects)
        with open("Rectangle.csv", "r") as f:
            reader = csv.DictReader(f)
            for row, rect in zip(reader, rects):
                for k, v in row.items():
                    row[k] = int(v)
                self.assertEqual(row, rect.to_dictionary())

    def test_load_from_file_csv_rect(self):
        """Test inherited load_from_file()"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rect_input)
        list_rect_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rect_output), len(list_rect_input))
        for ri, ro in zip(list_rect_input, list_rect_output):
            self.assertEqual(ri.__str__(), ro.__str__())

    def test_save_file_csv_none_rect(self):
        """Test save None object to csv file"""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r", newline='') as f:
            rects = Rectangle.load_from_file_csv()
            self.assertEqual(len(rects), 0)
            self.assertEqual(rects, [])

    def test_save_file_csv_empty_rect(self):
        """Test save empty list to csv file"""
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r", newline='') as f:
            rects = Rectangle.load_from_file_csv()
            self.assertEqual(len(rects), 0)
            self.assertEqual(rects, [])
