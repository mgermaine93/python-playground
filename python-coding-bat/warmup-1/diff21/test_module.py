import unittest
from diff21 import diff21


class UnitTests(unittest.TestCase):

    def test_19_returns_2(self):
        actual = diff21(19)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "19" to return "2"')

    def test_10_returns_11(self):
        actual = diff21(10)
        expected = 11
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "10" to return "11"')

    def test_21_returns_0(self):
        actual = diff21(21)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "21" to return "0"')

    def test_22_returns_2(self):
        actual = diff21(22)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "22" to return "2"')

    def test_25_returns_8(self):
        actual = diff21(25)
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "25" to return "8"')

    def test_30_returns_18(self):
        actual = diff21(30)
        expected = 18
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "30" to return "18"')

    def test_0_returns_21(self):
        actual = diff21(0)
        expected = 21
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "0" to return "21"')

    def test_1_returns_20(self):
        actual = diff21(1)
        expected = 20
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "1" to return "20"')

    def test_2_returns_19(self):
        actual = diff21(2)
        expected = 19
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "2" to return "19"')

    def test_negative_1_returns_22(self):
        actual = diff21(-1)
        expected = 22
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "-1" to return "22"')

    def test_negative_2_returns_23(self):
        actual = diff21(-2)
        expected = 23
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "-2" to return "23"')

    def test_50_returns_58(self):
        actual = diff21(50)
        expected = 58
        self.assertEqual(
            actual, expected, 'Expected calling diff21() with "50" to return "58"')


if __name__ == "__main__":
    unittest.main()
