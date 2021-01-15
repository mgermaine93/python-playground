import unittest
from common_end import common_end


class UnitTests(unittest.TestCase):

    def test_1_2_3_and_7_3_returns_true(self):
        actual = common_end([1, 2, 3], [7, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 3] and [7, 3] to return "True"')

    def test_1_2_3_and_7_3_2_returns_false(self):
        actual = common_end([1, 2, 3], [7, 3, 2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 3] and [7, 3, 2] to return "False"')

    def test_1_2_3_and_1_3_returns_true(self):
        actual = common_end([1, 2, 3], [1, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 3] and [1, 3] to return "True"')

    def test_1_2_3_and_1_returns_true(self):
        actual = common_end([1, 2, 3], [1])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 3] and [1] to return "True"')

    def test_1_2_3_and_2_returns_false(self):
        actual = common_end([1, 2, 3], [2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 3] and [2] to return "False"')


if __name__ == "__main__":
    unittest.main()
