import unittest
from unittest.mock import Mock

class BoardTesting(unittest.TestCase):

    def setUp(self):
      pawn = Mock()

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

