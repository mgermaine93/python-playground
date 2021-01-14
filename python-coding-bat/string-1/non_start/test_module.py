import unittest
from non_start import non_start


class UnitTests(unittest.TestCase):

    def test_hello_and_there_returns_ellohere(self):
        actual = non_start("Hello", "There")
        expected = "ellohere"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "Hello" and "There" to return "ellohere"')

    def test_java_and_code_returns_avaode(self):
        actual = non_start("java", "code")
        expected = "avaode"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "java" and "code" to return "avaode"')

    def test_shotl_and_java_returns_hotlava(self):
        actual = non_start("shotl", "java")
        expected = "hotlava"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "shotl" and "java" to return "hotlava"')

    def test_ab_and_xy_returns_by(self):
        actual = non_start("ab", "xy")
        expected = "by"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "ab" and "xy" to return "by"')

    def test_ab_and_x_returns_b(self):
        actual = non_start("ab", "x")
        expected = "b"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "ab" and "x" to return "b"')

    def test_x_and_ac_returns_c(self):
        actual = non_start("x", "ac")
        expected = "c"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "x" and "ac" to return "c"')

    def test_a_and_x_returns_blank(self):
        actual = non_start("a", "x")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "a" and "x" to return ""')

    def test_kit_and_kat_returns_itat(self):
        actual = non_start("kit", "kat")
        expected = "itat"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "kit" and "kat" to return "itat"')

    def test_mart_and_dart_returns_artart(self):
        actual = non_start("mart", "dart")
        expected = "artart"
        self.assertEqual(
            actual, expected, 'Expected calling non_start() with "mart" and "dart" to return "artart"')


if __name__ == "__main__":
    unittest.main()
