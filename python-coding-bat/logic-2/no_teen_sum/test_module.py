import unittest
from no_teen_sum import no_teen_sum


class UnitTests(unittest.TestCase):

    def test_1_2_and_3_returns_6(self):
        actual = no_teen_sum(1, 2, 3)
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 1, 2, and 6 to return "6"')

    def test_2_13_and_1_returns_3(self):
        actual = no_teen_sum(2, 13, 1)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 2, 13, and 1 to return "3"')

    def test_2_1_and_14_returns_3(self):
        actual = no_teen_sum(2, 1, 14)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 2, 1, and 14 to return "3"')

    def test_2_1_and_15_returns_18(self):
        actual = no_teen_sum(2, 1, 15)
        expected = 18
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 2, 1, and 15 to return "18"')

    def test_2_1_and_16_returns_19(self):
        actual = no_teen_sum(2, 1, 16)
        expected = 19
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 2, 1, and 16 to return "19"')

    def test_2_1_and_17_returns_3(self):
        actual = no_teen_sum(2, 1, 17)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 2, 1, and 17 to return "3"')

    def test_17_1_and_2_returns_3(self):
        actual = no_teen_sum(17, 1, 2)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 17, 1, and 2 to return "3"')

    def test_2_15_and_2_returns_19(self):
        actual = no_teen_sum(2, 15, 2)
        expected = 19
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 2, 15, and 2 to return "19"')

    def test_16_17_and_18_returns_16(self):
        actual = no_teen_sum(16, 17, 18)
        expected = 16
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 16, 17, and 18 to return "16"')

    def test_17_18_and_19_returns_0(self):
        actual = no_teen_sum(17, 18, 19)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 17, 18, and 19 to return "0"')

    def test_15_16_and_1_returns_32(self):
        actual = no_teen_sum(15, 16, 1)
        expected = 32
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 15, 16, and 1 to return "32"')

    def test_15_15_and_19_returns_30(self):
        actual = no_teen_sum(15, 15, 19)
        expected = 30
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 15, 15, and 19 to return "30"')

    def test_15_19_and_16_returns_31(self):
        actual = no_teen_sum(15, 19, 16)
        expected = 31
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 15, 19, and 16 to return "31"')

    def test_5_17_and_18_returns_5(self):
        actual = no_teen_sum(5, 17, 18)
        expected = 5
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 5, 17, and 18 to return "5"')

    def test_17_18_and_16_returns_16(self):
        actual = no_teen_sum(17, 18, 16)
        expected = 16
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 17, 18, and 16 to return "16"')

    def test_17_19_and_18_returns_0(self):
        actual = no_teen_sum(17, 19, 18)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling no_teen_sum() with 17, 19, and 18 to return "0"')


if __name__ == "__main__":
    unittest.main()
