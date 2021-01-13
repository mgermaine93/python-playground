import unittest
from array123 import array123


class UnitTests(unittest.TestCase):

    def test_1_1_2_3_1_returns_true(self):
        actual = array123([1, 1, 2, 3, 1])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 1, 2, 3, 1]" to return "True"')

    def test_1_1_2_4_1_returns_false(self):
        actual = array123([1, 1, 2, 4, 1])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 1, 2, 4, 1]" to return "False"')

    def test_1_1_2_1_2_3_returns_true(self):
        actual = array123([1, 1, 2, 1, 2, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 1, 2, 1, 2, 3]" to return "True"')

    def test_1_1_2_1_2_1_returns_false(self):
        actual = array123([1, 1, 2, 1, 2, 1])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 1, 2, 1, 2, 1]" to return "False"')

    def test_1_2_3_1_2_3_returns_true(self):
        actual = array123([1, 2, 3, 1, 2, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 2, 3, 1, 2, 3]" to return "True"')

    def test_1_2_3_returns_true(self):
        actual = array123([1, 2, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 2, 3]" to return "True"')

    def test_1_1_1_returns_false(self):
        actual = array123([1, 1, 1])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 2, 3]" to return "False"')

    def test_1_2_returns_false(self):
        actual = array123([1, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1, 2]" to return "False"')

    def test_1_returns_false(self):
        actual = array123([1])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[1]" to return "False"')

    def test_blank_returns_false(self):
        actual = array123([])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "[]" to return "False"')


if __name__ == "__main__":
    unittest.main()
