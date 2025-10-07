import os
from typing import List

from des import encrypt, decrypt
from key_generator import des_key_generator
from utilities import bytearray_to_64bits_block, _64bits_block_to_bytearray


def save_to_bin(filename: str, byte_array: bytearray):
    """
    Sauvegarde un bytearray dans un fichier binaire.
    """
    with open(filename, "wb") as file:
        file.write(byte_array)


def load_from_bin(filename: str) -> bytearray:
    """
    Charge un fichier binaire et retourne son contenu sous forme de bytearray.
    """
    with open(filename, "rb") as file:
        return bytearray(file.read())


def load_txt_file(name: str) -> str:
    """
    Charge la première ligne d'un fichier texte.
    """
    with open(name, encoding="UTF-8") as file:
        return file.readline().strip()


def save_txt_file(name: str, txt: str):
    """
    Sauvegarde une chaîne de caractères dans un fichier texte.
    """
    with open(name, "w", encoding="UTF-8") as file:
        file.write(txt)



def encrypt_file(input_filename: str, secret_key: int, OFB: bool = False) -> int:
    """Chiffre un fichier et sauvegarde le résultat."""

    filename = os.path.basename(input_filename)
    directory = os.path.dirname(input_filename) + '\\..\\Encrypted'
    output_filename = os.path.join(directory, filename)

    key_array: List[int] = des_key_generator(secret_key)
    array: bytearray = load_from_bin(input_filename)
    loaded_blocks: List[int] = bytearray_to_64bits_block(array)
    cypher_blocks: List[int] = encrypt(loaded_blocks, key_array, OFB)
    save_to_bin(output_filename, _64bits_block_to_bytearray(cypher_blocks))
    print(f"{input_filename} encrypted into {output_filename} with key {secret_key:#016x}")
    return secret_key


def decrypt_file(input_filename: str, key: int, OFB: bool = False) -> None:
    """Déchiffre un fichier et sauvegarde le résultat."""

    filename = os.path.basename(input_filename)
    directory = os.path.dirname(input_filename) + '\\..\\Decrypted'
    output_filename = os.path.join(directory, filename)

    key_array: List[int] = des_key_generator(key)
    loaded_array: bytearray = load_from_bin(input_filename)
    loaded_cypher_blocks: List[int] = bytearray_to_64bits_block(loaded_array)
    decrypted_array: bytearray = _64bits_block_to_bytearray(decrypt(loaded_cypher_blocks, key_array, OFB))
    save_to_bin(output_filename, decrypted_array)
    print(f"{input_filename} decrypted into {output_filename} with key {key:#016x}")

