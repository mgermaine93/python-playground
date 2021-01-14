import unittest
from hello_name import hello_name


class UnitTests(unittest.TestCase):

    def test_bob_returns_hello_bob(self):
        actual = hello_name("Bob")
        expected = "Hello Bob!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Bob" to return "Hello Bob!"')

    def test_alice_returns_hello_alice(self):
        actual = hello_name("Alice")
        expected = "Hello Alice!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Alice" to return "Hello Alice!"')

    def test_x_returns_hello_x(self):
        actual = hello_name("X")
        expected = "Hello X!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "X" to return "Hello X!"')

    def test_dolly_returns_hello_dolly(self):
        actual = hello_name("Dolly")
        expected = "Hello Dolly!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Dolly" to return "Hello Dolly!"')

    def test_alpha_returns_hello_alpha(self):
        actual = hello_name("Alpha")
        expected = "Hello Alpha!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Alpha" to return "Hello Alpha!"')

    def test_omega_returns_hello_omega(self):
        actual = hello_name("Omega")
        expected = "Hello Omega!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Omega" to return "Hello Omega!"')

    def test_goodbye_returns_hello_goodbye(self):
        actual = hello_name("Goodbye")
        expected = "Hello Goodbye!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Alice" to return "Hello Goodbye!"')

    def test_ho_ho_ho_returns_hello_ho_ho_ho(self):
        actual = hello_name("ho ho ho")
        expected = "Hello ho ho ho!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "ho ho ho" to return "Hello ho ho ho!"')

    def test_xyz_returns_hello_xyz(self):
        actual = hello_name("xyz")
        expected = "Hello xyz!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "xyz" to return "Hello xyz!"')

    def test_hello_returns_hello_hello(self):
        actual = hello_name("Hello")
        expected = "Hello Hello!"
        self.assertEqual(
            actual, expected, 'Expected calling hello_name() with "Hello" to return "Hello Hello!"')


if __name__ == "__main__":
    unittest.main()
