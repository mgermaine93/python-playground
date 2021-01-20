import unittest
from lucky_sum import lucky_sum


class UnitTests(unittest.TestCase):

    def test_1_2_and_3_returns_6(self):
        actual = lucky_sum(1, 2, 3)
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 1, 2, and 6 to return "6"')

    def test_1_2_and_13_returns_3(self):
        actual = lucky_sum(1, 2, 13)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 1, 2, and 13 to return "3"')

    def test_1_13_and_3_returns_1(self):
        actual = lucky_sum(1, 13, 3)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 1, 13, and 3 to return "1"')

    def test_1_13_and_13_returns_1(self):
        actual = lucky_sum(1, 13, 13)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 1, 13, and 13 to return "1"')

    def test_6_5_and_2_returns_13(self):
        actual = lucky_sum(6, 5, 2)
        expected = 13
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 6, 5, and 2 to return "13"')

    def test_13_2_and_3_returns_0(self):
        actual = lucky_sum(13, 2, 3)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 13, 2, and 3 to return "0"')

    def test_13_2_and_13_returns_0(self):
        actual = lucky_sum(13, 2, 13)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 13, 2, and 13 to return "0"')

    def test_13_13_and_2_returns_0(self):
        actual = lucky_sum(13, 13, 2)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 13, 13, and 2 to return "0"')

    def test_9_4_and_13_returns_13(self):
        actual = lucky_sum(9, 4, 13)
        expected = 13
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 9, 4, and 13 to return "13"')

    def test_8_13_and_2_returns_8(self):
        actual = lucky_sum(8, 13, 2)
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 8, 13, and 2 to return "8"')

    def test_7_2_and_1_returns_10(self):
        actual = lucky_sum(7, 2, 1)
        expected = 10
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 7, 2, and 1 to return "10"')

    def test_3_3_and_13_returns_6(self):
        actual = lucky_sum(3, 3, 13)
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling lucky_sum() with 3, 3, and 13 to return "6"')


if __name__ == "__main__":
    unittest.main()
