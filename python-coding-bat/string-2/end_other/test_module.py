import unittest
from end_other import end_other


class UnitTests(unittest.TestCase):

    def test_hiabc_and_abc_returns_true(self):
        actual = end_other("hiabc", "abc")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "hiabc" and "abc" to return "True"')

    def test_AbC_and_HiaBc_returns_true(self):
        actual = end_other("AbC", "HiaBc")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "AbC" and "HiaBc" to return "True"')

    def test_abc_and_abXabc_returns_true(self):
        actual = end_other("abc", "abXabc")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "abc" and "abXabc" to return "True"')

    def test_Hiabc_and_abcd_returns_false(self):
        actual = end_other("Hiabc", "abcd")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "Hiabc" and "abcd" to return "False"')

    def test_Hiabc_and_bc_returns_true(self):
        actual = end_other("Hiabc", "bc")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "Hiabc" and "bc" to return "True"')

    def test_Hiabcx_and_bc_returns_false(self):
        actual = end_other("Hiabcx", "bc")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "Hiabcx" and "bc" to return "False"')

    def test_abc_and_abc_returns_true(self):
        actual = end_other("abc", "abc")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "abc" and "abc" to return "True"')

    def test_xyz_and_12xyz_returns_true(self):
        actual = end_other("xyz", "12xyz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "xyz" and "12xyz" to return "True"')

    def test_yz_and_12xz_returns_false(self):
        actual = end_other("yz", "12xz")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "yz" and "12xz" to return "False"')

    def test_Z_and_12xz_returns_true(self):
        actual = end_other("Z", "12xz")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "Z" and "12xz" to return "True"')

    def test_12_and_12_returns_true(self):
        actual = end_other("12", "12")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "12" and "12" to return "True"')

    def test_abcXYZ_and_abcDEF_returns_false(self):
        actual = end_other("abcXYZ", "abcDEF")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "abcXYZ" and "abcDEF" to return "False"')

    def test_ab_and_ab12_returns_false(self):
        actual = end_other("ab", "ab12")
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "ab" and "ab12" to return "False"')

    def test_ab_and_12ab_returns_true(self):
        actual = end_other("ab", "12ab")
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling end_other() with "ab" and "12ab" to return "True"')


if __name__ == "__main__":
    unittest.main()
