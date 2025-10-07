from typing import List


def bytearray_to_64bits_block(byte_array: bytearray) -> List[int]:
    """
    Convertit un bytearray en une liste de blocs de 64 bits.
    """
    liste = []
    for i in range (0, len(byte_array), 8):
        block = (byte_array[i:i+8])
        #ajout de padding
        if len(block) < 8:
            block += b'\x00' * (8 - len(block))
        into_byte = int.from_bytes(block, 'big')
        liste.append(into_byte)
    return liste


def _64bits_block_to_bytearray(blocks: List[int]) -> bytearray:
    """
    Convertit une liste de blocs de 64 bits en un bytearray.
    """
    byte_array = b''
    for i in range (0, len(blocks)):
        byte_array += blocks[i].to_bytes(8, 'big')
    #on enlève le padding
    byte_array = byte_array.rstrip(b'\x00')
    return bytearray(byte_array)
