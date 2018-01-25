# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:08:54 2018

@author: francois.sidoroff
"""

import random
verbose = False


def mm_compare(l1, l2):
    if len(l1) > len(l2):
        ll1, ll2 = l2[:], l1[:]
    else:
        ll1, ll2 = l1[:], l2[:]
    cpos = 0
    ccol = 0
    for i in range(len(l1)):
        if ll1[i] == ll2[i]:
            cpos += 1
            ll1[i] = -1
            ll2[i] = -1
    for i in range(len(l1)):
        for j in range(len(l2)):
            if ll1[i] >= 0 and ll1[i] == ll2[j]:
                ccol += 1
                ll1[i] = -1
                ll2[j] = -1
    if verbose:
        print(l1, l2, cpos, ccol)
    return (cpos, ccol)


def str_compare(cmp):
    ss = ""
    for i in range(cmp[0]):
        ss += "o"
    for i in range(cmp[1]):
        ss += "-"
    return ss


class Mastermind:

    def __init__(self,  alphabet="ABCDEF", nb_pions=4):
        self.nb_pions = nb_pions
        self.nb_couleurs = len(alphabet)
        self.nb_comb = self.nb_couleurs**nb_pions
        self.alphabet = alphabet
        print(self.info())

    def info(self):
        s = f"Mastermind {self.nb_pions} pions de "
        s += f"({self.nb_couleurs} couleurs{self.alphabet})"
        return s + f"  -> {self.nb_comb} combinaisons"

    def str2lbyte(self, mot):
        ll = []
        for car in mot:
            try:
                n = self.alphabet.index(car)
            except ValueError:
                return -1
            ll.append(n)
        return ll

    def choix_code(self):
        self.scode = ""
        self.lcode = []
        for i in range(self.nb_pions):
            rnd = random.randrange(self.nb_couleurs)
            self.scode += self.alphabet[rnd]
            self.lcode.append(rnd)
        if verbose:
            print("mon code = " + self.scode)

    def encodeur(self):
        self.choix_code()
        print("J'ai choisi mon code, à toi de le trouver")
        print("(o: à sa place -: ailleurs")
        nb_tries = 0
#        encore = False
        ret = (0, 0)
        while ret[0] < self.nb_pions:
            nb_tries += 1
            essai = input(f"essai {nb_tries}: Ta proposition? ")
            less = self.str2lbyte(essai)
            ret = mm_compare(self.lcode, less)
            print(f"résultat pour {essai} : {str_compare(ret)}")
        print(f"Bravo, tu as eu besoin de {nb_tries} essais")
        return nb_tries


def test_mm_compare():
    l1 = [0, 1, 2, 3]
    l2 = [0, 1, 4, 2]
    print(l1, l2)
    print(mm_compare(l1, l2))
    print(l1, l2)


if __name__ == "__main__":
    jeu = Mastermind()
    jeu.encodeur()
