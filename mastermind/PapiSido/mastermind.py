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
    """
    compte le nombre d'occurence d'élément dans liste
    J'ai essayé liste.count(eleemnt) mais ça ne marche pas 
    """
    ne = 0
    for e in liste:
        if e == element:
            ne += 1
    return ne


def mm_compare(l1, l2):
    """ 
    deux listes l1 et l2
    renvoie le tuple (cpos,ccol)
    cpos = nombre d'éléments identiques à la même position 
    ccol = nombre d'éléments identiques en position différente
    (régles du mastermind)
    """
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
    """
    transforme le retour de mm_compare sous forme d'une chaîne
    de cpos "o" et ccol "-" (2,1) -> "oo-"
    """
    ss = ""
    for i in range(cmp[0]):
        ss += "o"
    for i in range(cmp[1]):
        ss += "-"
    return ss


def str2cmp(s):
    """
    opération inverse de str_compare "oo-" -> (2,1)
    """
    return (s.count('o'), s.count('-'))


class Mastermind:
    """ Mastermind
    nombre de couleurs et de pions définis à l'initialisation
    une partie peut choisir et/ou résoudre un code
    """

    def __init__(self, journal, alphabet="ABCDEF", nb_pions=4):
        """
        alphabet définit les "couleurs" et du même coup leur nombre
        défaut mastermind classique 4 pions, 6 couleurs
        """
        self.journal = journal
        self.nb_pions = nb_pions
        self.nb_couleurs = len(alphabet)
        self.nb_comb = self.nb_couleurs**nb_pions
        self.alphabet = alphabet
        self.journal.write("---------" + self.info()+"\n")
        print(self.info())

    def print_historique(self, partie=""):
        self.journal.write(f"----- historique {partie} ------\n")
        for h in self.historique:
            self.journal.write(f"{h[0]} -> {h[1]}\n")
        self.journal.write(f"soit {len(self.historique)} essais")

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

    def solver_ini(self):
        self.lcomb = np.zeros(self.nb_comb, dtype=np.int8)
        self.lstidx0 = ()
        pass

    def solver_next(self):
        idx0 = random.randrange(self.nb_comb)
        if debug:
            idx0 = 0    # pour supprimer l'aléa et reproduire
        self.lstidx0 += (idx0,)
#        if verbose:
#                print(f"restent {nb_possibles} combinaisons possibles")
        while self.lcomb[idx0] > 0:
                idx0 = (idx0 + 1) % self.nb_comb
        ltry = self.lcombinaison(idx0)
        stry = self.scombinaison(ltry)
        return (stry, ltry)

    def solver_analyse(self, ltry, ret):
        for i in range(self.nb_comb):
            if (self.lcomb[i] == 0) and not self.compatible(i, ltry, ret):
                self.lcomb[i] = 1
            nb_possibles = compte(0, self.lcomb)
            if nb_possibles == 0:
                ret = "ERREUR"

    def partie(self, coder, solver):
        """
        coder et solver : qui choisit le code  et qui le résoud
        0 : l'utilisateur
        1 : l'ordinateur ( algorithme simple )
        """
        if coder == 0:
            ret = input("choisis ton code et retiens-le bien")
            self.journal.write("code choisi par l(uilisateur\n")
        else:
            self.choix_code()
            self.journal.write(f"code choisi: {self.scode} {self.lcode}\n")
        self.historique = ()
        nb_tries = 0
        if solver > 0:
            self.solver_ini()
        ret = (0, 0)
        while ret != "ERREUR" and ret[0] < self.nb_pions:
            nb_tries += 1
            if solver > 0:
                (stry, ltry) = self.solver_next()
            else:
                stry = input(f"essai {nb_tries}: Ta proposition? ")
                ltry = self.str2lbyte(stry)
            if coder > 0:
                ret = mm_compare(self.lcode, ltry)
                print(f"résultat pour {stry} : {str_compare(ret)}")
            else:
                res = input("pour essai: " + stry + "  réponse ? ")
                ret = str2cmp(res)
            if solver > 0:
                self.solver_analyse(ltry, ret)
            self.historique += ((stry, ret),)
        if ret == "ERREUR":
            print("Pour moi, c'est impossible!?  ")
        else:
            print(f"code trouvé en {nb_tries} essais")
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
    
    
    
    import argparse
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-a", "--alphabet", action='store', default='ABCDEF',
                            help = 'alphabet: the symbols used for colors')
    parser.add_argument("-n", "--number", action='store', default=4,
                            help="number of positions in the code")
    parser.add_argument("-z", "--nbgames", action='store', default=10,
                            help="number of games to be played")
    parser.add_argument("-s", "--solver", action='store_true', default=False,
                        help="l'ordinateur cherche (et trouve) le code")
    parser.add_argument("-c", "--coder", action='store_true', default=False,
                        help="l'ordinateur choisit le code")
    parser.add_argument("-j", "--journal", action='store', default="mm.jnl",
                        help="filename to store journal info; '-' for stdout")
    args = parser.parse_args()
        
    def real_main(journal):
        if args.coder:
            coder = 1
        else:
            coder = 0
        if args.solver:
            solver = 1
        else:
            solver = 0
        jeu = Mastermind(journal, args.alphabet, int(args.number))
        try:
            jeu.partie(coder, solver)
        except KeyboardInterrupt as e:
            print("bye") 
    
    
    if args.journal == '-':
        real_main(sys.stdout)
    else:
        with open(args.journal, "w") as journal:
            real_main(journal)
    
    
