import unittest
from round_sum import round_sum


class UnitTests(unittest.TestCase):

    def test_16_17_and_18_returns_60(self):
        actual = round_sum(16, 17, 18)
        expected = 60
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 16, 17, and 18 to return "60"')

    def test_12_13_and_14_returns_30(self):
        actual = round_sum(12, 13, 14)
        expected = 30
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 12, 13, and 14 to return "30"')

    def test_6_4_and_4_returns_10(self):
        actual = round_sum(6, 4, 4)
        expected = 10
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 6, 4, and 4 to return "10"')

    def test_4_6_and_5_returns_20(self):
        actual = round_sum(4, 6, 5)
        expected = 20
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 4, 6, and 5 to return "20"')

    def test_4_4_and_6_returns_10(self):
        actual = round_sum(4, 4, 6)
        expected = 10
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 4, 4, and 6 to return "10"')

    def test_9_4_and_4_returns_10(self):
        actual = round_sum(9, 4, 4)
        expected = 10
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 9, 4, 4 to return "10"')

    def test_0_0_and_1_returns_0(self):
        actual = round_sum(0, 0, 1)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 0, 0, and 1 to return "0"')

    def test_0_9_and_0_returns_10(self):
        actual = round_sum(0, 9, 0)
        expected = 10
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 0, 9, and 0 to return "10"')

    def test_10_10_and_19_returns_40(self):
        actual = round_sum(10, 10, 19)
        expected = 40
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 10, 10, and 19 to return "40"')

    def test_20_30_and_40_returns_90(self):
        actual = round_sum(20, 30, 40)
        expected = 90
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 20, 30, and 40 to return "90"')

    def test_45_21_and_30_returns_100(self):
        actual = round_sum(45, 21, 30)
        expected = 100
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 45, 21, and 30 to return "100"')

    def test_23_11_and_26_returns_60(self):
        actual = round_sum(23, 11, 26)
        expected = 60
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 23, 11, and 26 to return "60"')

    def test_23_24_and_25_returns_70(self):
        actual = round_sum(23, 24, 25)
        expected = 70
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 23, 24, and 25 to return "70"')

    def test_25_24_and_25_returns_80(self):
        actual = round_sum(25, 24, 25)
        expected = 80
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 25, 24, and 25 to return "80"')

    def test_23_24_and_29_returns_70(self):
        actual = round_sum(23, 24, 29)
        expected = 70
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 23, 24, and 29 to return "70"')

    def test_16_17_and_18_returns_60(self):
        actual = round_sum(16, 17, 18)
        expected = 60
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 16, 17, and 18 to return "60"')

    def test_11_24_and_36_returns_70(self):
        actual = round_sum(11, 24, 36)
        expected = 70
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 11, 24, and 36 to return "70"')

    def test_24_36_and_32_returns_90(self):
        actual = round_sum(24, 36, 32)
        expected = 90
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 24, 36, and 32 to return "90"')

    def test_14_12_and_26_returns_50(self):
        actual = round_sum(14, 12, 26)
        expected = 50
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 14, 12, and 26 to return "50"')

    def test_12_10_and_24_returns_40(self):
        actual = round_sum(12, 10, 24)
        expected = 40
        self.assertEqual(
            actual, expected, 'Expected calling round_sum() with 12, 10, and 24 to return "40"')


if __name__ == "__main__":
    unittest.main()
