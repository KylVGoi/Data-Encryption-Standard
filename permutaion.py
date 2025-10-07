def permutation(block: int, new_position: list[int], input_size: int) -> int:
    """
    Effectue une permutation sur un bloc en fonction d'une nouvelle position.

    :param block: Le bloc de données d'entrée sous forme d'entier.
    :param new_position: Liste des nouvelles positions des bits après permutation.
    :param input_size: Taille du bloc d'entrée en bits.
    :return: Le bloc permuté sous forme d'entier.
    """
    # on transforme l'entier en une "str" pour pouvoir travailler dessus
    block_in = format(block, f'0{input_size}b')
    permuted_block = ""
    for i in new_position:
        # on remplace le bit de sortie pas le bit d'entrée (dans la table)
        permuted_block += block_in[int(i) - 1]

    return int(permuted_block, 2)
