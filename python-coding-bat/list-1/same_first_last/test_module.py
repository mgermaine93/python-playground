import unittest
from same_first_last import same_first_last


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_false(self):
        actual = same_first_last([1, 2, 3])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 3] to return "False"')

    def test_1_2_3_1_returns_true(self):
        actual = same_first_last([1, 2, 3, 1])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 3, 1] to return "True"')

    def test_1_2_1_returns_true(self):
        actual = same_first_last([1, 2, 1])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 1] to return "True"')

    def test_7_returns_true(self):
        actual = same_first_last([7])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [7] to return "True"')

    def test_blank_returns_false(self):
        actual = same_first_last([])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [] to return "False"')

    def test_1_2_3_4_5_1_returns_true(self):
        actual = same_first_last([1, 2, 3, 4, 5, 1])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 3, 4, 5, 1] to return "True"')

    def test_1_2_3_4_5_13_returns_false(self):
        actual = same_first_last([1, 2, 3, 4, 5, 13])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [1, 2, 3, 4, 5, 13] to return "False"')

    def test_13_2_3_4_5_13_returns_true(self):
        actual = same_first_last([13, 2, 3, 4, 5, 13])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [13, 2, 3, 4, 5, 13] to return "True"')

    def test_7_7_returns_true(self):
        actual = same_first_last([7, 7])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling first_last6() with [7, 7] to return "True"')


if __name__ == "__main__":
    unittest.main()
