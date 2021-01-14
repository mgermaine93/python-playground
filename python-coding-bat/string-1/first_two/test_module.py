import unittest
from first_two import first_two


class UnitTests(unittest.TestCase):

    def test_hello_returns_he(self):
        actual = first_two("Hello")
        expected = "He"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "Hello" to return "He"')

    def test_abcdefg_returns_ab(self):
        actual = first_two("abcdefg")
        expected = "ab"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "abcdefg" to return "ab"')

    def test_ab_returns_ab(self):
        actual = first_two("ab")
        expected = "ab"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "ab" to return "ab"')

    def test_a_returns_a(self):
        actual = first_two("a")
        expected = "a"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "a" to return "a"')

    def test_blank_returns_blank(self):
        actual = first_two("")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "" to return ""')

    def test_kitten_returns_ki(self):
        actual = first_two("Kitten")
        expected = "Ki"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "Kitten" to return "Ki"')

    def test_hi_returns_hi(self):
        actual = first_two("hi")
        expected = "hi"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "hi" to return "hi"')

    def test_hiya_returns_hi(self):
        actual = first_two("hiya")
        expected = "hi"
        self.assertEqual(
            actual, expected, 'Expected calling first_two() with "hiya" to return "hi"')


if __name__ == "__main__":
    unittest.main()
