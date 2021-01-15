import unittest
from reverse3 import reverse3


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_3_2_1(self):
        actual = reverse3([1, 2, 3])
        expected = [3, 2, 1]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [1, 2, 3] to return [3, 2, 1]')

    def test_5_11_9_returns_9_11_5(self):
        actual = reverse3([5, 11, 9])
        expected = [9, 11, 5]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [5, 11, 9] to return [9, 11, 5]')

    def test_7_0_0_returns_0_0_7(self):
        actual = reverse3([7, 0, 0])
        expected = [0, 0, 7]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [7, 0, 0] to return [0, 0, 7]')

    def test_2_1_2_returns_2_1_2(self):
        actual = reverse3([2, 1, 2])
        expected = [2, 1, 2]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [2, 1, 2] to return [2, 1, 2]')

    def test_1_2_1_returns_1_2_1(self):
        actual = reverse3([1, 2, 1])
        expected = [1, 2, 1]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [1, 2, 1] to return [1, 2, 1]')

    def test_2_11_3_returns_3_11_2(self):
        actual = reverse3([2, 11, 3])
        expected = [3, 11, 2]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [2, 11, 3] to return [3, 11, 2]')

    def test_0_6_5_returns_5_6_0(self):
        actual = reverse3([0, 6, 5])
        expected = [5, 6, 0]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [0, 6, 5] to return [5, 6, 0]')

    def test_7_2_3_returns_3_2_7(self):
        actual = reverse3([7, 2, 3])
        expected = [3, 2, 7]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [7, 2, 3] to return [3, 2, 7]')


if __name__ == "__main__":
    unittest.main()
