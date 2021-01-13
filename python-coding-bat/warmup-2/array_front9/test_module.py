import unittest
from array_front9 import array_front9


class UnitTests(unittest.TestCase):

    def test_1_2_9_3_4_returns_true(self):
        actual = array_front9([1, 2, 9, 3, 4])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[1, 2, 9, 3, 4]" to return "True"')

    def test_1_2_3_4_9_returns_false(self):
        actual = array_front9([1, 2, 3, 4, 9])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[1, 2, 3, 4, 9]" to return "False"')

    def test_1_2_3_4_5_returns_false(self):
        actual = array_front9([1, 2, 3, 4, 5])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[1, 2, 3, 4, 5]" to return "False"')

    def test_9_2_3_returns_true(self):
        actual = array_front9([9, 2, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[9, 2, 3]" to return "True"')

    def test_1_9_9_returns_true(self):
        actual = array_front9([1, 9, 9])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[1, 9, 9]" to return "True"')

    def test_1_2_3_returns_false(self):
        actual = array_front9([1, 2, 3])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[1, 2, 3]" to return "False"')

    def test_1_9_returns_true(self):
        actual = array_front9([1, 9])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[1, 9]" to return "True"')

    def test_5_5_returns_false(self):
        actual = array_front9([5, 5])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[5, 5]" to return "False"')

    def test_2_returns_false(self):
        actual = array_front9([2])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[2]" to return "False"')

    def test_9_returns_true(self):
        actual = array_front9([9])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[9]" to return "True"')

    def test_blank_returns_false(self):
        actual = array_front9([])
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[]" to return "False"')

    def test_3_9_2_3_3_returns_true(self):
        actual = array_front9([3, 9, 2, 3, 3])
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling array_front9() with "[3, 9, 2, 3, 3]" to return "True"')


if __name__ == "__main__":
    unittest.main()
