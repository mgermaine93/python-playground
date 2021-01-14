import unittest
from first_half import first_half


class UnitTests(unittest.TestCase):

    def test_woohoo_returns_woo(self):
        actual = first_half("WooHoo")
        expected = "Woo"
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "WooHoo" to return "Woo"')

    def test_hellothere_returns_hello(self):
        actual = first_half("HelloThere")
        expected = "Hello"
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "HelloThere" to return "Hello"')

    def test_abcdef_returns_abc(self):
        actual = first_half("abcdef")
        expected = "abc"
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "abc" to return "abcdef"')

    def test_ab_returns_a(self):
        actual = first_half("ab")
        expected = "a"
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "ab" to return "a"')

    def test_blank_returns_blank(self):
        actual = first_half("")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "" to return ""')

    def test_0123456789_returns_01234(self):
        actual = first_half("0123456789")
        expected = "01234"
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "0123456789" to return "01234"')

    def test_kitten_returns_kit(self):
        actual = first_half("kitten")
        expected = "kit"
        self.assertEqual(
            actual, expected, 'Expected calling first_half() with "kitten" to return "kit"')


if __name__ == "__main__":
    unittest.main()
