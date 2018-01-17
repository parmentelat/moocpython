# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:33:26 2018
Jewels of Heuro
http://www.open.edu/openlearn/science-maths-technology/computing-and-ict/computing/the-jewels-heuro
@author: francois sidoroff
"""

import numpy as np
import itertools


def diag_azero(tableau):
    for i in range(tableau.shape[0]):
        tableau[i, i] = 0


class JewelsError(Exception):
    pass


class Jewels:

    def __init__(self, meth, param):
        """ cree le tableau des distances
        si meth = "r" au hasard avec param-1 bijoux
            (entre 200 et 600 ( d(A,B)!=d(B,A)))
        si meth = "f" par lecture du fichier param.dat
        le fichier donjon.dat est aussi créé en sortie
        """
        # import random
        if meth == "r":
            self.dim = param
            self.tableau = np.random.randint(200, 600, (self.dim, self.dim))
        elif meth == "f":
            self.load(param)
        else:
            raise(JewelsError, f"methode {meth} inconnue")
        diag_azero(self.tableau)
        print(self.tableau)
        self.save()

    def save(self):
        with open("donjon.dat", "w", encoding='utf-8')as fsave:
            fsave.write(str(str(self.dim) + "\n"))
            for i in range(self.dim):
                li = [str(self.tableau[i, j]) for j in range(self.dim)]
                fsave.write("\t".join(li) + "\n")

    def load(self, fname):
        with open(fname + ".dat", "r", encoding='utf-8')as fload:
            l0 = fload.readline()
            self.dim = int(l0)
            print(f"lecture de {fname}.dat => dim {self.dim}")
            table = []
            for ss in fload:
                lstr = ss[:-1].split("\t")
                lint = []
                for sss in lstr:
                    lint.append(int(sss))
                table.append(lint)
            self.tableau = np.array(table, dtype=np.uint16)

    def solve(self, algo):
        """
        propose une solution selon l'algorithme algo
        pour l'instant algo = ""fb", force brute
        """
        if algo == "fb":
            self.force_brute()
        else:
            raise(JewelsError, f"methode inconnue")
            # raise(JewelsError, f"methode {algo} inconnue, à ce jour 'fb'")

    def dist_parcourue(self, chemin):
        distance = 0
        ch = chemin + (0,)
        for i in range(self.dim):
            distance += self.tableau[ch[i], ch[i+1]]
        return distance

    def force_brute(self):
        p = itertools.permutations(range(1, self.dim))
        dbest = -1
        for chemin in p:
            d_parcours = self.dist_parcourue((0,)+chemin)
            print(f"{chemin} > distance parcourue = {d_parcours}")
            if (dbest < 0) or d_parcours < dbest:
                dbest = d_parcours
                chbest = chemin
        print(f"chemin optimal {chbest} avec distance = {dbest}")


if __name__ == "__main__":
    donjon = Jewels("r", 5)
    # donjon = Jewels("f", "d4a")
    donjon.solve("fb")

