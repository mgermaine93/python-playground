import unittest
from array_count9 import array_count9


class UnitTests(unittest.TestCase):

    def test_1_2_9_returns_1(self):
        actual = array_count9([1, 2, 9])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[1, 2, 9]" to equal "1"')

    def test_1_9_9_returns_2(self):
        actual = array_count9([1, 9, 9])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[1, 9, 9]" to equal "2"')

    def test_1_9_9_3_9_returns_3(self):
        actual = array_count9([1, 9, 9, 3, 9])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[1, 9, 9, 3, 9]" to equal "3"')

    def test_1_2_3_returns_0(self):
        actual = array_count9([1, 2, 3])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[1, 2, 3]" to equal "0"')

    def test_blank_array_returns_0(self):
        actual = array_count9([])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[]" to equal "0"')

    def test_4_2_4_3_1_returns_0(self):
        actual = array_count9([4, 2, 4, 3, 1])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[4, 2, 4, 3, 1]" to equal "0"')

    def test_9_2_4_3_1_returns_1(self):
        actual = array_count9([9, 2, 4, 3, 1])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling array_count9() with "[9, 2, 4, 3, 1]" to equal "1"')


if __name__ == "__main__":
    unittest.main()
