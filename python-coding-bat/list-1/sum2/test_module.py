import unittest
from sum2 import sum2


class UnitTests(unittest.TestCase):

    def test_1_2_3_returns_3(self):
        actual = sum2([1, 2, 3])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [1, 2, 3] to return 3')

    def test_1_1_returns_2(self):
        actual = sum2([1, 1])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [1, 1] to return 2')

    def test_1_1_1_1_returns_2(self):
        actual = sum2([1, 1, 1, 1])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [1, 1, 1, 1] to return 2')

    def test_1_2_returns_3(self):
        actual = sum2([1, 2])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [1, 2] to return 3')

    def test_1_returns_1(self):
        actual = sum2([1])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [1] to return 1')

    def test_blank_returns_0(self):
        actual = sum2([])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [] to return 0')

    def test_4_5_6_returns_9(self):
        actual = sum2([4, 5, 6])
        expected = 9
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [4, 5, 6] to return 9')

    def test_4_returns_4(self):
        actual = sum2([4])
        expected = 4
        self.assertEqual(
            actual, expected, 'Expected calling sum2() with [4] to return 4')


if __name__ == "__main__":
    unittest.main()
