import unittest
from middle_way import middle_way


class UnitTests(unittest.TestCase):

    def test_1_2_3_and_4_5_6_returns_2_5(self):
        actual = middle_way([1, 2, 3], [4, 5, 6])
        expected = [2, 5]
        self.assertEqual(
            actual, expected, 'Expected calling middle_way() with [1, 2, 3] and [4, 5, 6] to return [2, 5]')

    def test_7_7_7_and_3_8_0_returns_7_8(self):
        actual = middle_way([7, 7, 7], [3, 8, 0])
        expected = [7, 8]
        self.assertEqual(
            actual, expected, 'Expected calling middle_way() with [7, 7, 7] and [3, 8, 0] to return [7, 8]')

    def test_5_2_9_and_1_4_5_returns_2_4(self):
        actual = middle_way([5, 2, 9], [1, 4, 5])
        expected = [2, 4]
        self.assertEqual(
            actual, expected, 'Expected calling middle_way() with [5, 2, 9] and [1, 4, 5] to return [2, 4]')

    def test_1_9_7_and_4_8_8_returns_9_8(self):
        actual = middle_way([1, 9, 7], [4, 8, 8])
        expected = [9, 8]
        self.assertEqual(
            actual, expected, 'Expected calling middle_way() with [1, 9, 7] and [4, 8, 8] to return [9, 8]')

    def test_1_2_3_and_3_1_4_returns_2_1(self):
        actual = middle_way([1, 2, 3], [3, 1, 4])
        expected = [2, 1]
        self.assertEqual(
            actual, expected, 'Expected calling middle_way() with [1, 2, 3] and [3, 1, 4] to return [2, 1]')

    def test_1_2_3_and_4_1_1_returns_2_1(self):
        actual = middle_way([1, 2, 3], [4, 1, 1])
        expected = [2, 1]
        self.assertEqual(
            actual, expected, 'Expected calling middle_way() with [1, 2, 3] and [4, 1, 1] to return [2, 1]')


if __name__ == "__main__":
    unittest.main()
