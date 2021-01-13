import unittest
from string_times import string_times


class UnitTests(unittest.TestCase):

    def test_hi_and_2_returns_hihi(self):
        actual = string_times("Hi", 2)
        expected = "HiHi"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "Hi" and "2" to equal "HiHi"')

    def test_hi_and_3_returns_hihihi(self):
        actual = string_times("Hi", 3)
        expected = "HiHiHi"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "Hi" and "3" to equal "HiHiHi"')

    def test_hi_and_1_returns_hi(self):
        actual = string_times("Hi", 1)
        expected = "Hi"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "Hi" and "1" to equal "Hi"')

    def test_hi_and_0_returns_blank(self):
        actual = string_times("Hi", 0)
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "Hi" and "0" to equal ""')

    def test_hi_and_5_returns_hihi(self):
        actual = string_times("Hi", 5)
        expected = "HiHiHiHiHi"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "Hi" and "5" to equal "HiHiHiHiHi"')

    def test_oh_boy_and_2_returns_ohboyohboy(self):
        actual = string_times("Oh Boy!", 2)
        expected = "Oh Boy!Oh Boy!"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "Oh Boy!" and "2" to equal "Oh Boy!Oh Boy!"')

    def test_x_and_4_returns_xxxx(self):
        actual = string_times("x", 4)
        expected = "xxxx"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "x" and "4" to equal "xxxx"')

    def test_blank_and_4_returns_blank(self):
        actual = string_times("", 4)
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "" and "4" to equal ""')

    def test_code_and_2_returns_codecode(self):
        actual = string_times("code", 2)
        expected = "codecode"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "code" and "2" to equal "codecode"')

    def test_code_and_3_returns_codecodecode(self):
        actual = string_times("code", 3)
        expected = "codecodecode"
        self.assertEqual(
            actual, expected, 'Expected calling string_times() with "code" and "3" to equal "codecodecode"')


if __name__ == "__main__":
    unittest.main()
