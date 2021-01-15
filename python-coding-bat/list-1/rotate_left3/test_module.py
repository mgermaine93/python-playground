import unittest
from rotate_left3 import rotate_left3


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_2_3_1(self):
        actual = rotate_left3([1, 2, 3])
        expected = [2, 3, 1]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [1, 2, 3] to return [2, 3, 1]')

    def test_5_11_9_returns_11_9_5(self):
        actual = rotate_left3([5, 11, 9])
        expected = [11, 9, 5]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [5, 11, 9] to return [11, 9, 5]')

    def test_7_0_0_returns_0_0_7(self):
        actual = rotate_left3([7, 0, 0])
        expected = [0, 0, 7]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [7, 0, 0] to return [0, 0, 7]')

    def test_1_2_1_returns_2_1_1(self):
        actual = rotate_left3([1, 2, 1])
        expected = [2, 1, 1]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [1, 2, 1] to return [2, 1, 1]')

    def test_0_0_1_returns_0_1_0(self):
        actual = rotate_left3([0, 0, 1])
        expected = [0, 1, 0]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [0, 0, 1] to return [0, 1, 0]')


if __name__ == "__main__":
    unittest.main()
