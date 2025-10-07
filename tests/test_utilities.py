import unittest

from utilities import bytearray_to_64bits_block, _64bits_block_to_bytearray


class TestFunctions(unittest.TestCase):

    # Tests pour bytearray_to_64bits_block

    def test_bytearray_to_64bits_block_normal(self):
        # Test avec un bytearray de 8 octets
        byte_array = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
        result = bytearray_to_64bits_block(byte_array)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 0x0102030405060708)

    def test_bytearray_to_64bits_block_multiple_blocks(self):
        # Test avec un bytearray de 16 octets
        byte_array = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                                0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10])
        result = bytearray_to_64bits_block(byte_array)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 0x0102030405060708)
        self.assertEqual(result[1], 0x090A0B0C0D0E0F10)

    def test_bytearray_to_64bits_block_empty(self):
        # Cas dégradé : Test avec un bytearray vide
        byte_array = bytearray()
        result = bytearray_to_64bits_block(byte_array)
        self.assertEqual(result, [])

    def test_bytearray_to_64bits_block_single_byte(self):
        # Cas dégradé : Test avec un bytearray d'un seul octet
        byte_array = bytearray([0xFF])
        result = bytearray_to_64bits_block(byte_array)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 0xFF00000000000000)

    def test_bytearray_to_64bits_block_invalid(self):
        # Cas dégradé : Test avec un bytearray avec moins de 8 octets, il devrait y avoir un seul bloc partiel
        byte_array = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06])
        result = bytearray_to_64bits_block(byte_array)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 0x0102030405060000)  # Remplissage de 0 pour les octets manquants

    # Tests pour _64bits_block_to_bytearray

    def test_64bits_block_to_bytearray_normal(self):
        # Test avec une liste de blocs de 64 bits
        blocks = [0x0102030405060708, 0x090A0B0C0D0E0F10]
        result = _64bits_block_to_bytearray(blocks)
        expected = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                              0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10])
        self.assertEqual(result, expected)

    def test_64bits_block_to_bytearray_empty(self):
        # Cas dégradé : Test avec une liste vide de blocs
        blocks = []
        result = _64bits_block_to_bytearray(blocks)
        self.assertEqual(result, bytearray())

    def test_64bits_block_to_bytearray_partial_block(self):
        # Cas dégradé : Test avec un seul bloc incomplet (remplissage de 0 nécessaire)
        blocks = [0x01]
        result = _64bits_block_to_bytearray(blocks)
        self.assertEqual(result, bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]))

