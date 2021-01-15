import unittest
from first_last6 import first_last6


class UnitTests(unittest.TestCase):

    def test_1_2_6_returns_true(self):
        actual = first_last6([1, 2, 6])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 6] to return "True"')

    def test_6_1_2_3_returns_true(self):
        actual = first_last6([6, 1, 2, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [6, 1, 2, 3] to return "True"')

    def test_13_6_1_2_3_returns_false(self):
        actual = first_last6([13, 6, 1, 2, 3])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [13, 6, 1, 2, 3] to return "False"')

    def test_13_6_1_2_6_returns_true(self):
        actual = first_last6([13, 6, 1, 2, 6])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [13, 6, 1, 2, 6] to return "True"')

    def test_3_2_1_returns_false(self):
        actual = first_last6([3, 2, 1])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [3, 2, 1] to return "False"')

    def test_3_6_1_returns_false(self):
        actual = first_last6([3, 6, 1])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [3, 6, 1] to return "False"')

    def test_3_6_returns_true(self):
        actual = first_last6([3, 6])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [3, 6] to return "True"')

    def test_6_returns_true(self):
        actual = first_last6([6])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [6] to return "True"')

    def test_3_returns_false(self):
        actual = first_last6([3])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [3] to return "False"')

    def test_5_6_returns_true(self):
        actual = first_last6([13, 6, 1, 2, 6])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [13, 6, 1, 2, 6] to return "True"')

    def test_5_5_returns_false(self):
        actual = first_last6([5, 5])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [5, 5] to return "False"')

    def test_1_2_3_4_6_returns_true(self):
        actual = first_last6([1, 2, 3, 4, 6])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 3, 4, 6] to return "True"')

    def test_1_2_3_4_returns_false(self):
        actual = first_last6([1, 2, 3, 4])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 3, 4] to return "False"')


if __name__ == "__main__":
    unittest.main()
