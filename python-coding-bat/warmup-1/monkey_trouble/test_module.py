import unittest
from monkey_trouble import monkey_trouble


class UnitTests(unittest.TestCase):

    def test_true_and_true_returns_true(self):
        actual = monkey_trouble(True, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling "monkey_trouble() with "True" and "True" to return "True"')

    def test_false_and_false_returns_true(self):
        actual = monkey_trouble(False, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling "monkey_trouble() with "False" and "False" to return "True"')

    def test_true_and_false_returns_false(self):
        actual = monkey_trouble(True, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling "monkey_trouble() with "True" and "False" to return "False"')

    def test_false_and_true_returns_false(self):
        actual = monkey_trouble(False, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling "monkey_trouble() with "False" and "True" to return "False"')


if __name__ == "__main__":
    unittest.main()
