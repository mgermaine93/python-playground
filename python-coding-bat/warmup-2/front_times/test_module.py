import unittest
from front_times import front_times


class UnitTests(unittest.TestCase):

    def test_chocolate_and_2_returns_chocho(self):
        actual = front_times("Chocolate", 2)
        expected = "ChoCho"
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "Chocolate" and "2" to equal "ChoCho"')

    def test_chocolate_and_3_returns_chochocho(self):
        actual = front_times("Chocolate", 3)
        expected = "ChoChoCho"
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "Chocolate" and "3" to equal "ChoChoCho"')

    def test_abc_and_3_returns_abcabcabc(self):
        actual = front_times("Abc", 3)
        expected = "AbcAbcAbc"
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "Abc" and "3" to equal "AbcAbcAbc"')

    def test_ab_and_4_returns_abababab(self):
        actual = front_times("Ab", 4)
        expected = "AbAbAbAb"
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "Ab" and "4" to equal "AbAbAbAb"')

    def test_a_and_4_returns_aaaa(self):
        actual = front_times("A", 4)
        expected = "AAAA"
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "A" and "4" to equal "AAAA"')

    def test_blank_and_4_returns_blank(self):
        actual = front_times("", 4)
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "" and "4" to equal ""')

    def test_abc_and_0_returns_blank(self):
        actual = front_times("Abc", 0)
        expected = ""
        self.assertEqual(
            actual, expected, 'Expected calling front_times() with "Abc" and "0" to equal ""')


if __name__ == "__main__":
    unittest.main()
