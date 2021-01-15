import unittest
from make_pi import make_pi


class UnitTests(unittest.TestCase):

    def test_makepi_returns_3_1_4(self):
        actual = make_pi()
        expected = [3, 1, 4]
        self.assertEqual(
            actual, expected, 'Expected calling make_pi() to return [3, 1, 4]')


if __name__ == "__main__":
    unittest.main()
