import unittest
from centered_average import centered_average


class UnitTests(unittest.TestCase):

    def test_1_2_3_4_100_returns_3(self):
        actual = centered_average([1, 2, 3, 4, 100])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [1, 2, 3, 4, 100] to return "3"')

    def test_1_1_5_5_10_8_7_returns_5(self):
        actual = centered_average([1, 1, 5, 5, 10, 8, 7])
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [1, 1, 5, 5, 10, 8, 7] to return "5"')

    def test_megative_10_negative_4_negative_2_negative_4_negative_2_negative_0_returns_negative_3(self):
        actual = centered_average([-10, -4, -2, -4, -2, 0])
        expected = -3
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [-10, -4, -2, -4, -2, 0] to return "-3"')

    def test_5_3_4_6_2_returns_4(self):
        actual = centered_average([5, 3, 4, 6, 2])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [5, 3, 4, 6, 2] to return "4"')

    def test_5_3_4_0_100_returns_4(self):
        actual = centered_average([5, 3, 4, 0, 100])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [5, 3, 4, 0, 100] to return "4"')

    def test_100_0_5_3_4_returns_4(self):
        actual = centered_average([100, 0, 5, 3, 4])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [100, 0, 5, 3, 4] to return "4"')

    def test_4_0_100_returns_4(self):
        actual = centered_average([4, 0, 100])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [4, 0, 100] to return "4"')

    def test_0_2_3_4_100_returns_3(self):
        actual = centered_average([0, 2, 3, 4, 100])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [0, 2, 3, 4, 100] to return "3"')

    def test_1_1_100_returns_1(self):
        actual = centered_average([1, 1, 100])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [1, 1, 100] to return "1"')

    def test_7_7_7_returns_7(self):
        actual = centered_average([7, 7, 7])
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [7, 7, 7] to return "7"')

    def test_1_7_8_returns_7(self):
        actual = centered_average([1, 7, 8])
        expected = 7
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [1, 7, 8] to return "7"')

    def test_1_1_99_99_returns_50(self):
        actual = centered_average([1, 1, 99, 99])
        expected = 50
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [1, 1, 99, 99] to return "50"')

    def test_1000_0_1_99_returns_50(self):
        actual = centered_average([1000, 0, 1, 99])
        expected = 50
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [1000, 0, 1, 99] to return "50"')

    def test_4_4_4_4_5_returns_4(self):
        actual = centered_average([4, 4, 4, 4, 5])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [4, 4, 4, 4, 5] to return "4"')

    def test_4_4_4_1_5_returns_4(self):
        actual = centered_average([4, 4, 4, 1, 5])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [4, 4, 4, 1, 5] to return "4"')

    def test_6_4_8_12_3_returns_6(self):
        actual = centered_average([6, 4, 8, 12, 3])
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling centered_average() with [6, 4, 8, 12, 3] to return "6"')


if __name__ == "__main__":
    unittest.main()
