import unittest
from sum67 import sum67


class UnitTests(unittest.TestCase):

    def test_1_2_2_returns_5(self):
        actual = sum67([1, 2, 2])
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [1, 2, 2] to return "5"')

    def test_1_2_2_6_99_99_7_returns_5(self):
        actual = sum67([1, 2, 2, 6, 99, 99, 7])
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [1, 2, 2, 6, 99, 99, 7] to return "5"')

    def test_1_1_6_7_2_returns_4(self):
        actual = sum67([1, 1, 6, 7, 2])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [1, 1, 6, 7, 2] to return "4"')

    def test_1_6_2_2_7_1_6_99_99_7_returns_2(self):
        actual = sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [1, 6, 2, 2, 7, 1, 6, 99, 99, 7] to return "2"')

    def test_1_6_2_6_2_7_1_6_99_99_7_returns_2(self):
        actual = sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7] to return "2"')

    def test_2_7_6_2_6_7_2_7_returns_18(self):
        actual = sum67([2, 7, 6, 2, 6, 7, 2, 7])
        expected = 18
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [2, 7, 6, 2, 6, 7, 2, 7] to return "18"')

    def test_2_7_6_2_6_2_7_returns_9(self):
        actual = sum67([2, 7, 6, 2, 6, 2, 7])
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [2, 7, 6, 2, 6, 2, 7] to return "9"')

    def test_1_6_7_7_returns_8(self):
        actual = sum67([1, 6, 7, 7])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [1, 6, 7, 7] to return "8"')

    def test_6_7_1_6_7_7_returns_8(self):
        actual = sum67([6, 7, 1, 6, 7, 7])
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [6, 7, 1, 6, 7, 7] to return "8"')

    def test_6_8_1_6_7_returns_0(self):
        actual = sum67([6, 8, 1, 6, 7])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [6, 8, 1, 6, 7] to return "0"')

    def test_empty_list_returns_0(self):
        actual = sum67([])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [] to return "0"')

    def test_6_7_11_returns_11(self):
        actual = sum67([6, 7, 11])
        expected = 11
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [6, 7, 11] to return "11"')

    def test_11_6_7_11_returns_22(self):
        actual = sum67([11, 6, 7, 11])
        expected = 22
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [11, 6, 7, 11] to return "22"')

    def test_2_2_6_7_7_returns_11(self):
        actual = sum67([2, 2, 6, 7, 7])
        expected = 11
        self.assertEqual(
            actual, expected, 'Expected calling sum67() with [2, 2, 6, 7, 7] to return "11"')


if __name__ == "__main__":
    unittest.main()
