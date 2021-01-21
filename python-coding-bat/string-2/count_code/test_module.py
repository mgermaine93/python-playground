import unittest
from count_code import count_code


class UnitTests(unittest.TestCase):

    def test_aaacodebbb_returns_1(self):
        actual = count_code("aaacodebbb")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "aaacodebbb" to return "1"')

    def test_codexxcode_returns_2(self):
        actual = count_code("codexxcode")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "codexxcode" to return "2"')

    def test_cozexxcope_returns_2(self):
        actual = count_code("cozexxcope")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "cozexxcope" to return "2"')

    def test_cozfxxcope_returns_1(self):
        actual = count_code("cozfxxcope")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "cozfxxcope" to return "1"')

    def test_xxcozeyycop_returns_1(self):
        actual = count_code("xxcozeyycop")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "xxcozeyycop" to return "1"')

    def test_cozcop_returns_0(self):
        actual = count_code("cozcop")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "cozcop" to return "0"')

    def test_abcxyz_returns_0(self):
        actual = count_code("abcxyz")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "abcxyz" to return "0"')

    def test_code_returns_1(self):
        actual = count_code("code")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "code" to return "1"')

    def test_ode_returns_0(self):
        actual = count_code("ode")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "ode" to return "0"')

    def test_c_returns_0(self):
        actual = count_code("c")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "c" to return "0"')

    def test_blank_string_returns_0(self):
        actual = count_code("")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "" to return "0"')

    def test_AAcodeBBcoleCCccoreDD_returns_3(self):
        actual = count_code("AAcodeBBcoleCCccoreDD")
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "AAcodeBBcoleCCccoreDD" to return "3"')

    def test_AAcodeBBcoleCCccorfDD_returns_2(self):
        actual = count_code("AAcodeBBcoleCCccorfDD")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "AAcodeBBcoleCCccorfDD" to return "2"')

    def test_coAcodeBcoleccoreDD_returns_3(self):
        actual = count_code("coAcodeBcoleccoreDD")
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling count_code() with "coAcodeBcoleccoreDD" to return "3"')


if __name__ == "__main__":
    unittest.main()
