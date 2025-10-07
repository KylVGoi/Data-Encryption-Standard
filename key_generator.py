from random import randint
from typing import List
from permutaion import permutation

# variables pour les sous clés
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
    ]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
    ]

SHIFTS = [ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def rdm_key_generator() -> int:
    """
    Génère une clé aléatoire de 64 bits.

    :return: Clé sous forme d'un entier de 64 bits.
    """
    return randint(0, 2**64 - 1)


def shift_left(data: int, input_size: int) -> int:
    """
    Effectue une rotation circulaire à gauche sur un bloc de données.

    :param data: Données sous forme d'un entier.
    :param input_size: Taille en bits du bloc à faire tourner.
    :return: Données après la rotation circulaire à gauche.
    """
    into_byte = format(data, f'0{input_size}b')
    rotation = into_byte[1:] + into_byte[0]
    return int(rotation, 2)


def des_key_generator(key: int) -> List[int]:
    """
    Génère les 16 sous-clés de 48 bits pour le chiffrement DES.

    :param key: Clé initiale de 64 bits.
    :return: Liste des 16 sous-clés de 48 bits.
    """
    global PC1, PC2, SHIFTS
    # permutation de la clé avec le PC1, pour donner une clé de 56 bits, en supprimant les bits de parité
    key_56 = permutation(key, PC1, 64)

    # on traite la clé pour la diviser en 2 parties
    key_bin = format(key_56, '056b')
    c = int(key_bin[:28], 2)
    d = int(key_bin[28:], 2)

    subkeys = []

    for shift in SHIFTS:
        # Décalage circulaire, si shift = 1 une rotation, si shift = 2 on en fait une double
        c = shift_left(c, 28) if shift == 1 else shift_left(shift_left(c, 28), 28)
        d = shift_left(d, 28) if shift == 1 else shift_left(shift_left(d, 28), 28)

        # Concaténer c et d + mettre au format binaire
        cd = format(c, '028b') + format(d, '028b')
        # transformer en int pour que ça rentre dans permutation
        cd_int = int(cd, 2)

        subkey_bin = permutation(cd_int, PC2, 56)

        subkeys.append(subkey_bin)

    return subkeys

