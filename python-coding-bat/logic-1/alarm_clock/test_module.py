import unittest
from alarm_clock import alarm_clock


class UnitTests(unittest.TestCase):

    def test_1_and_false_returns_700(self):
        actual = alarm_clock(1, False)
        expected = "7:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 1 and False to return "7:00"')

    def test_5_and_false_returns_700(self):
        actual = alarm_clock(5, False)
        expected = "7:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 5 and False to return "7:00"')

    def test_0_and_false_returns_1000(self):
        actual = alarm_clock(0, False)
        expected = "10:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 0 and False to return "10:00"')

    def test_6_and_false_returns_1000(self):
        actual = alarm_clock(6, False)
        expected = "10:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 6 and False to return "10:00"')

    def test_0_and_true_returns_off(self):
        actual = alarm_clock(0, True)
        expected = "off"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 0 and True to return "off"')

    def test_6_and_true_returns_off(self):
        actual = alarm_clock(6, True)
        expected = "off"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 6 and True to return "off"')

    def test_1_and_true_returns_1000(self):
        actual = alarm_clock(1, True)
        expected = "10:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 1 and True to return "10:00"')

    def test_3_and_true_returns_1000(self):
        actual = alarm_clock(3, True)
        expected = "10:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 3 and True to return "10:00"')

    def test_5_and_true_returns_1000(self):
        actual = alarm_clock(5, True)
        expected = "10:00"
        self.assertEqual(
            actual, expected, 'Expected calling alarm_clock() with 5 and True to return "10:00"')


if __name__ == "__main__":
    unittest.main()
