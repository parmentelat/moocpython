# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:08:54 2018

@author: francois.sidoroff
"""

import random
import numpy as np
verbose = False
debug = False


def compte(element, liste):
    ne = 0
    for e in liste:
        if e == element:
            ne += 1
    return ne


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
    if debug:
        print("mm_compare ", l1, l2, cpos, ccol)
    return (cpos, ccol)


def str_compare(cmp):
    ss = ""
    for i in range(cmp[0]):
        ss += "o"
    for i in range(cmp[1]):
        ss += "-"
    return ss


def str2cmp(s):
    return (s.count('o'), s.count('-'))


class Mastermind:
    """ Mastermind
    nombre de couleurs et de pions définis à l'initialisation
    encodeur() choisit un code et te réponds pour que tu le trouves
    decodeur() trouvera un code, lorsque cela sera implanté
    """

    def __init__(self,  alphabet="ABCDEF", nb_pions=4):
        """
        alphabet définit les "couleurs"
        """
        self.nb_pions = nb_pions
        self.nb_couleurs = len(alphabet)
        self.nb_comb = self.nb_couleurs**nb_pions
        self.alphabet = alphabet
        journal.write("---------" + self.info()+"\n")
        print(self.info())

    def print_historique(self, partie=""):
        journal.write(f"----- historique {partie} ------\n")
        for h in self.historique:
            journal.write(f"{h[0]} -> {h[1]}\n")
        journal.write(f"soit {len(self.historique)} essais")

    def info(self):
        s = f"Mastermind {self.nb_pions} pions de "
        s += f"{self.nb_couleurs} couleurs ({self.alphabet})"
        return s + f"  -> {self.nb_comb} combinaisons"

    def str2lbyte(self, mot):
        ll = []
        for car in mot:
            try:
                n = self.alphabet.index(car)
            except ValueError:
                n = -1
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
        self.historique = ()
        self.choix_code()
        print("J'ai choisi mon code, à toi de le trouver")
        print("(o: à sa place -: ailleurs)")
        nb_tries = 0
#        encore = False
        ret = (0, 0)
        while ret[0] < self.nb_pions:
            nb_tries += 1
            essai = input(f"essai {nb_tries}: Ta proposition? ")
            less = self.str2lbyte(essai)
            ret = mm_compare(self.lcode, less)
            print(f"résultat pour {essai} : {str_compare(ret)}")
            self.historique += ((essai, ret),)
        print(f"Bravo, tu as eu besoin de {nb_tries} essais")
        self.print_historique()
        if verbose:
            print("historique:", self.historique)
        return nb_tries

    def lcombinaison(self, idxl):
        ii = idxl
        lc = []
        for i in range(self.nb_pions):
            lc.append(ii % self.nb_couleurs)
            ii //= self.nb_couleurs
        # lc.reverse()
        return lc[::-1]

    def scombinaison(self, ll):
        sret = ""
        for i in range(self.nb_pions):
            sret += self.alphabet[ll[i]]
        return sret

    def compatible(self, idx, essai, retour):
        return mm_compare(essai, self.lcombinaison(idx)) == retour

    def decodeur(self):
        self.historique = ()
        nb_tries = 0
        lcomb = np.zeros(self.nb_comb, dtype=np.int8)
        mmsh = [self.nb_couleurs for i in range(self.nb_pions)]
        tcomb = lcomb.reshape(mmsh)
        if verbose:
            print(lcomb.shape, tcomb.shape)
        print("réponse par une chaîne o: à sa place -: ailleurs)  ")
        ret = input("Choisis et note ton code puis retour  ")
        print("réponse par une chaîne de o et - ")
        print("o pour un pion à sa place ")
        print("- pour une lettre présente mais mal placée")
        print("exemple si code ABFF essai FAFA > réponse o--")
        ret = (0, 0)
        nb_possibles = self.nb_comb
        while ret != "NO" and ret[0] < self.nb_pions:
            nb_tries += 1
            idx0 = random.randrange(self.nb_comb)
            idx0 = 25    #} pour supprimer l'aléa et reproduire
            if verbose:
                print(f"restent {nb_possibles} combinaisons possibles")
#            lc = self.lcombinaison(idx0)
            while lcomb[idx0] > 0:
                idx0 = (idx0 + 1) % self.nb_comb
            ltry = self.lcombinaison(idx0)
            stry = self.scombinaison(ltry)
            ret = (ret[0] + 1, 2)
            res = input(" mon essai: " + stry + "  verdict ? ")
            ret = str2cmp(res)
            for i in range(self.nb_comb):
                if (lcomb[i] == 0) and not self.compatible(i, ltry, ret):
                    lcomb[i] = 1
            nb_possibles = compte(0, lcomb)
            if nb_possibles == 0:
                ret = "NO"
            self.historique += ((stry, ret),)
        if ret == "NO":
            print("C'est impossible! Tricheur ou Distrait ? ")
        else:
            print(f"J'ai trouvé en {nb_tries} essais")
        self.print_historique()
        if verbose:
            print("historique:", self.historique)
        return nb_tries


def test_mm_compare():
    l1 = [0, 1, 2, 3]
    l2 = [0, 1, 4, 2]
    print(l1, l2)
    print(mm_compare(l1, l2))
    print(l1, l2)


if __name__ == "__main__":
    with open("mastermind.jnl", "w", encoding='utf-8')as journal:
        jeu = Mastermind('ABCDEF', 4)
#        jeu.encodeur()
        jeu.decodeur()
