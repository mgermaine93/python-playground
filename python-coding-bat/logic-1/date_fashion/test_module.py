import unittest
from date_fashion import date_fashion


class UnitTests(unittest.TestCase):

    def test_5_and_10_returns_2(self):
        actual = date_fashion(5, 10)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 5 and 10 to return "2"')

    def test_5_and_2_returns_0(self):
        actual = date_fashion(5, 2)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 5 and 2 to return "0"')

    def test_5_and_5_returns_1(self):
        actual = date_fashion(5, 5)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 5 and 5 to return "1"')

    def test_3_and_3_returns_1(self):
        actual = date_fashion(3, 3)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 3 and 3 to return "1"')

    def test_10_and_2_returns_0(self):
        actual = date_fashion(10, 2)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 10 and 2 to return "0"')

    def test_2_and_9_returns_0(self):
        actual = date_fashion(2, 9)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 2 and 9 to return "0"')

    def test_9_and_9_returns_2(self):
        actual = date_fashion(9, 9)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 9 and 9 to return "2"')

    def test_10_and_5_returns_2(self):
        actual = date_fashion(10, 5)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 10 and 5 to return "2"')

    def test_2_and_2_returns_0(self):
        actual = date_fashion(2, 2)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 2 and 2 to return "0"')

    def test_3_and_7_returns_1(self):
        actual = date_fashion(3, 7)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 3 and 7 to return "1"')

    def test_2_and_7_returns_0(self):
        actual = date_fashion(2, 7)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 2 and 7 to return "0"')

    def test_6_and_2_returns_0(self):
        actual = date_fashion(6, 2)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling date_fashion() with 6 and 2 to return "0"')


if __name__ == "__main__":
    unittest.main()
