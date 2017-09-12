#!/usr/bin/python3
"""
Contains test for Task 1
"""

import unittest
from models import base
Base = base.Base


class TestTask1(unittest.TestCase):
    """"""
    def test_module_docstring(self):
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_no_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_no_id_after_set(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb_private(self):
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)
