import unittest
from cigar_party import cigar_party


class UnitTests(unittest.TestCase):

    def test_30_and_false_returns_false(self):
        actual = cigar_party(30, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 30 and False to return "False"')

    def test_50_and_false_returns_true(self):
        actual = cigar_party(50, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 50 and False to return "True"')

    def test_70_and_true_returns_true(self):
        actual = cigar_party(70, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 70 and True to return "True"')

    def test_30_and_true_returns_false(self):
        actual = cigar_party(30, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 30 and True to return "False"')

    def test_50_and_true_returns_true(self):
        actual = cigar_party(50, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 50 and True to return "True"')

    def test_60_and_false_returns_true(self):
        actual = cigar_party(60, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 60 and False to return "True"')

    def test_61_and_false_returns_false(self):
        actual = cigar_party(61, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 61 and False to return "False"')

    def test_40_and_false_returns_true(self):
        actual = cigar_party(40, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 40 and False to return "True"')

    def test_39_and_false_returns_false(self):
        actual = cigar_party(39, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 39 and False to return "False"')

    def test_40_and_true_returns_true(self):
        actual = cigar_party(40, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 40 and True to return "True"')

    def test_39_and_true_returns_false(self):
        actual = cigar_party(39, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cigar_party() with 39 and True to return "False"')


if __name__ == "__main__":
    unittest.main()
