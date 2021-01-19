import unittest
from love6 import love6


class UnitTests(unittest.TestCase):

    def test_6_and_4_returns_true(self):
        actual = love6(6, 4)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 6 and 4 to return "True"')

    def test_4_and_5_returns_false(self):
        actual = love6(4, 5)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 4 and 5 to return "False"')

    def test_1_and_5_returns_true(self):
        actual = love6(1, 5)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 1 and 5 to return "True"')

    def test_1_and_6_returns_true(self):
        actual = love6(1, 6)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 1 and 6 to return "True"')

    def test_1_and_8_returns_false(self):
        actual = love6(1, 8)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 1 and 8 to return "False"')

    def test_1_and_7_returns_true(self):
        actual = love6(1, 7)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 1 and 7 to return "True"')

    def test_7_and_5_returns_false(self):
        actual = love6(7, 5)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 7 and 5 to return "False"')

    def test_8_and_2_returns_true(self):
        actual = love6(8, 2)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 8 and 2 to return "True"')

    def test_6_and_6_returns_true(self):
        actual = love6(6, 6)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 6 and 6 to return "True"')

    def test_negative_6_and_2_returns_false(self):
        actual = love6(-6, 2)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with -6 and 2 to return "False"')

    def test_negative_4_and_negative_10_returns_true(self):
        actual = love6(-4, -10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with -4 and -10 to return "True"')

    def test_negative_7_and_1_returns_false(self):
        actual = love6(-7, 1)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with -7 and 1 to return "False"')

    def test_7_and_negative_1_returns_true(self):
        actual = love6(7, -1)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 7 and -1 to return "True"')

    def test_negative_6_and_12_returns_true(self):
        actual = love6(-6, 12)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with -6 and 12 to return "True"')

    def test_negative_2_and_negative_4_returns_false(self):
        actual = love6(-2, -4)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with -2 and -4 to return "False"')

    def test_7_and_1_returns_true(self):
        actual = love6(7, 1)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 7 and 1 to return "True"')

    def test_negative_0_and_9_returns_false(self):
        actual = love6(0, 9)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 0 and 9 to return "False"')

    def test_8_and_3_returns_false(self):
        actual = love6(8, 3)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 8 and 3 to return "False"')

    def test_3_and_3_returns_true(self):
        actual = love6(3, 3)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 3 and 3 to return "True"')

    def test_3_and_4_returns_false(self):
        actual = love6(3, 4)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling love6() with 3 and 4 to return "False"')


if __name__ == "__main__":
    unittest.main()
