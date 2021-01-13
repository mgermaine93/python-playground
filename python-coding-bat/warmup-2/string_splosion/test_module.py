import unittest
from string_splosion import string_splosion


class UnitTests(unittest.TestCase):

    def test_code_returns_ccocodcode(self):
        actual = string_splosion("Code")
        expected = "CCoCodCode"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "Code" to equal "CCoCodCode"')

    def test_abc_returns_aababc(self):
        actual = string_splosion("abc")
        expected = "aababc"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "abc" to equal "aababc"')

    def test_ab_returns_aab(self):
        actual = string_splosion("ab")
        expected = "aab"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "ab" to equal "aab"')

    def test_x_returns_x(self):
        actual = string_splosion("x")
        expected = "x"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "x" to equal "x"')

    def test_fade_returns_ffafadfade(self):
        actual = string_splosion("fade")
        expected = "ffafadfade"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "fade" to equal "ffafadfade"')

    def test_there_returns_tththetherthere(self):
        actual = string_splosion("There")
        expected = "TThTheTherThere"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "There" to equal "TThTheTherThere"')

    def test_kitten_returns_kkikitkittkittekitten(self):
        actual = string_splosion("Kitten")
        expected = "KKiKitKittKitteKitten"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "Kitten" to equal "KKiKitKittKitteKitten"')

    def test_bye_returns_bbybye(self):
        actual = string_splosion("Bye")
        expected = "BByBye"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "Bye" to equal "BByBye"')

    def test_good_returns_ggogoogood(self):
        actual = string_splosion("Good")
        expected = "GGoGooGood"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "Good" to equal "GGoGooGood"')

    def test_bad_returns_bbabad(self):
        actual = string_splosion("Bad")
        expected = "BBaBad"
        self.assertEqual(
            actual, expected, 'Expected calling string_splosion() with "Bad" to equal "BBaBad"')


if __name__ == "__main__":
    unittest.main()
