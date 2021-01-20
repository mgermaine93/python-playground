import unittest
from close_far import close_far


class UnitTests(unittest.TestCase):

    def test_1_2_and_10_returns_true(self):
        actual = close_far(1, 2, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 1, 2, and 10 to return "True"')

    def test_1_2_and_3_returns_false(self):
        actual = close_far(1, 2, 3)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 1, 2, and 3 to return "False"')

    def test_4_1_and_3_returns_true(self):
        actual = close_far(4, 1, 3)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 4, 1, and 3 to return "True"')

    def test_4_5_and_3_returns_false(self):
        actual = close_far(4, 5, 3)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 4, 5, and 3 to return "False"')

    def test_4_3_and_5_returns_false(self):
        actual = close_far(4, 3, 5)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 4, 5, and 3 to return "False"')

    def test_negative_1_10_and_0_returns_true(self):
        actual = close_far(-1, 10, 0)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with -1, 10, and 0 to return "True"')

    def test_0_negative_1_and_10_returns_true(self):
        actual = close_far(0, -1, 10)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 0, -1, and 10 to return "True"')

    def test_10_10_and_8_returns_true(self):
        actual = close_far(10, 10, 8)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 10, 10, and 8 to return "True"')

    def test_10_8_and_9_returns_false(self):
        actual = close_far(10, 8, 9)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 10, 8, and 9 to return "False"')

    def test_8_9_and_10_returns_false(self):
        actual = close_far(8, 9, 10)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 8, 9, and 10 to return "False"')

    def test_8_9_and_7_returns_false(self):
        actual = close_far(8, 9, 7)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 8, 9, and 7 to return "False"')

    def test_8_6_and_9_returns_true(self):
        actual = close_far(8, 6, 9)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling close_far() with 8, 6, and 9 to return "True"')


if __name__ == "__main__":
    unittest.main()
