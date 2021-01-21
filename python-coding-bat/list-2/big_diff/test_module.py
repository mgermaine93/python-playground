import unittest
from big_diff import big_diff


class UnitTests(unittest.TestCase):

    def test_10_3_5_6_returns_7(self):
        actual = big_diff([10, 3, 5, 6])
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [10, 3, 5, 6] to return "7"')

    def test_7_2_10_9_returns_8(self):
        actual = big_diff([7, 2, 10, 9])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [7, 2, 10, 9] to return "8"')

    def test_2_10_7_2_returns_8(self):
        actual = big_diff([2, 10, 7, 2])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [2, 10, 7, 2] to return "8"')

    def test_2_10_returns_8(self):
        actual = big_diff([2, 10])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [2, 10] to return "8"')

    def test_10_2_returns_8(self):
        actual = big_diff([10, 2])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [10, 2] to return "8"')

    def test_10_0_returns_10(self):
        actual = big_diff([10, 0])
        expected = 10
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [10, 0] to return "10"')

    def test_2_3_returns_1(self):
        actual = big_diff([2, 3])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [2, 3] to return "1"')

    def test_2_2_returns_0(self):
        actual = big_diff([2, 2])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [2, 2] to return "0"')

    def test_2_returns_0(self):
        actual = big_diff([2])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [2] to return "0"')

    def test_5_1_6_1_9_9_returns_8(self):
        actual = big_diff([5, 1, 6, 1, 9, 9])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [5, 1, 6, 1, 9, 9] to return "8"')

    def test_7_6_8_5_returns_3(self):
        actual = big_diff([7, 6, 8, 5])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [7, 6, 8, 5] to return "3"')

    def test_7_7_6_8_5_5_6_returns_3(self):
        actual = big_diff([7, 7, 6, 8, 5, 5, 6])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling big_diff() with [7, 7, 6, 8, 5, 5, 6] to return "3"')


if __name__ == "__main__":
    unittest.main()
