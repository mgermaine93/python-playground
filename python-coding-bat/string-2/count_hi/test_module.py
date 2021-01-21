import unittest
from count_hi import count_hi


class UnitTests(unittest.TestCase):

    def test_abchiho_returns_1(self):
        actual = count_hi("abc hi ho")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "abc hi ho" to return "1"')

    def test_ABChihi_returns_2(self):
        actual = count_hi("ABChi hi")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "ABChi hi" to return "2"')

    def test_hihi_returns_2(self):
        actual = count_hi("hihi")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "hihi" to return "2"')

    def test_hiHIhi_returns_2(self):
        actual = count_hi("hiHIhi")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "hiHIhi" to return "2"')

    def test_empty_string_returns_0(self):
        actual = count_hi("")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "" to return "0"')

    def test_h_returns_0(self):
        actual = count_hi("h")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "h" to return "0"')

    def test_hi_returns_1(self):
        actual = count_hi("hi")
        expected = 1
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "hi" to return "1"')

    def test_HiisnoHIonahI_returns_0(self):
        actual = count_hi("Hi is no HI on ahI")
        expected = 0
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "Hi is no HI on ahI" to return "0"')

    def test_hihonotHOHIhi_returns_2(self):
        actual = count_hi("hiho not HOHIhi")
        expected = 2
        self.assertEqual(
            actual, expected, 'Expected calling count_hi() with "hiho not HOHIhi" to return "2"')


if __name__ == "__main__":
    unittest.main()
