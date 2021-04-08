import unittest
from palindrome_checker import palindrome_checker


class UnitTests(unittest.TestCase):
    def test_level(self):
        actual = palindrome_checker("level")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected output to be True when calling "palindrome_checker()" with "level"')

    def test_hello_world(self):
        actual = palindrome_checker("hello world")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected output to be False when calling "palindrome_checker()" with "hello world"')

    def test_go_hang_a_salami_im_a_lasagna_hog(self):
        actual = palindrome_checker("Go hang a salami - I'm a lasagna hog")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected output to be True when calling "palindrome_checker()" with "Go hang a salami - I\'m a lasagna hog"')

    def test_race_car(self):
        actual = palindrome_checker("race car")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected output to be True when calling "palindrome_checker()" with "race car"')

    def test_level_1_level(self):
        actual = palindrome_checker("level 1 level")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected output to be True when calling "palindrome_checker()" with "level 1 level"')

    def test_LeVEL(self):
        actual = palindrome_checker("LeVEL")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected output to be [True when calling "palindrome_checker()" with "LeVEl"')

    def test_beaver(self):
        actual = palindrome_checker("beaver")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected output to be False when calling "palindrome_checker()" with "beaver"')


if __name__ == "__main__":
    unittest.main()
