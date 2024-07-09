#!/usr/bin/env python3
"""Parameterized unit tests
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


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


class TestGetJson(unittest.TestCase):
    """ Test Get Json Functionality """
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}],
    ])
    def test_get_json(self, test_url, test_payload):
        """ test get json method with mock class """
        attrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Class for testing memoization """
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as test_method:
            test_method.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            test_method.assert_called_once()
