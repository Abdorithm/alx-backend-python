#!/usr/bin/env python3
"""Parameterized unit tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map Functionality
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, nested_map, path, res):
        """ test the access nested map with parameterized module"""
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        [{}, ("a",), "a"],
        [{"a": 1}, ("a", "b"), "b"],
    ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        """ test keyerror raises """
        with self.assertRaises(KeyError) as keyerr:
            access_nested_map(nested_map, path)
            assertEqual(keyerr, key)
