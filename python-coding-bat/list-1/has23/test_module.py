import unittest
from has23 import has23


class UnitTests(unittest.TestCase):

    def test_2_5_returns_true(self):
        actual = has23([2, 5])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [2, 5] to return "True"')

    def test_4_3_returns_true(self):
        actual = has23([4, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [4, 3] to return "True"')

    def test_4_5_returns_false(self):
        actual = has23([4, 5])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [4, 5] to return "False"')

    def test_2_2_returns_true(self):
        actual = has23([2, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [2, 2] to return "True"')

    def test_3_2_returns_true(self):
        actual = has23([3, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [3, 2] to return "True"')

    def test_3_3_returns_true(self):
        actual = has23([3, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [3, 3] to return "True"')

    def test_7_7_returns_false(self):
        actual = has23([7, 7])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [7, 7] to return "False"')

    def test_3_9_returns_true(self):
        actual = has23([3, 9])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [3, 9] to return "True"')

    def test_9_5_returns_false(self):
        actual = has23([9, 5])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has23() with [9, 5] to return "False"')


if __name__ == "__main__":
    unittest.main()
