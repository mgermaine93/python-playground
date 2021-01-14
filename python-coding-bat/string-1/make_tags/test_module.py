import unittest
from make_tags import make_tags


class UnitTests(unittest.TestCase):

    def test_i_and_yay_returns_italicized_yay(self):
        actual = make_tags("i", "Yay")
        expected = "<i>Yay</i>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "i" and "Yay" to return "<i>Yay</i>"')

    def test_i_and_hello_returns_italicized_hello(self):
        actual = make_tags("i", "Hello")
        expected = "<i>Hello</i>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "i" and "Hello" to return "<i>Hello</i>"')

    def test_cite_and_yay_returns_cited_yay(self):
        actual = make_tags("cite", "Yay")
        expected = "<cite>Yay</cite>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "cite" and "Yay" to return "<cite>Yay</cite>"')

    def test_address_and_here_returns_addressed_here(self):
        actual = make_tags("address", "here")
        expected = "<address>here</address>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "address" and "here" to return "<address>here</address>"')

    def test_body_and_heart_returns_bodied_heart(self):
        actual = make_tags("body", "Heart")
        expected = "<body>Heart</body>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "body" and "Heart" to return "<body>Heart</body>"')

    def test_i_and_i_returns_italicized_i(self):
        actual = make_tags("i", "i")
        expected = "<i>i</i>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "i" and "i" to return "<i>i</i>"')

    def test_i_and_blank_returns_italicized_blank(self):
        actual = make_tags("i", "")
        expected = "<i></i>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "i" and "" to return "<i></i>"')


if __name__ == "__main__":
    unittest.main()
