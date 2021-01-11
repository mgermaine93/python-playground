import unittest
from pos_neg import pos_neg


class UnitTests(unittest.TestCase):

    def test_1_and_negative_1_and_false_returns_true(self):
        actual = pos_neg(1, -1, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "1", "-1", and "False" to be "True"'
        )

    def test_negative_1_and_1_and_false_returns_true(self):
        actual = pos_neg(-1, 1, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-1", "1", and "False" to be "True"'
        )

    def test_negative_4_and_negative_5_and_true_returns_true(self):
        actual = pos_neg(-4, -5, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-4", "-5", and "True" to be "True"'
        )

    def test_negative_4_and_negative_5_and_false_returns_false(self):
        actual = pos_neg(-4, -5, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-4", "-5", and "False" to be "False"'
        )

    def test_negative_4_and_5_and_false_returns_true(self):
        actual = pos_neg(-4, 5, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-4", "5", and "False" to be "True"'
        )

    def test_negative_4_and_5_and_true_returns_false(self):
        actual = pos_neg(-4, 5, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-4", "5", and "True" to be "False"'
        )

    def test_1_and_1_and_false_returns_false(self):
        actual = pos_neg(1, 1, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "1", "1", and "False" to be "False"'
        )

    def test_negative_1_and_negative_1_and_false_returns_false(self):
        actual = pos_neg(-1, -1, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-1", "-1", and "False" to be "False"'
        )

    def test_1_and_negative_1_and_true_returns_false(self):
        actual = pos_neg(1, -1, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "1", "-1", and "True" to be "False"'
        )

    def test_negative_1_and_1_and_true_returns_false(self):
        actual = pos_neg(-1, 1, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-1", "1", and "True" to be "False"'
        )

    def test_1_and_1_and_true_returns_false(self):
        actual = pos_neg(1, 1, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "1", "1", and "True" to be "False"'
        )

    def test_negative_4_and_negative_five_and_false_returns_false(self):
        actual = pos_neg(-4, -5, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-4", "-5", and "False" to be "False"'
        )

    def test_negative_1_and_negative_1_and_true_returns_true(self):
        actual = pos_neg(-1, -1, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-1", "-1", and "True" to be "True"'
        )

    def test_5_and_negative_5_and_false_returns_true(self):
        actual = pos_neg(5, -5, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "5", "-5", and "False" to be "True"'
        )

    def test_negative_6_and_6_and_false_returns_true(self):
        actual = pos_neg(-6, 6, False)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-6", "6", and "False" to be "True"'
        )

    def test_negative_5_and_negative_6_and_false_returns_false(self):
        actual = pos_neg(-5, -6, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-5", "-6", and "False" to be "False"'
        )

    def test_negative_2_and_negative_1_and_false_returns_false(self):
        actual = pos_neg(-2, -1, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-2", "-1", and "False" to be "False"'
        )

    def test_1_and_2_and_false_returns_false(self):
        actual = pos_neg(1, 2, False)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "1", "2", and "False" to be "False"'
        )

    def test_negative_5_and_6_and_true_returns_false(self):
        actual = pos_neg(-5, 6, True)
        expected = False
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-5", "6", and "True" to be "False"'
        )

    def test_negative_5_and_negative_5_and_true_returns_true(self):
        actual = pos_neg(-5, -5, True)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected calling pos_neg() with "-5", "-5", and "True" to be "True"'
        )


if __name__ == "__main__":
    unittest.main()
