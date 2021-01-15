import unittest
from max_end3 import max_end3


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_3_3_3(self):
        actual = max_end3([1, 2, 3])
        expected = [3, 3, 3]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [1, 2, 3] to return [3, 3, 3]')

    def test_11_5_9_returns_11_11_11(self):
        actual = max_end3([11, 5, 9])
        expected = [11, 11, 11]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [11, 5, 9] to return [11, 11, 11]')

    def test_2_11_3_returns_3_3_3(self):
        actual = max_end3([2, 11, 3])
        expected = [3, 3, 3]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [2, 11, 3] to return [3, 3, 3]')

    def test_11_3_3_returns_11_11_11(self):
        actual = max_end3([11, 3, 3])
        expected = [11, 11, 11]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [11, 3, 3] to return [11, 11, 11]')

    def test_3_11_11_returns_11_11_11(self):
        actual = max_end3([3, 11, 11])
        expected = [11, 11, 11]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [3, 11, 11] to return [11, 11, 11]')

    def test_2_2_2_returns_2_2_2(self):
        actual = max_end3([2, 2, 2])
        expected = [2, 2, 2]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [2, 2, 2] to return [2, 2, 2]')

    def test_2_11_2_returns_2_2_2(self):
        actual = max_end3([2, 11, 2])
        expected = [2, 2, 2]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [2, 11, 2] to return [2, 2, 2]')

    def test_0_0_1_returns_1_1_1(self):
        actual = max_end3([0, 0, 1])
        expected = [1, 1, 1]
        self.assertEqual(
            actual, expected, 'Expected calling rotate_left3() with [0, 0, 1] to return [1, 1, 1]')


if __name__ == "__main__":
    unittest.main()
