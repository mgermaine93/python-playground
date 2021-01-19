import unittest
from sorta_sum import sorta_sum


class UnitTests(unittest.TestCase):

    def test_3_and_4_returns_7(self):
        actual = sorta_sum(3, 4)
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 3 and 4 to return "7"')

    def test_9_and_4_returns_20(self):
        actual = sorta_sum(9, 4)
        expected = 20
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 9 and 4 to return "20"')

    def test_10_and_11_returns_21(self):
        actual = sorta_sum(10, 11)
        expected = 21
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 10 and 11 to return "21"')

    def test_12_and_negative_3_returns_9(self):
        actual = sorta_sum(12, -3)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 12 and -3 to return "9"')

    def test_negative_3_and_12_returns_9(self):
        actual = sorta_sum(-3, 12)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with -3 and 12 to return "9"')

    def test_4_and_5_returns_9(self):
        actual = sorta_sum(4, 5)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 4 and 5 to return "9"')

    def test_4_and_6_returns_20(self):
        actual = sorta_sum(4, 6)
        expected = 20
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 4 and 6 to return "20"')

    def test_14_and_7_returns_21(self):
        actual = sorta_sum(14, 7)
        expected = 21
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 14 and 7 to return "21"')

    def test_14_and_6_returns_20(self):
        actual = sorta_sum(14, 6)
        expected = 20
        self.assertEqual(
            actual, expected, 'Expected calling sorta_sum() with 14 and 6 to return "20"')


if __name__ == "__main__":
    unittest.main()
