# Write a test case for a function that checks if a number is prime
# unit test for check_prime

import unittest

from check_prime import check_prime

class TestPrime(unittest.TestCase):
    def test_true(self):
        """
        Test that it returns true for a prime number
        """
        result = check_prime(17)
        self.assertTrue(result)

    def test_false(self):
        """
        Test that it returns false for a number that is not prime
        """
        result = check_prime(8)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()