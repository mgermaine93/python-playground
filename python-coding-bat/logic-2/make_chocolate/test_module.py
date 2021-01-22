import unittest
from make_chocolate import make_chocolate


class UnitTests(unittest.TestCase):

    def test_4_1_9_returns_4(self):
        actual = make_chocolate(4, 1, 9)
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [4, 1, 9] to return "4"')

    def test_4_1_10_returns_negative_1(self):
        actual = make_chocolate(4, 1, 10)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [4, 1, 10] to return "-1"')

    def test_4_1_7_returns_2(self):
        actual = make_chocolate(4, 1, 7)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [4, 1, 7] to return "2"')

    def test_6_2_7_returns_2(self):
        actual = make_chocolate(6, 2, 7)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 2, 7] to return "2"')

    def test_4_1_5_returns_0(self):
        actual = make_chocolate(4, 1, 5)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [4, 1, 5] to return "0"')

    def test_4_1_4_returns_4(self):
        actual = make_chocolate(4, 1, 4)
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [4, 1, 4] to return "4"')

    def test_5_4_9_returns_4(self):
        actual = make_chocolate(5, 4, 9)
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [5, 4, 9] to return "4"')

    def test_9_3_18_returns_3(self):
        actual = make_chocolate(9, 3, 18)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [9, 3, 18] to return "3"')

    def test_3_1_9_returns_negative_1(self):
        actual = make_chocolate(3, 1, 9)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [3, 1, 9] to return "-1"')

    def test_1_2_7_returns_negative_1(self):
        actual = make_chocolate(1, 2, 7)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [1, 2, 7] to return "-1"')

    def test_1_2_6_returns_1(self):
        actual = make_chocolate(1, 2, 6)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [1, 2, 6] to return "1"')

    def test_1_2_5_returns_0(self):
        actual = make_chocolate(1, 2, 5)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [1, 2, 5] to return "0"')

    def test_6_1_10_returns_5(self):
        actual = make_chocolate(6, 1, 10)
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 1, 10] to return "5"')

    def test_6_1_11_returns_6(self):
        actual = make_chocolate(6, 1, 11)
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 1, 11] to return "6"')

    def test_6_1_12_returns_negative_1(self):
        actual = make_chocolate(6, 1, 12)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 1, 12] to return "-1"')

    def test_6_1_13_returns_negative_1(self):
        actual = make_chocolate(6, 1, 13)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 1, 13] to return "-1"')

    def test_6_2_10_returns_0(self):
        actual = make_chocolate(6, 2, 10)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 2, 10] to return "0"')

    def test_6_2_11_returns_1(self):
        actual = make_chocolate(6, 2, 11)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 2, 11] to return "1"')

    def test_6_2_12_returns_2(self):
        actual = make_chocolate(6, 2, 12)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [6, 2, 12] to return "2"')

    def test_60_100_550_returns_50(self):
        actual = make_chocolate(60, 100, 550)
        expected = 50
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [60, 100, 550] to return "50"')

    def test_1000_1000000_5000006_returns_6(self):
        actual = make_chocolate(1000, 1000000, 5000006)
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [1000, 1000000, 5000006] to return "6"')

    def test_7_1_12_returns_7(self):
        actual = make_chocolate(7, 1, 12)
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [7, 1, 12] to return "7"')

    def test_7_1_13_returns_negative_1(self):
        actual = make_chocolate(7, 1, 13)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [7, 1, 13] to return "-1"')

    def test_7_2_13_returns_3(self):
        actual = make_chocolate(7, 2, 13)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling make_chocolate() with [7, 2, 13] to return "3"')


if __name__ == "__main__":
    unittest.main()
