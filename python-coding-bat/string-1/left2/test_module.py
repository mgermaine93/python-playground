import unittest
from left2 import left2


class UnitTests(unittest.TestCase):

    def test_hello_returns_lloHe(self):
        actual = left2("Hello")
        expected = "lloHe"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "Hello" to return "lloHe"')

    def test_java_returns_vaja(self):
        actual = left2("java")
        expected = "vaja"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "java" to return "vaja"')

    def test_hi_returns_hi(self):
        actual = left2("Hi")
        expected = "Hi"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "Hi" to return "Hi"')

    def test_code_returns_deco(self):
        actual = left2("code")
        expected = "deco"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "code" to return "deco"')

    def test_cat_returns_tca(self):
        actual = left2("cat")
        expected = "tca"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "cat" to return "tca"')

    def test_12345_returns_34512(self):
        actual = left2("12345")
        expected = "34512"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "12345" to return "34512"')

    def test_chocolate_returns_ocolateCh(self):
        actual = left2("Chocolate")
        expected = "ocolateCh"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "Chocolate" to return "ocolateCh"')

    def test_bricks_returns_icksbr(self):
        actual = left2("bricks")
        expected = "icksbr"
        self.assertEqual(
            actual, expected, 'Expected calling left2() with "bricks" to return "icksbr"')


if __name__ == "__main__":
    unittest.main()
