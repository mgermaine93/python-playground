import unittest
from sum13 import sum13


class UnitTests(unittest.TestCase):

    def test_1_2_2_1_returns_6(self):
        actual = sum13([1, 2, 2, 1])
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [1, 2, 2, 1] to return "6"')

    def test_1_1_returns_2(self):
        actual = sum13([1, 1])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [1, 1] to return "2"')

    def test_1_2_2_1_13_returns_6(self):
        actual = sum13([1, 2, 2, 1, 13])
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [1, 2, 2, 1, 13] to return "6"')

    def test_1_2_13_2_1_13_returns_4(self):
        actual = sum13([1, 2, 13, 2, 1, 13])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [1, 2, 13, 2, 1, 13] to return "4"')

    def test_13_1_2_13_2_1_13_returns_3(self):
        actual = sum13([13, 1, 2, 13, 2, 1, 13])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [13, 1, 2, 13, 2, 1, 13] to return "3"')

    def test_empty_list_returns_0(self):
        actual = sum13([])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [] to return "0"')

    def test_13_returns_0(self):
        actual = sum13([13])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [13] to return "0"')

    def test_13_13_returns_0(self):
        actual = sum13([13, 13])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [13, 13] to return "0"')

    def test_13_0_13_returns_0(self):
        actual = sum13([13, 0, 13])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [13, 0, 13] to return "0"')

    def test_13_1_13_returns_0(self):
        actual = sum13([13, 1, 13])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [13, 1, 13] to return "0"')

    def test_5_7_2_returns_14(self):
        actual = sum13([5, 7, 2])
        expected = 14
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [5, 7, 2] to return "14"')

    def test_5_13_2_returns_5(self):
        actual = sum13([5, 13, 2])
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [5, 13, 2] to return "5"')

    def test_0_returns_0(self):
        actual = sum13([0])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [0] to return "0"')

    def test_13_0_returns_0(self):
        actual = sum13([13, 0])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum13() with [13, 0] to return "0"')


if __name__ == "__main__":
    unittest.main()
