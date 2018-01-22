#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_init_param(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(-1)
        self.assertEqual(b2.id, -1)
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_init_mix(self):
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        b3 = Base(8)
        self.assertEqual(b3.id, 8)
        b4 = Base()
        self.assertEqual(b4.id, 6)
