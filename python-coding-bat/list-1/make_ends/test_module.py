import unittest
from make_ends import make_ends


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_1_3(self):
        actual = make_ends([1, 2, 3])
        expected = [1, 3]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [1, 2, 3] to return [1, 3]')

    def test_1_2_3_4_returns_1_4(self):
        actual = make_ends([1, 2, 3, 4])
        expected = [1, 4]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [1, 2, 3, 4] to return [1, 4]')

    def test_7_4_6_2_returns_7_2(self):
        actual = make_ends([7, 4, 6, 2])
        expected = [7, 2]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [7, 4, 6, 2] to return [7, 2]')

    def test_1_2_2_2_2_2_2_3_returns_1_3(self):
        actual = make_ends([1, 2, 2, 2, 2, 2, 2, 3])
        expected = [1, 3]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [1, 2, 2, 2, 2, 2, 2, 3] to return [1, 3]')

    def test_7_4_returns_7_4(self):
        actual = make_ends([7, 4])
        expected = [7, 4]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [7, 4] to return [7, 4]')

    def test_7_returns_7_7(self):
        actual = make_ends([7])
        expected = [7, 7]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [7] to return [7, 7]')

    def test_5_2_9_returns_5_9(self):
        actual = make_ends([5, 2, 9])
        expected = [5, 9]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [5, 2, 9] to return [5, 9]')

    def test_2_3_4_1_returns_2_1(self):
        actual = make_ends([2, 3, 4, 1])
        expected = [2, 1]
        self.assertEqual(
            actual, expected, 'Expected calling make_ends() with [2, 3, 4, 1] to return [2, 1]')


if __name__ == "__main__":
    unittest.main()
