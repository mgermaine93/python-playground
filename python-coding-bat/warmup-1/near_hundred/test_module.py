import unittest
from near_hundred import near_hundred


class UnitTests(unittest.TestCase):

    def test_93_returns_true(self):
        actual = near_hundred(93)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "93" to return "True"')

    def test_90_returns_true(self):
        actual = near_hundred(90)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "90" to return "True"')

    def test_89_returns_false(self):
        actual = near_hundred(89)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "89" to return "False"')

    def test_110_returns_true(self):
        actual = near_hundred(110)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "110" to return "True"')

    def test_111_returns_false(self):
        actual = near_hundred(111)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "111" to return "False"')

    def test_121_returns_false(self):
        actual = near_hundred(121)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "121" to return "False"')

    def test_negative_101_returns_false(self):
        actual = near_hundred(-101)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "-101" to return "False"')

    def test_negative_209_returns_false(self):
        actual = near_hundred(-209)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "-209" to return "False"')

    def test_190_returns_true(self):
        actual = near_hundred(190)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "190" to return "True"')

    def test_209_returns_true(self):
        actual = near_hundred(209)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "209" to return "True"')

    def test_0_returns_true(self):
        actual = near_hundred(0)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "0" to return "False"')

    def test_5_returns_false(self):
        actual = near_hundred(5)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "5" to return "False"')

    def test_negative_50_returns_false(self):
        actual = near_hundred(-50)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "-50" to return "False"')

    def test_191_returns_true(self):
        actual = near_hundred(191)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "191" to return "True"')

    def test_189_returns_false(self):
        actual = near_hundred(189)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "189" to return "False"')

    def test_200_returns_true(self):
        actual = near_hundred(200)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "200" to return "True"')

    def test_210_returns_true(self):
        actual = near_hundred(210)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "210" to return "True"')

    def test_211_returns_false(self):
        actual = near_hundred(211)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "211" to return "True"')

    def test_290_returns_false(self):
        actual = near_hundred(290)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling near_hundred() with "290" to return "False"')


if __name__ == "__main__":
    unittest.main()
