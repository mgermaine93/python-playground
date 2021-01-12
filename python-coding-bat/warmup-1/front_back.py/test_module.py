import unittest
from front_back import front_back


class UnitTests(unittest.TestCase):

    def test_code_returns_eodc(self):
        actual = front_back("code")
        expected = "eodc"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "code" to return "eodc"'
        )

    def test_a_returns_a(self):
        actual = front_back("a")
        expected = "a"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "a" to return "a"'
        )

    def test_ab_returns_ba(self):
        actual = front_back("ab")
        expected = "ba"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "ab" to return "ba"'
        )

    def test_abc_returns_cba(self):
        actual = front_back("abc")
        expected = "cba"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "abc" to return "cba"'
        )

    def test_black_returns_blank(self):
        actual = front_back("")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "" to return ""'
        )

    def test_chocolate_returns_ehocolatC(self):
        actual = front_back("Chocolate")
        expected = "ehocolatC"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "Chocolate" to return "ehocolatC"'
        )

    def test_aavJ_returns_Java(self):
        actual = front_back("aavJ")
        expected = "Java"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "aavJ" to return "Java"'
        )

    def test_hello_returns_oellh(self):
        actual = front_back("hello")
        expected = "oellh"
        self.assertEqual(
            actual, expected, 'Expected calling front_back() with "hello" to return "oellh"'
        )


if __name__ == "__main__":
    unittest.main()
