# Write a simple unit test for a function that adds two numbers.

import unittest

from add_numbers import add_numbers

class TestAdd(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_numbers(2,3), 5)

if __name__ == '__main__':
        unittest.main()