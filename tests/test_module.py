import unittest

from src.pypack import module


class TestHelloFunc(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(module.get_hello(), "Hello!")
