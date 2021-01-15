import unittest
from sum3 import sum3


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_6(self):
        actual = sum3([1, 2, 3])
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 3] to return "6"')

    def test_5_11_2_returns_18(self):
        actual = sum3([5, 11, 2])
        expected = 18
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [5, 11, 2] to return "18"')

    def test_7_0_0_returns_7(self):
        actual = sum3([7, 0, 0])
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [7, 0, 0] to return "7"')

    def test_1_2_1_returns_4(self):
        actual = sum3([1, 2, 1])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 2, 1] to return "4"')

    def test_1_1_1_returns_3(self):
        actual = sum3([1, 1, 1])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [1, 1, 1] to return "3"')

    def test_2_7_2_returns_11(self):
        actual = sum3([2, 7, 2])
        expected = 11
        self.assertEqual(
            actual, expected, 'Expected calling common_end() with [2, 7, 2] to return "11"')


if __name__ == "__main__":
    unittest.main()
