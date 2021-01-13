import unittest
from last2 import last2


class UnitTests(unittest.TestCase):

    def test_hixxhi_returns_1(self):
        actual = last2("hixxhi")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "hixxhi" to equal "1"')

    def test_xaxxaxaxx_returns_1(self):
        actual = last2("xaxxaxaxx")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "xaxxaxaxx" to equal "1"')

    def test_axxxaaxx_returns_2(self):
        actual = last2("axxxaaxx")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "axxxaaxx" to equal "2"')

    def test_xxaxxaxxaxx_returns_3(self):
        actual = last2("xxaxxaxxaxx")
        expected = 3
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "xxaxxaxxaxx" to equal "3"')

    def test_xaxaxaxx_returns_0(self):
        actual = last2("xaxaxaxx")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "xaxaxaxx" to equal "0"')

    def test_xxxx_returns_2(self):
        actual = last2("xxxx")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "xxxx" to equal "2"')

    def test_13121312_returns_1(self):
        actual = last2("13121312")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "13121312" to equal "1"')

    def test_11212_returns_1(self):
        actual = last2("11212")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "11212" to equal "1"')

    def test_13121311_returns_0(self):
        actual = last2("13121311")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "13121311" to equal "0"')

    def test_1717171_returns_2(self):
        actual = last2("1717171")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "1717171" to equal "2"')

    def test_hi_returns_0(self):
        actual = last2("hi")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "hi" to equal "0"')

    def test_h_returns_0(self):
        actual = last2("h")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "h" to equal "0"')

    def test_blank_returns_0(self):
        actual = last2("")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling last2() with "" to equal "0"')


if __name__ == "__main__":
    unittest.main()
