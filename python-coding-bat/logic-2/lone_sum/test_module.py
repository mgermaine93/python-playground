import unittest
from lone_sum import lone_sum


class UnitTests(unittest.TestCase):

    def test_1_2_and_3_returns_6(self):
        actual = lone_sum(1, 2, 3)
        expected = 6
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 1, 2, and 6 to return "6"')

    def test_3_2_and_3_returns_2(self):
        actual = lone_sum(3, 2, 3)
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 3, 2, and 3 to return "2"')

    def test_3_3_and_3_returns_0(self):
        actual = lone_sum(3, 3, 3)
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 3, 3, and 3 to return "0"')

    def test_9_2_and_2_returns_9(self):
        actual = lone_sum(9, 2, 2)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 9, 2, and 2 to return "9"')

    def test_2_2_9_returns_9(self):
        actual = lone_sum(2, 2, 9)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 2, 2, and 9 to return "9"')

    def test_2_9_2_returns_9(self):
        actual = lone_sum(2, 9, 2)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 2, 9, and 2 to return "9"')

    def test_2_9_3_returns_14(self):
        actual = lone_sum(2, 9, 3)
        expected = 14
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 2, 9, and 3 to return "14"')

    def test_4_2_3_returns_9(self):
        actual = lone_sum(4, 2, 3)
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 4, 2, and 3 to return "9"')

    def test_1_3_1_returns_3(self):
        actual = lone_sum(1, 3, 1)
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling lone_sum() with 1, 3, and 1 to return "3"')


if __name__ == "__main__":
    unittest.main()
