from key_generator import *
from des_feistel_function import des_feistel_function
from utilities import *
from utilities import _64bits_block_to_bytearray
from typing import List


def feistel(block: int, key: int, swap: bool = True) -> int:
    """Applique une fonction de Feistel sur un bloc de 64 bits avec une sous-clé."""
    return 0


def encrypt_block(block: int, key_array: List[int]) -> int:
    """Chiffre un bloc de 64 bits avec une série de sous-clés."""
    return 0


def encryptECB(blocks: List[int], key_array: List[int]) -> List[int]:
    """Chiffre une liste de blocs en mode ECB."""
    return []


def encryptOFB(blocks: List[int], key_array: List[int]) -> List[int]:
    """Chiffre une liste de blocs en mode OFB."""
    return []


def encrypt(blocks: List[int], key_array: List[int], OFB: bool = False) -> List[int]:
    """Chiffre les blocs en mode ECB ou OFB selon le paramètre."""
    return []


def decrypt_block(block: int, key_array: List[int]) -> int:
    """Déchiffre un bloc de 64 bits avec une série de sous-clés."""
    return 0


def decryptECB(blocks: List[int], key_array: List[int]) -> List[int]:
    """Déchiffre une liste de blocs en mode ECB."""
    return []


def decryptOFB(blocks: List[int], key_array: List[int]) -> List[int]:
    """Déchiffre une liste de blocs en mode OFB."""
    return []


def decrypt(blocks: List[int], key_array: List[int], OFB: bool = False) -> List[int]:
    """Déchiffre les blocs en mode ECB ou OFB selon le paramètre."""
    return []

