import unittest
from xyz_there import xyz_there


class UnitTests(unittest.TestCase):

    def test_abcxyz_returns_true(self):
        actual = xyz_there("abcxyz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "abcxyz" to return "True"')

    def test_abc_period_xyz_returns_false(self):
        actual = xyz_there("abc.xyz")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "abc.xyz" to return "False"')

    def test_xyz_period_abc_returns_true(self):
        actual = xyz_there("xyz.abc")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "xyz.abc" to return "True"')

    def test_abcxy_returns_false(self):
        actual = xyz_there("abcxy")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "abcxy" to return "False"')

    def test_xyz_returns_true(self):
        actual = xyz_there("xyz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "xyz" to return "True"')

    def test_xy_returns_false(self):
        actual = xyz_there("xy")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "xy" to return "False"')

    def test_x_returns_false(self):
        actual = xyz_there("x")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "x" to return "False"')

    def test_empty_string_returns_false(self):
        actual = xyz_there("")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "" to return "False"')

    def test_abc_period_xyzxyz_returns_true(self):
        actual = xyz_there("abc.xyzxyz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "abc.xyzxyz" to return "True"')

    def test_abc_period_xxyz_returns_true(self):
        actual = xyz_there("abc.xxyz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "abc.xxyz" to return "True"')

    def test_period_xyz_returns_false(self):
        actual = xyz_there(".xyz")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with ".xyz" to return "False"')

    def test_12_period_xyz_returns_false(self):
        actual = xyz_there("12.xyz")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "12.xyz" to return "False"')

    def test_12xyz_returns_true(self):
        actual = xyz_there("12xyz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "12xyz" to return "True"')

    def test_1_period_xyz_period_xyz2_period_xyz_returns_false(self):
        actual = xyz_there("1.xyz.xyz2.xyz")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling xyz_there() with "1.xyz.xyz2.xyz" to return "False"')


if __name__ == "__main__":
    unittest.main()
