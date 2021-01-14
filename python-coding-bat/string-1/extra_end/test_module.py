import unittest
from extra_end import extra_end


class UnitTests(unittest.TestCase):

    def test_hello_returns_lololo(self):
        actual = extra_end("Hello")
        expected = "lololo"
        self.assertEqual(
            actual, expected, 'Expected calling extra_end() with "Hello" to return "lololo"')

    def test_ab_returns_ababab(self):
        actual = extra_end("ab")
        expected = "ababab"
        self.assertEqual(
            actual, expected, 'Expected calling extra_end() with "ab" to return "ababab"')

    def test_hi_returns_hihihi(self):
        actual = extra_end("Hi")
        expected = "HiHiHi"
        self.assertEqual(
            actual, expected, 'Expected calling extra_end() with "Hi" to return "HiHiHi"')

    def test_candy_returns_dydydy(self):
        actual = extra_end("Candy")
        expected = "dydydy"
        self.assertEqual(
            actual, expected, 'Expected calling extra_end() with "Candy" to return "dydydy"')

    def test_code_returns_code(self):
        actual = extra_end("Code")
        expected = "dedede"
        self.assertEqual(
            actual, expected, 'Expected calling extra_end() with "Code" to return "dedede"')


if __name__ == "__main__":
    unittest.main()
