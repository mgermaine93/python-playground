import unittest
from make_out_word import make_out_word


class UnitTests(unittest.TestCase):

    def test_two_carrots_and_yay_returns_carroted_yay(self):
        actual = make_out_word("<<>>", "Yay")
        expected = "<<Yay>>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "<<>>" and "Yay" to return "<<Yay>>"')

    def test_two_carrots_and_woohoo_returns_carroted_woohoo(self):
        actual = make_out_word("<<>>", "WooHoo")
        expected = "<<WooHoo>>"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "<<>>" and "WooHoo" to return "<<WooHoo>>"')

    def test_two_square_brackets_and_word_returns_bracketed_word(self):
        actual = make_out_word("[[]]", "word")
        expected = "[[word]]"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "[[]]" and "word" to return "[[word]]"')

    def test_hhoo_and_hello_returns_hhhellooo_yay(self):
        actual = make_out_word("HHoo", "Hello")
        expected = "HHHellooo"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "HHoo" and "Hello" to return "HHHellooo"')

    def test_abyz_and_yay_returns_abyayyz(self):
        actual = make_out_word("abyz", "YAY")
        expected = "abYAYyz"
        self.assertEqual(
            actual, expected, 'Expected calling make_tags() with "abyz" and "YAY" to return "abYAYyz"')


if __name__ == "__main__":
    unittest.main()
