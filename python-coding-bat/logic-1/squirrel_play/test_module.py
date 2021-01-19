import unittest
from squirrel_play import squirrel_play


class UnitTests(unittest.TestCase):

    def test_70_and_false_returns_true(self):
        actual = squirrel_play(70, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 70 and False to return "True"')

    def test_95_and_false_returns_false(self):
        actual = squirrel_play(95, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 95 and False to return "False"')

    def test_95_and_true_returns_true(self):
        actual = squirrel_play(95, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 95 and True to return "True"')

    def test_90_and_false_returns_true(self):
        actual = squirrel_play(90, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 90 and False to return "True"')

    def test_90_and_true_returns_true(self):
        actual = squirrel_play(90, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 90 and True to return "True"')

    def test_50_and_false_returns_false(self):
        actual = squirrel_play(50, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 50 and False to return "False"')

    def test_50_and_true_returns_false(self):
        actual = squirrel_play(50, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 50 and True to return "False"')

    def test_100_and_false_returns_false(self):
        actual = squirrel_play(100, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 100 and False to return "False"')

    def test_100_and_true_returns_true(self):
        actual = squirrel_play(100, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 100 and True to return "True"')

    def test_105_and_true_returns_false(self):
        actual = squirrel_play(105, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 105 and True to return "False"')

    def test_59_and_false_returns_false(self):
        actual = squirrel_play(59, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 59 and False to return "False"')

    def test_59_and_true_returns_false(self):
        actual = squirrel_play(59, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 59 and True to return "False"')

    def test_60_and_false_returns_true(self):
        actual = squirrel_play(60, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling squirrel_play() with 60 and False to return "True"')


if __name__ == "__main__":
    unittest.main()
