import unittest
from make_abba import make_abba


class UnitTests(unittest.TestCase):

    def test_hi_bye_returns_hibyebyehi(self):
        actual = make_abba("Hi", "Bye")
        expected = "HiByeByeHi"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "Hi" and "Bye" to return "HiByeByeHi"')

    def test_yo_alice_returns_yoalicealiceyo(self):
        actual = make_abba("Yo", "Alice")
        expected = "YoAliceAliceYo"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "Yo" and "Alice" to return "YoAliceAliceYo"')

    def test_what_up_returns_whatupupwhat(self):
        actual = make_abba("What", "Up")
        expected = "WhatUpUpWhat"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "What" and "Up" to return "WhatUpUpWhat"')

    def test_aaa_bbb_returns_aaabbbbbbaaa(self):
        actual = make_abba("aaa", "bbb")
        expected = "aaabbbbbbaaa"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "aaa" and "bbb" to return "aaabbbbbbaaa"')

    def test_x_y_returns_xyyx(self):
        actual = make_abba("x", "y")
        expected = "xyyx"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "x" and "y" to return "xyyx"')

    def test_x_blank_returns_xx(self):
        actual = make_abba("x", "")
        expected = "xx"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "x" and "" to return "xx"')

    def test_blank_y_returns_yy(self):
        actual = make_abba("", "y")
        expected = "yy"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "" and "y" to return "yy"')

    def test_bo_ya_returns_boyayabo(self):
        actual = make_abba("Bo", "Ya")
        expected = "BoYaYaBo"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "Bo" and "Ya" to return "BoYaYaBo"')

    def test_ya_ya_returns_yayayaya(self):
        actual = make_abba("Ya", "Ya")
        expected = "YaYaYaYa"
        self.assertEqual(
            actual, expected, 'Expected calling make_abba() with "Ya" and "Ya" to return "YaYaYaYa"')


if __name__ == "__main__":
    unittest.main()
