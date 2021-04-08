import unittest
from find_all_list_items import find_all_list_items


class UnitTests(unittest.TestCase):

    def test_multi_dimensional_list(self):
        actual = find_all_list_items([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)
        expected = [[0, 0, 1], [0, 1], [1, 1]]
        self.assertEqual(
            actual, expected, 'Expected output to be [[0, 0, 1], [0, 1], [1, 1]] when calling "find_all_list_items()" with [[[1, 2, 3], 2, [1, 3]], [ 1, 2, 3]]')


if __name__ == "__main__":
    unittest.main()
