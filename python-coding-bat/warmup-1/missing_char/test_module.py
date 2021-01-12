import unittest
from missing_char import missing_char


class UnitTests(unittest.TestCase):

    def test_kitten_and_1_returns_ktten(self):
        actual = missing_char("kitten", 1)
        expected = "ktten"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "kitten" and "1" to return "ktten"'
        )

    def test_kitten_and_0_returns_ktten(self):
        actual = missing_char("kitten", 0)
        expected = "itten"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "kitten" and "0" to return "itten"'
        )

    def test_kitten_and_4_returns_kittn(self):
        actual = missing_char("kitten", 4)
        expected = "kittn"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "kitten" and "4" to return "kittn"'
        )

    def test_hi_and_0_returns_i(self):
        actual = missing_char("Hi", 0)
        expected = "i"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "Hi" and "0" to return "i"'
        )

    def test_hi_and_1_returns_h(self):
        actual = missing_char("Hi", 1)
        expected = "H"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "Hi" and "1" to return "H"'
        )

    def test_code_and_0_returns_ode(self):
        actual = missing_char("code", 0)
        expected = "ode"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "code" and "0" to return "ode"'
        )

    def test_code_and_1_returns_cde(self):
        actual = missing_char("code", 1)
        expected = "cde"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "code" and "1" to return "cde"'
        )

    def test_code_and_2_returns_coe(self):
        actual = missing_char("code", 2)
        expected = "coe"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "code" and "2" to return "coe"'
        )

    def test_code_and_3_returns_ode(self):
        actual = missing_char("code", 3)
        expected = "cod"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "code" and "3" to return "cod"'
        )

    def test_chocolate_and_8_returns_chocolat(self):
        actual = missing_char("chocolate", 8)
        expected = "chocolat"
        self.assertEqual(
            actual, expected, 'Expected calling missing_char() with "chocolat" and "8" to return "chocolat"'
        )


if __name__ == "__main__":
    unittest.main()
