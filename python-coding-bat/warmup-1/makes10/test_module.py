import unittest
from makes10 import makes10


class UnitTests(unittest.TestCase):

    def test_9_and_10_returns_true(self):
        actual = makes10(9, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "9" and "10" to return "True"')

    def test_9_and_9_returns_false(self):
        actual = makes10(9, 9)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "9" and "9" to return "False"')

    def test_1_and_9_returns_true(self):
        actual = makes10(1, 9)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "1" and "9" to return "True"')

    def test_10_and_1_returns_true(self):
        actual = makes10(10, 1)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "10" and "1" to return "True"')

    def test_10_and_10_returns_true(self):
        actual = makes10(10, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "10" and "10" to return "True"')

    def test_8_and_2_returns_true(self):
        actual = makes10(8, 2)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "8" and "2" to return "True"')

    def test_8_and_3_returns_false(self):
        actual = makes10(8, 3)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "8" and "3" to return "False"')

    def test_10_and_42_returns_true(self):
        actual = makes10(10, 42)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "10" and "42" to return "True"')

    def test_12_and_negative_2_returns_true(self):
        actual = makes10(12, -2)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling makes10() with "12" and "-2" to return "True"')


if __name__ == "__main__":
    unittest.main()
