import unittest
from make_bricks import make_bricks


class UnitTests(unittest.TestCase):

    def test_3_1_and_8_returns_true(self):
        actual = make_bricks(3, 1, 8)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 3, 1, and 8 to return "True"')

    def test_3_1_and_9_returns_false(self):
        actual = make_bricks(3, 1, 9)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 3, 1, and 9 to return "False"')

    def test_3_2_and_10_returns_true(self):
        actual = make_bricks(3, 2, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 3, 2, and 10 to return "True"')

    def test_3_2_and_8_returns_true(self):
        actual = make_bricks(3, 2, 8)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 3, 2, and 8 to return "True"')

    def test_3_2_and_9_returns_false(self):
        actual = make_bricks(3, 2, 9)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 3, 2, and 9 to return "False"')

    def test_6_1_and_11_returns_true(self):
        actual = make_bricks(6, 1, 11)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 6, 1, and 11 to return "True"')

    def test_6_0_and_11_returns_false(self):
        actual = make_bricks(6, 0, 11)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 6, 0, and 11 to return "False"')

    def test_1_4_and_11_returns_true(self):
        actual = make_bricks(1, 4, 11)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 1, 4, and 11 to return "True"')

    def test_0_3_and_10_returns_true(self):
        actual = make_bricks(0, 3, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 0, 3, and 10 to return "True"')

    def test_1_4_and_12_returns_false(self):
        actual = make_bricks(1, 4, 12)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 1, 4, and 12 to return "False"')

    def test_3_1_and_7_returns_true(self):
        actual = make_bricks(3, 1, 7)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 3, 1, and 7 to return "True"')

    def test_1_1_and_7_returns_false(self):
        actual = make_bricks(1, 1, 7)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 1, 1, and 7 to return "False"')

    def test_2_1_and_7_returns_true(self):
        actual = make_bricks(2, 1, 7)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 2, 1, and 7 to return "True"')

    def test_7_1_and_11_returns_true(self):
        actual = make_bricks(7, 1, 11)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 7, 1, and 11 to return "True"')

    def test_7_1_and_8_returns_true(self):
        actual = make_bricks(7, 1, 8)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 7, 1, and 8 to return "True"')

    def test_7_1_and_13_returns_false(self):
        actual = make_bricks(7, 1, 13)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 7, 1, and 13 to return "False"')

    def test_43_1_and_46_returns_true(self):
        actual = make_bricks(43, 1, 46)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 43, 1, and 46 to return "True"')

    def test_40_1_and_46_returns_false(self):
        actual = make_bricks(40, 1, 46)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 40, 1, and 46 to return "False"')

    def test_40_2_and_47_returns_true(self):
        actual = make_bricks(40, 2, 47)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 40, 2, and 47 to return "True"')

    def test_40_2_and_50_returns_true(self):
        actual = make_bricks(40, 2, 50)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 40, 2, and 50 to return "True"')

    def test_40_2_and_52_returns_false(self):
        actual = make_bricks(40, 2, 52)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 40, 2, and 52 to return "False"')

    def test_22_2_and_33_returns_false(self):
        actual = make_bricks(22, 2, 33)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 22, 2, and 33 to return "False"')

    def test_0_2_and_10_returns_true(self):
        actual = make_bricks(0, 2, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 0, 2, and 10 to return "True"')

    def test_1000000_1000_and_1000100_returns_true(self):
        actual = make_bricks(1000000, 1000, 1000100)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 1000000, 1000, and 1000100 to return "True"')

    def test_2_1000000_and_100003_returns_false(self):
        actual = make_bricks(2, 1000000, 100003)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 2, 1000000, and 100003 to return "False"')

    def test_20_0_and_19_returns_true(self):
        actual = make_bricks(20, 0, 19)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 20, 0, and 19 to return "True"')

    def test_20_0_and_21_returns_false(self):
        actual = make_bricks(20, 0, 21)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 20, 0, and 21 to return "False"')

    def test_20_4_and_51_returns_false(self):
        actual = make_bricks(20, 4, 51)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 20, 4, and 51 to return "False"')

    def test_20_4_and_39_returns_true(self):
        actual = make_bricks(20, 4, 39)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling make_bricks() with 20, 4, and 39 to return "True"')


if __name__ == "__main__":
    unittest.main()
