import unittest
from sum_double import sum_double


class UnitTests(unittest.TestCase):

    def test_1_and_2_returns_3(self):
        actual = sum_double(1, 2)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "1" and "2" to equal "3"')

    def test_3_and_2_returns_5(self):
        actual = sum_double(3, 2)
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "3" and "2" to equal "5"')

    def test_2_and_2_returns_8(self):
        actual = sum_double(2, 2)
        expected = 8
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "2" and "2" to equal "8"')

    def test_negative_1_and_0_returns_negative_1(self):
        actual = sum_double(-1, 0)
        expected = -1
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "-1" and "0" to equal "-1"')

    def test_3_and_3_returns_12(self):
        actual = sum_double(3, 3)
        expected = 12
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "3" and "3" to equal "12"')

    def test_0_and_0_returns_0(self):
        actual = sum_double(0, 0)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "0" and "0" to equal "0"')

    def test_0_and_1_returns_1(self):
        actual = sum_double(0, 1)
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "0" and "1" to equal "1"')

    def test_3_and_4_returns_7(self):
        actual = sum_double(3, 4)
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling sum_double with "3" and "4" to equal "7"')


if __name__ == "__main__":
    unittest.main()
