import unittest
from sleep_in import sleep_in


class UnitTests(unittest.TestCase):

    def test_false_and_false_returns_true(self):
        actual = sleep_in(False, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling sleep_in() with "False" and "False" to return "True"')

    def test_true_and_false_returns_false(self):
        actual = sleep_in(True, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling sleep_in() with "True" and "False" to return "False"')

    def test_false_and_true_returns_false(self):
        actual = sleep_in(False, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling sleep_in() with "False" and "True" to return "True"')

    def test_true_and_true_returns_true(self):
        actual = sleep_in(True, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling sleep_in() with "True" and "True" to return "True"')


if __name__ == "__main__":
    unittest.main()
