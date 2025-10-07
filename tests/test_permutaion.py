import unittest
from permutaion import permutation

INIT_PERM_TEST = [1, 5, 9, 8, 2, 3, 7, 4, 6]
FINAL_PERM_TEST = [1, 5, 6, 8, 2, 9, 7, 4, 3]


class TestPermutation(unittest.TestCase):

    def test_permutation_init_from_book(self):
        init = 0b100000001
        final = permutation(init, INIT_PERM_TEST, 9)
        expected = 0b101000000
        assert final == expected

    def test_permutation_final_from_book(self):
        expected = 0b100000001
        init = 0b101000000
        final = permutation(init, FINAL_PERM_TEST, 9)
        assert final == expected

    def test_permutation_identity(self):
        init = 0b1010
        pos = [1, 2, 3, 4]
        final = permutation(init, pos, 4)
        assert init == final

    def test_permutation_A(self):
        init = 0b1010
        expected = 0b0011
        pos = [2, 4, 3, 1]
        final = permutation(init, pos, 4)
        assert expected == final

    def test_permutation_inverse(self):
        init = 0b1010
        expected = 0b0101
        pos = [4, 3, 2, 1]
        final = permutation(init, pos, 4)
        assert expected == final

    def test_permutation_B(self):
        init = 0b1010
        expected = 0b1100
        pos = [3, 1, 4, 2]
        final = permutation(init, pos, 4)
        assert expected == final

 # Tests pour permutation

    def test_permutation_normal(self):
        # Test avec un bloc de 64 bits et une permutation simple
        block = 0b1010101010101010101010101010101010101010101010101010101010101010
        new_position = [64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        input_size = 64
        result = permutation(block, new_position, input_size)
        expected_result = 0b0101010101010101010101010101010101010101010101010101010101010101
        self.assertEqual(result, expected_result)

    def test_permutation_empty_position(self):
        # Cas dégradé : Test avec une liste de positions vide
        block = 0b1010101010101010101010101010101010101010101010101010101010101010
        new_position = []
        result = permutation(block, new_position, 64)
        self.assertEqual(result, 0)

    def test_permutation_large_block(self):
        # Cas dégradé : Test avec un bloc plus grand que 64 bits
        block = 0b1010101010101010101010101010101010101010101010101010101010101010
        new_position = [i for i in range(1, 129)]  # Positions allant de 1 à 128
        result = permutation(block, new_position, 128)
        self.assertNotEqual(result, 0)

    def test_permutation_small_block(self):
        # Cas dégradé : Test avec un bloc plus petit que 64 bits (par exemple 32 bits)
        block = 0b1010101010101010  # 32 bits
        new_position = [i for i in range(1, 33)]  # Positions de 1 à 32
        result = permutation(block, new_position, 32)
        self.assertNotEqual(result, 0)
