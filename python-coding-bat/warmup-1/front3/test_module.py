import unittest
from front3 import front3


class UnitTests(unittest.TestCase):

    def test_java_returns_javjavjav(self):
        actual = front3("Java")
        expected = "JavJavJav"
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "Java" to return "JavJavJav"'
        )

    def test_chocolate_returns_chochocho(self):
        actual = front3("Chocolate")
        expected = "ChoChoCho"
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "Chocolate" to return "ChoChoCho"'
        )

    def test_abc_returns_abcabcabc(self):
        actual = front3("abc")
        expected = "abcabcabc"
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "abc" to return "abcabcabc"'
        )

    def test_abcxyz_returns_abcabcabc(self):
        actual = front3("abcXYZ")
        expected = "abcabcabc"
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "abcXYZ" to return "abcabcabc"'
        )

    def test_ab_returns_ababab(self):
        actual = front3("ab")
        expected = "ababab"
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "ab" to return "ababab"'
        )

    def test_a_returns_aaa(self):
        actual = front3("a")
        expected = "aaa"
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "a" to return "aaa"'
        )

    def test_blank_returns_blank(self):
        actual = front3("")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling front3() with "" to return ""'
        )


if __name__ == "__main__":
    unittest.main()
