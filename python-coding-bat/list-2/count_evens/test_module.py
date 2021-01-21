import unittest
from count_evens import count_evens


class UnitTests(unittest.TestCase):

    def test_2_1_2_3_4_returns_3(self):
        actual = count_evens([2, 1, 2, 3, 4])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [2, 1, 2, 3, 4] to return "3"')

    def test_2_2_0_returns_3(self):
        actual = count_evens([2, 2, 0])
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [2, 2, 0] to return "3"')

    def test_1_3_5_returns_0(self):
        actual = count_evens([1, 3, 5])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [1, 3, 5] to return "0"')

    def test_empty_array_returns_0(self):
        actual = count_evens([])
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [] to return "0"')

    def test_11_9_0_1_returns_1(self):
        actual = count_evens([11, 9, 0, 1])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [11, 9, 0, 1] to return "1"')

    def test_2_11_9_0_returns_2(self):
        actual = count_evens([2, 11, 9, 0])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [2, 11, 9, 0] to return "2"')

    def test_2_returns_1(self):
        actual = count_evens([2])
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [2] to return "1"')

    def test_2_5_12_returns_2(self):
        actual = count_evens([2, 5, 12])
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_evens() with [2, 5, 12] to return "2"')


if __name__ == "__main__":
    unittest.main()
