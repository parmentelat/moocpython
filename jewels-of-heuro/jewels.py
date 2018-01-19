# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:33:26 2018

@author: franc
"""

import numpy as np
import itertools


def diag_azero(tableau):
    for i in range(tableau.shape[0]):
        tableau[i, i] = 0


class My_IOerror(Exception):
    pass


def save_tabrect(fname, tab):
#    if tab.ndim != 2:
#        raise(My_IOerror, f" save tabtrect: ndim = {tab.ndim}")
    with open(fname + ".dat", "w", encoding='utf-8')as fsave:
        fsave.write(str(len(tab[0])) + "\n")
        for i in range(len(tab)):
            li = [str(tab[i][j]) for j in range(len(tab[0]))]
            fsave.write("\t".join(li) + "\n")


def load_tabrect(fname):
    with open(fname + ".dat", "r", encoding='utf-8')as fload:
        l0 = fload.readline()
        dim1 = int(l0)
        print(f"lecture de {fname}.dat => dim1 {dim1}")
        table = []
        for ss in fload:
            lstr = ss[:-1].split("\t")
            lint = []
            for sss in lstr:
                lint.append(int(sss))
            table.append(lint)
        print(table)
        return table


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
        save_tabrect("jewels", self.tableau)

    def load(self, fname):
        self.tableau = np.array(load_tabrect(fname))
        self.dim = len(self.tableau[0, :])
        print(self.dim)

    def solve(self, algo):
        """
        propose une solution selon l'algorithme algo
        pour l'instant algo = ""fb", force brute
        """
        if algo == "fb":
            chemin, longueur = self.force_brute()
        elif algo == "cl":
            chemin, longueur = self.closest()
        else:
            raise(JewelsError, f"{algo} : algorirthme inconnue")
        print(f"algorithme {algo}: chemin: {chemin}, longueur= {longueur}")

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
        return chbest, dbest

    def closest(self):
        chemin = (0,)
        while len(chemin) < self.dim:
            shortest = -1
            depart = chemin[len(chemin)-1]
            # avisiter = (i in range(self.dim) if i not in chemin)
            for i in range(self.dim):
                if i not in chemin:
                    d = self.tableau[depart, i]
                    if (shortest < 0) or (shortest > d):
                        shortest = d
                        arrivee = i
            chemin = chemin + (arrivee,)
        return chemin[1:], self.dist_parcourue(chemin)


if __name__ == "__main__":
    #♠ donjon = Jewels("r", 7)
    donjon = Jewels("f", "austria6")
    donjon.solve("fb")
    donjon.solve("cl")
    dj2 = Jewels("f", "austria101")
    dj2.solve("cl")
