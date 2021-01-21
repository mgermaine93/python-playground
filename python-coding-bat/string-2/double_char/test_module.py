import unittest
from double_char import double_char


class UnitTests(unittest.TestCase):

    def test_the_returns_tthhee(self):
        actual = double_char("The")
        expected = "TThhee"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "The" to return "TThhee"')

    def test_aabb_returns_aaaabbbb(self):
        actual = double_char("AAbb")
        expected = "AAAAbbbb"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "AAbb" to return "AAAAbbbb"')

    def test_hithere_returns_hhiitthheerree(self):
        actual = double_char("Hi-There")
        expected = "HHii--TThheerree"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "Hi-There" to return "HHii--TThheerree"')

    def test_word_returns_wwoorrdd(self):
        actual = double_char("Word!")
        expected = "WWoorrdd!!"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "Word!" to return "WWoorrdd!!"')

    def test_two_exclamation_points_returns_four_exclamation_points(self):
        actual = double_char("!!")
        expected = "!!!!"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "!!" to return "!!!!"')

    def test_empty_string_returns_empty_string(self):
        actual = double_char("")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "" to return ""')

    def test_a_returns_aa(self):
        actual = double_char("a")
        expected = "aa"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "a" to return "aa"')

    def test_one_period_returns_two_periods(self):
        actual = double_char(".")
        expected = ".."
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "." to return ".."')

    def test_aa_returns_aaaa(self):
        actual = double_char("aa")
        expected = "aaaa"
        self.assertEqual(
            actual, expected, 'Expected calling double_char() with "aa" to return "aaaa"')


if __name__ == "__main__":
    unittest.main()
