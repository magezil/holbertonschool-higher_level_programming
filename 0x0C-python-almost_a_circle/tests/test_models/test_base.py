#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_init(self):
        """Initialize with no arguments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_init_param(self):
        """Initialize with id given"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(-1)
        self.assertEqual(b2.id, -1)
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_init_mix(self):
        """Initialize with no id given, id given, no id given"""
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        b3 = Base(8)
        self.assertEqual(b3.id, 8)
        b4 = Base()
        self.assertEqual(b4.id, 6)

    def test_init_toomany(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_init_str(self):
        """Initialize id with string"""
        b1 = Base("123")
        self.assertEqual(b1.id, "123")

    def test_init_dict(self):
        """Initialize id with dictionary"""
        b1 = Base({"123": "456"})
        self.assertEqual(b1.id, {"123": "456"})

    def test_init_tup(self):
        """Initialize id with tuple"""
        b1 = Base((1, ))
        self.assertEqual(b1.id, (1, ))

    def test_init_list(self):
        """Initialize id with list"""
        b1 = Base([1])
        self.assertEqual(b1.id, [1])
