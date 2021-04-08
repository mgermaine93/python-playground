import unittest
from string_sorter import string_sorter


class UnitTests(unittest.TestCase):

    def test_banana_ORANGE_apple(self):
        actual = string_sorter("banana ORANGE apple")
        expected = "apple banana ORANGE"
        self.assertEqual(
            actual, expected, 'Expected output to be "apple banana ORANGE" when calling "string_sorter()" with "banana ORANGE apple"')

    def test_aardvark_iguana_yak_zebra(self):
        actual = string_sorter("aardvark iguana yak zebra")
        expected = "aardvark iguana yak zebra"
        self.assertEqual(
            actual, expected, 'Expected output to be "aardvark iguana yak zebra" when calling "string_sorter()" with "aardvark iguana yak zebra"')

    def test_aardvark_zebra_yak_iguana(self):
        actual = string_sorter("aardvark zebra yak iguana")
        expected = "aardvark iguana yak zebra"
        self.assertEqual(
            actual, expected, 'Expected output to be "aardvark iguana yak zebra" when calling "string_sorter()" with "aardvark zebra yak iguana"')

    def test_a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z(self):
        actual = string_sorter(
            "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        expected = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        self.assertEqual(
            actual, expected, 'Expected output to be "a b c d e f g h i j k l m n o p q r s t u v w x y z" when calling "string_sorter()" with "a b c d e f g h i j k l m n o p q r s t u v w x y z"')

    def test_z_y_x_w_v_u_t_s_r_q_p_o_n_m_l_k_j_i_h_g_f_e_d_c_b_a(self):
        actual = string_sorter(
            "z y x w v u t s r q p o n m l k j i h g f e d c b a")
        expected = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        self.assertEqual(
            actual, expected, 'Expected output to be "a b c d e f g h i j k l m n o p q r s t u v w x y z" when calling "string_sorter()" with "z y x w v u t s r q p o n m l k j i h g f e d c b a"')


if __name__ == "__main__":
    unittest.main()
