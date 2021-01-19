import unittest
from caught_speeding import caught_speeding


class UnitTests(unittest.TestCase):

    def test_60_and_false_returns_0(self):
        actual = caught_speeding(60, False)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 60 and False to return "0"')

    def test_65_and_false_returns_1(self):
        actual = caught_speeding(65, False)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 65 and False to return "1"')

    def test_65_and_true_returns_0(self):
        actual = caught_speeding(65, True)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 65 and True to return "0"')

    def test_80_and_false_returns_1(self):
        actual = caught_speeding(80, False)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 80 and False to return "1"')

    def test_85_and_false_returns_2(self):
        actual = caught_speeding(85, False)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 85 and False to return "2"')

    def test_85_and_true_returns_1(self):
        actual = caught_speeding(85, True)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 85 and True to return "1"')

    def test_70_and_false_returns_1(self):
        actual = caught_speeding(70, False)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 70 and False to return "1"')

    def test_75_and_false_returns_1(self):
        actual = caught_speeding(75, False)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 75 and False to return "1"')

    def test_75_and_true_returns_1(self):
        actual = caught_speeding(75, True)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 75 and True to return "1"')

    def test_40_and_false_returns_0(self):
        actual = caught_speeding(40, False)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 40 and False to return "0"')

    def test_40_and_true_returns_0(self):
        actual = caught_speeding(40, True)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 40 and True to return "0"')

    def test_90_and_false_returns_2(self):
        actual = caught_speeding(90, False)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling caught_speeding() with 90 and False to return "2"')


if __name__ == "__main__":
    unittest.main()
