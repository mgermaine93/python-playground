import unittest
from without_end import without_end


class UnitTests(unittest.TestCase):

    def test_hello_returns_ell(self):
        actual = without_end("Hello")
        expected = "ell"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "Hello" to return "ell"')

    def test_java_returns_av(self):
        actual = without_end("java")
        expected = "av"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "Java" to return "av"')

    def test_coding_returns_odin(self):
        actual = without_end("coding")
        expected = "odin"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "coding" to return "odin"')

    def test_code_returns_od(self):
        actual = without_end("code")
        expected = "od"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "code" to return "od"')

    def test_ab_returns_blank(self):
        actual = without_end("ab")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "ab" to return ""')

    def test_chocolate_returns_hocolate(self):
        actual = without_end("Chocolate!")
        expected = "hocolate"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "Chocolate!" to return "hocolate"')

    def test_kitten_returns_itte(self):
        actual = without_end("kitten")
        expected = "itte"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "kitten" to return "itte"')

    def test_woohoo_returns_ooho(self):
        actual = without_end("woohoo")
        expected = "ooho"
        self.assertEqual(
            actual, expected, 'Expected calling without_end() with "woohoo" to return "ooho"')


if __name__ == "__main__":
    unittest.main()
