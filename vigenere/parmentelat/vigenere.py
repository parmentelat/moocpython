#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
from itertools import cycle

"""
la classe Vigenere permet de coder et décoder à partir d'une clé

on fournit deux variantes de l'algorithme, selon la façon
dont est traitée la ponctuation
"""


# un hash qui associe à un tuple (texte, cle) le caractère correspondant
# (texte, cle) -> code
encode_vigenere = {
    (x, y): chr((ord(y) + ord(x) - 97 * 2) % 26 + 97)
    for x in string.ascii_lowercase
    for y in string.ascii_lowercase
}

# pour inverser, c'est à dire pour construire
# (code, cle) -> texte
# c'est très simple
decode_vigenere = {
    (z, y): x for (x, y), z
    in encode_vigenere.items()
}

# algo #1 : on fait tourner la clé pour tous les caractères
# du message, même la ponctuation


def vigenere_continuous(texte, cle, table):
    """
    encode ou decode un texte, avec l'algorithme 
    dit "continuous" c'est-à-dire qu'on fait tourner
    la clé même si on rencontre un caractère de ponctuation

    l'objet table est une des deux tables de hash ci-dessus
    selon qu'on code ou qu'on decode

    retourne un iterateur
    """
    # on s'économise la compréhension qui n'est pas utile,
    # un générateur fera tout à fait l'affaire
    # avec cycle, on n'a pas besoin de gérer
    # les longeurs respectives du texte et de la clé
    for x, y in zip(texte, cycle(cle)):
        # si on ne trouve pas le tuple, c'est qu'on a en entrée
        # un espace ou une ponctuation, on le laisse alors tel quel
        yield table.get((x, y), x)


# algo #2 : on ne fait tourner la clé que quand on encode
# un caractère alphabétique
def vigenere_skip_punctuation(texte, cle, table):
    """
    encode ou decode, mais cette fois on ne fait tourner
    la clé que si on a rencontré un caractère alphabétique

    sinon comme vigenere_continuous

    """
    infinite_key = cycle(cle)

    def lookup(x):
        if x in string.ascii_lowercase:
            k = next(infinite_key)
            return table.get((x, k))
        else:
            return x
    for x in texte:
        yield lookup(x)


# deux points d'entrée sous forme de fonctions
def encode(texte, cle):
    """
    encode en mode skip_continuous
    """
    return "".join(
        vigenere_skip_punctuation(texte, cle, encode_vigenere))


def decode(texte, cle):
    """
    decode en mode skip_continuous
    """
    return "".join(
        vigenere_skip_punctuation(texte, cle, decode_vigenere))


####################
class Vigenere:
    """
    une instance de Vigenere est un codeur-décodeur
    """

    def __init__(self, cle, continuous=False):
        self.cle = cle
        self.continuous = continuous

    def encode(self, message):
        """
        encode et retourne un str
        """
        iterator = vigenere_continuous(message, self.cle, encode_vigenere) \
            if self.continuous \
            else vigenere_skip_punctuation(message, self.cle, encode_vigenere)
        return "".join(iterator)

    def decode(self, message):
        """
        decode et retourne un str
        """
        iterator = vigenere_continuous(message, self.cle, decode_vigenere) \
            if self.continuous \
            else vigenere_skip_punctuation(message, self.cle, decode_vigenere)
        return "".join(iterator)


####################
if __name__ == '__main__':

    texte_clair = "voici une proposition de code pour vigenere"
    cle = "python"

    codec = Vigenere(cle)
    texte_encode = codec.encode(texte_clair)
    print(f"encode = {texte_encode}")
    texte_decode = codec.decode(texte_encode)
    print(f"decode = {texte_decode}")
