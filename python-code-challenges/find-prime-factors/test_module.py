import unittest
from find_prime_factors import find_prime_factors


# the test case
class UnitTests(unittest.TestCase):
    def test_prime_factors_of_630(self):
        actual = find_prime_factors(630)
        expected = [2, 3, 3, 5, 7]
        self.assertEqual(
            actual, expected, 'Expected output to be [2, 3, 3, 5, 7] when calling "find_prime_factors()" with 630')

    def test_prime_factors_of_1(self):
        actual = find_prime_factors(1)
        expected = []
        self.assertEqual(
            actual, expected, 'Expected output to be [] when calling "find_prime_factors()" with 1')

    def test_prime_factors_of_negative_5(self):
        actual = find_prime_factors(-1)
        expected = []
        self.assertEqual(
            actual, expected, 'Expected output to be [] when calling "find_prime_factors()" with -5')

    def test_prime_factors_of_60(self):
        actual = find_prime_factors(60)
        expected = [2, 2, 3, 5]
        self.assertEqual(
            actual, expected, 'Expected output to be [2, 2, 3, 5] when calling "find_prime_factors()" with 60')

    def test_prime_factors_of_123456789(self):
        actual = find_prime_factors(123456789)
        expected = [3, 3, 3607, 3803]
        self.assertEqual(
            actual, expected, 'Expected output to be [3, 3, 3607, 3803] when calling "find_prime_factors()" with 123456789')


if __name__ == "__main__":
    unittest.main()
