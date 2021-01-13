import unittest
from string_match import string_match


class UnitTests(unittest.TestCase):

    def test_xxcaazz_and_xxbaaz_returns_3(self):
        actual = string_match("xxcaazz", "xxbaaz")
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "xxcaazz" and "xxbaaz" to return 3')

    def test_abc_and_abc_returns_2(self):
        actual = string_match("abc", "abc")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "abc" and "abc" to return 2')

    def test_abc_and_axc_returns_0(self):
        actual = string_match("abc", "axc")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "abc" and "axc" to return 0')

    def test_hello_and_he_returns_1(self):
        actual = string_match("hello", "he")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "hello" and "he" to return 1')

    def test_he_and_hello_returns_1(self):
        actual = string_match("he", "hello")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "he" and "hello" to return 1')

    def test_h_and_hello_returns_0(self):
        actual = string_match("h", "hello")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "h" and "hello" to return 0')

    def test_blank_and_hello_returns_0(self):
        actual = string_match("", "hello")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "" and "hello" to return 0')

    def test_aabbccdd_and_abbbxxd_returns_1(self):
        actual = string_match("aabbccdd", "abbbxxd")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "aabbccdd" and "abbbxxd" to return 1')

    def test_aaxxaaxx_and_iaxxai_returns_3(self):
        actual = string_match("aaxxaaxx", "iaxxai")
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "aaxxaaxx" and "iaxxai" to return 3')

    def test_iaxxai_and_aaxxaaxx_returns_3(self):
        actual = string_match("iaxxai", "aaxxaaxx")
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling array123() with "iaxxai" and "aaxxaaxx" to return 3')


if __name__ == "__main__":
    unittest.main()
