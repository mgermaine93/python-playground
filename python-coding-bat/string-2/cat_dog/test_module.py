import unittest
from cat_dog import cat_dog


class UnitTests(unittest.TestCase):

    def test_catdog_returns_true(self):
        actual = cat_dog("catdog")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "catdog" to return "True"')

    def test_catcat_returns_false(self):
        actual = cat_dog("catcat")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "catcat" to return "False"')

    def test_1cat1cadodog_returns_true(self):
        actual = cat_dog("1cat1cadodog")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "1cat1cadodog" to return "True"')

    def test_catxxdogxxxdog_returns_false(self):
        actual = cat_dog("catxxdogxxxdog")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "catxxdogxxxdog" to return "False"')

    def test_catxdogxdogxcat_returns_true(self):
        actual = cat_dog("catxdogxdogxcat")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "catxdogxdogxcat" to return "True"')

    def test_catxdogxdogxca_returns_false(self):
        actual = cat_dog("catxdogxdogxca")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "catxdogxdogxca" to return "False"')

    def test_dogdogcat_returns_false(self):
        actual = cat_dog("dogdogcat")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "dogdogcat" to return "False"')

    def test_dogogcat_returns_true(self):
        actual = cat_dog("dogogcat")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "dogogcat" to return "True"')

    def test_dog_returns_false(self):
        actual = cat_dog("dog")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "dog" to return "False"')

    def test_cat_returns_false(self):
        actual = cat_dog("cat")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "cat" to return "False"')

    def test_ca_returns_true(self):
        actual = cat_dog("ca")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "ca" to return "True"')

    def test_c_returns_true(self):
        actual = cat_dog("c")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "c" to return "True"')

    def test_empty_string_returns_true(self):
        actual = cat_dog("")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling cat_dog() with "" to return "True"')


if __name__ == "__main__":
    unittest.main()
