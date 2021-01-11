import unittest
from not_string import not_string


class UnitTests(unittest.TestCase):

    def test_candy_returns_not_candy(self):
        actual = not_string("candy")
        expected = "not candy"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "candy" to return "not candy"'
        )

    def test_x_returns_not_x(self):
        actual = not_string("x")
        expected = "not x"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "x" to return "not x"'
        )

    def test_not_bad_returns_not_bad(self):
        actual = not_string("not bad")
        expected = "not bad"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "not bad" to return "not bad"'
        )

    def test_bad_returns_not_bad(self):
        actual = not_string("bad")
        expected = "not bad"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "bad" to return "not bad"'
        )

    def test_not_returns_not(self):
        actual = not_string("not")
        expected = "not"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "not" to return "not"'
        )

    def test_is_not_returns_not_is_not(self):
        actual = not_string("is not")
        expected = "not is not"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "is not" to return "not is not"'
        )

    def test_no_returns_not_no(self):
        actual = not_string("no")
        expected = "not no"
        self.assertEqual(
            actual, expected, 'Expected calling not_string() with "no" to return "not no"'
        )


if __name__ == "__main__":
    unittest.main()
