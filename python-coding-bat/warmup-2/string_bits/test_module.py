import unittest
from string_bits import string_bits


class UnitTests(unittest.TestCase):

    def test_hello_returns_hlo(self):
        actual = string_bits("Hello")
        expected = "Hlo"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "Hello" to equal "Hlo"')

    def test_hi_returns_h(self):
        actual = string_bits("Hi")
        expected = "H"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "Hi" to equal "H"')

    def test_heeololeo_returns_hello(self):
        actual = string_bits("Heeololeo")
        expected = "Hello"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "Heeololeo" to equal "Hello"')

    def test_hihihi_returns_hhh(self):
        actual = string_bits("HiHiHi")
        expected = "HHH"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "HiHiHi" to equal "HHH"')

    def test_blank_returns_blank(self):
        actual = string_bits("")
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "" to equal ""')

    def test_greetings_returns_getns(self):
        actual = string_bits("Greetings")
        expected = "Getns"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "Greetings" to equal "Getns"')

    def test_chocoate_returns_coot(self):
        actual = string_bits("Chocoate")
        expected = "Coot"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "Chocoate" to equal "Coot"')

    def test_pi_returns_p(self):
        actual = string_bits("pi")
        expected = "p"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "pi" to equal "p"')

    def test_hellokitten_returns_hlokte(self):
        actual = string_bits("Hello Kitten")
        expected = "HloKte"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "Hello Kitten" to equal "HloKte"')

    def test_hxaxpxpxy_returns_happy(self):
        actual = string_bits("hxaxpxpxy")
        expected = "happy"
        self.assertEqual(
            actual, expected, 'Expected calling string_bits() with "hxaxpxpxy" to equal "happy"')


if __name__ == "__main__":
    unittest.main()
