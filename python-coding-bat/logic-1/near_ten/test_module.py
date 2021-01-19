import unittest
from near_ten import near_ten


class UnitTests(unittest.TestCase):

    def test_12_returns_true(self):
        actual = near_ten(12)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 12 to return "True"')

    def test_17_returns_false(self):
        actual = near_ten(17)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 17 to return "False"')

    def test_19_returns_true(self):
        actual = near_ten(19)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 19 to return "True"')

    def test_31_returns_true(self):
        actual = near_ten(31)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 31 to return "True"')

    def test_6_returns_false(self):
        actual = near_ten(6)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 6 to return "False"')

    def test_10_returns_true(self):
        actual = near_ten(10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 10 to return "True"')

    def test_11_returns_true(self):
        actual = near_ten(11)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 11 to return "True"')

    def test_21_returns_true(self):
        actual = near_ten(21)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 21 to return "True"')

    def test_22_returns_true(self):
        actual = near_ten(22)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 22 to return "True"')

    def test_23_returns_false(self):
        actual = near_ten(23)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 23 to return "False"')

    def test_54_returns_false(self):
        actual = near_ten(54)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 54 to return "False"')

    def test_155_returns_false(self):
        actual = near_ten(155)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 155 to return "False"')

    def test_158_returns_true(self):
        actual = near_ten(158)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 158 to return "True"')

    def test_3_returns_false(self):
        actual = near_ten(3)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 3 to return "False"')

    def test_1_returns_true(self):
        actual = near_ten(1)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_ten() with 1 to return "True"')


if __name__ == "__main__":
    unittest.main()
