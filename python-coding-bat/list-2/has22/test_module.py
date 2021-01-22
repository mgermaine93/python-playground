import unittest
from has22 import has22


class UnitTests(unittest.TestCase):

    def test_1_2_2_returns_true(self):
        actual = has22([1, 2, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [1, 2, 2] to return "True"')

    def test_1_2_1_2_returns_false(self):
        actual = has22([1, 2, 1, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [1, 2, 1, 2] to return "False"')

    def test_2_1_2_returns_false(self):
        actual = has22([2, 1, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [2, 1, 2] to return "False"')

    def test_2_2_1_2_returns_true(self):
        actual = has22([2, 2, 1, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [2, 2, 1, 2] to return "True"')

    def test_1_3_2_returns_false(self):
        actual = has22([1, 3, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [1, 3, 2] to return "False"')

    def test_1_3_2_2_returns_true(self):
        actual = has22([1, 3, 2, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [1, 3, 2, 2] to return "True"')

    def test_2_3_2_2_returns_true(self):
        actual = has22([2, 3, 2, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [2, 3, 2, 2] to return "True"')

    def test_4_2_4_2_2_5_returns_true(self):
        actual = has22([4, 2, 4, 2, 2, 5])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [4, 2, 4, 2, 2, 5] to return "True"')

    def test_1_2_returns_false(self):
        actual = has22([1, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [1, 2] to return "False"')

    def test_2_2_returns_true(self):
        actual = has22([2, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [2, 2] to return "True"')

    def test_2_returns_false(self):
        actual = has22([2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [2] to return "False"')

    def test_empty_list_returns_false(self):
        actual = has22([])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [] to return "False"')

    def test_3_3_2_2_returns_true(self):
        actual = has22([3, 3, 2, 2])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [3, 3, 2, 2] to return "True"')

    def test_5_2_5_2_returns_false(self):
        actual = has22([5, 2, 5, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling has22() with [5, 2, 5, 2] to return "False"')


if __name__ == "__main__":
    unittest.main()
