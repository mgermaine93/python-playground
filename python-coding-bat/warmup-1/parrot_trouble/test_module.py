import unittest
from parrot_trouble import parrot_trouble


class UnitTests(unittest.TestCase):

    def test_true_and_6_returns_true(self):
        actual = parrot_trouble(True, 6)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "True" and "6" to return "True"')

    def test_true_and_7_returns_false(self):
        actual = parrot_trouble(True, 7)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "True" and "7" to return "False"')

    def test_false_and_6_returns_true(self):
        actual = parrot_trouble(False, 6)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "False" and "6" to return "False"')

    def test_true_and_21_returns_true(self):
        actual = parrot_trouble(True, 21)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "True" and "21" to return "True"')

    def test_false_and_21_returns_false(self):
        actual = parrot_trouble(False, 21)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "False" and "21" to return "False"')

    def test_false_and_20_returns_false(self):
        actual = parrot_trouble(False, 20)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "False" and "20" to return "False"')

    def test_true_and_23_returns_true(self):
        actual = parrot_trouble(True, 23)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "True" and "23" to return "True"')

    def test_false_and_23_returns_false(self):
        actual = parrot_trouble(False, 23)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "False" and "23" to return "False"')

    def test_true_and_20_returns_false(self):
        actual = parrot_trouble(True, 20)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "True" and "20" to return "False"')

    def test_false_and_12_returns_false(self):
        actual = parrot_trouble(False, 12)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling parrot_trouble with "False" and "12" to return "False"')


if __name__ == "__main__":
    unittest.main()
