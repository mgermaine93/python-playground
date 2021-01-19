import unittest
from in1to10 import in1to10


class UnitTests(unittest.TestCase):

    def test_5_and_false_returns_true(self):
        actual = in1to10(5, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 5 and False to return "True"')

    def test_11_and_false_returns_false(self):
        actual = in1to10(11, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 11 and False to return "False"')

    def test_11_and_true_returns_true(self):
        actual = in1to10(11, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 11 and True to return "True"')

    def test_10_and_false_returns_true(self):
        actual = in1to10(10, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 10 and False to return "True"')

    def test_10_and_true_returns_true(self):
        actual = in1to10(10, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 10 and True to return "True"')

    def test_9_and_false_returns_true(self):
        actual = in1to10(9, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 9 and False to return "True"')

    def test_9_and_true_returns_false(self):
        actual = in1to10(9, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 9 and True to return "False"')

    def test_1_and_false_returns_true(self):
        actual = in1to10(1, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 1 and False to return "True"')

    def test_1_and_true_returns_true(self):
        actual = in1to10(1, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 1 and True to return "True"')

    def test_0_and_false_returns_false(self):
        actual = in1to10(0, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 0 and False to return "False"')

    def test_0_and_true_returns_true(self):
        actual = in1to10(0, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 0 and True to return "True"')

    def test_negative_1_and_false_returns_false(self):
        actual = in1to10(-1, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with -1 and False to return "False"')

    def test_negative_1_and_true_returns_true(self):
        actual = in1to10(-1, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with -1 and True to return "True"')

    def test_99_and_false_returns_false(self):
        actual = in1to10(99, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with 99 and False to return "False"')

    def test_negative_99_and_true_returns_true(self):
        actual = in1to10(-99, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling in1to10() with -99 and True to return "True"')


if __name__ == "__main__":
    unittest.main()
