"""Run tests on pypack.module"""

import unittest

from src.pypack import module


class TestHelloFunc(unittest.TestCase):
    """Test pypack.module.get_hello"""

    def test_hello(self):
        """Check output."""
        self.assertEqual(module.get_hello(), "Hello!")
