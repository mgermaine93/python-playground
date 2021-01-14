import unittest
from combo_string import combo_string


class UnitTests(unittest.TestCase):

    def test_hello_and_hi_returns_hihellohi(self):
        actual = combo_string("Hello", "hi")
        expected = "hiHellohi"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "Hello" and "hi" to return "hiHellohi"')

    def test_hi_and_hello_returns_hihellohi(self):
        actual = combo_string("hi", "Hello")
        expected = "hiHellohi"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "hi" and "Hello" to return "hiHellohi"')

    def test_aaa_and_b_returns_baaab(self):
        actual = combo_string("aaa", "b")
        expected = "baaab"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "aaa" and "b" to return "baaab"')

    def test_aaa_and_blank_returns_aaa(self):
        actual = combo_string("aaa", "")
        expected = "aaa"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "aaa" and "" to return "aaa"')

    def test_blank_and_bb_returns_bb(self):
        actual = combo_string("", "bb")
        expected = "bb"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "" and "bb" to return "bb"')

    def test_aaa_and_1234_returns_aaa1234aaa(self):
        actual = combo_string("aaa", "1234")
        expected = "aaa1234aaa"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "aaa" and "1234" to return "aaa1234aaa"')

    def test_aaa_and_bb_returns_bbaaabb(self):
        actual = combo_string("aaa", "bb")
        expected = "bbaaabb"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "aaa" and "bb" to return "bbaaabb"')

    def test_a_and_bb_returns_abba(self):
        actual = combo_string("a", "bb")
        expected = "abba"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "a" and "bb" to return "abba"')

    def test_bb_and_a_returns_abba(self):
        actual = combo_string("bb", "a")
        expected = "abba"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "bb" and "a" to return "abba"')

    def test_xyz_and_ab_returns_abxyzab(self):
        actual = combo_string("xyz", "ab")
        expected = "abxyzab"
        self.assertEqual(
            actual, expected, 'Expected calling combo_string() with "xyz" and "ab" to return "abxyzab"')


if __name__ == "__main__":
    unittest.main()
