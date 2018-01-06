# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:06:15 2018
@author: franc
"""
import random

verbose = True


def seq_car(c, n):
    "renvoie une chaine de n fois le caractére c ou éventuellemnt un chaine )"
    s = ""
    for i in range(n):
        s += c
    return s


class Joueur:

    def __init__(self, nom, humain=True, symbol=""):
        self.nom = nom
        self.symbol = symbol
        self.humain = humain

    def __str__(self):
        return f"{self.nom} ({self.symbol})"

    def reponse(self, p4):
        if self.humain:
            print(self.nom + " n'est pas un robot")
            return "A"
        if self.nom == "AuHasard":
            return self.rep_AuHasard(p4)
        print(self.nom + " robot inconnu")
        return "A"

    def rep_AuHasard(self, p4):
        while True:
            col = random.randrange(p4.largeur)
            if p4.coup_valide(col):
                return col


class Analyse_p4:
    pass


class Puissance4:

    def __init__(self, ll=7, hh=6, symbols='.X@'):
        self.largeur = min(ll, 9)
        self.hauteur = min(hh, 10)
        self.symbols = [symbols[0], symbols[1], symbols[2]]

    def info(self):
        s = f"Puissance 4 taille {self.largeur}x{self.hauteur} "
        return s + f" symbols: {self.symbols}"

    def ini_partie(self, joueurs):
        self.joueurs = joueurs
        for i in range(2):
            if len(joueurs[i].symbol) != 1:
                joueurs[i].symbol = self.symbols[i+1]
            else:
                self.symbols[i+1] = joueurs[i].symbol
        print(f"new_partie: {joueurs[0]} vs {joueurs[1]}")
        self.ini_plateau()
        self.draw_p4()
        self.partie = str(self.largeur - 1) + str(self.hauteur - 1) + "##"

    def conclusion(self):
        if self.res == 0:
            return "partie nulle"
        if self.res in (1, 2):
            sres = f"Bravo {self.joueurs[self.res-1].nom}, "
            return sres + f"vainqueur par {self.msg}"
        return f"ERREUR res={self.res}"

    def coup_valide(self, col):
        if (col < 0) or (col >= self.largeur):
            return False
        elif self.plancher[col] >= self.hauteur:
            return False
        return True

    def coup_joueur(self, nj):
        ok = False
        col = -1
        msg = " à toi de jouer"
        invite = "quelle colonne ? (A pour abandonner) "
        while not ok:
            if self.joueurs[nj].humain:
                s1 = f"{msg} {self.joueurs[nj]}"
                scol = input(s1 + "\n" + invite).strip()
                if scol == "A":
                    return "A"
                if scol.isdigit() and len(scol) == 1:
                    col = int(scol)-1
                    if self.coup_valide(col):
                        return col
                msg = "colonne non valide,"
            else:
                return self.joueurs[nj].reponse(self)

    def do_coup(self, col):
        self.plateau[col][self.plancher[col]] = 1 + len(self.partie) % 2
        self.plancher[col] += 1

    def new_partie(self, joueurs):
        self.ini_partie(joueurs)
        self.res = 3  # 0: partie nulle, 1,2 si vainqueur, 3 si encours
        while self.res == 3:
            coup = self.coup_joueur(len(self.partie) % 2)
            if coup == "A":
                self.res = 2 - len(self.partie) % 2
                self.msg = "abandon"
            else:
                self.do_coup(coup)
                self.draw_p4()
                self.partie += str(coup)
                if verbose:
                    print(f"partie: {self.partie} > plancher={self.plancher}")
            if len(self.partie) > self.hauteur * self.largeur + 3:
                self.res = 0
                self.msg = "terminé"
            pass
        print(self.conclusion())

    def ini_plateau(self):
        self.plateau = []
        self.plancher = []
        for c in range(self.largeur):
            colonne = []
            self.plancher.append(0)
            for l in range(self.hauteur):
                colonne.append(0)
            self.plateau.append(colonne)
        # self.draw_p4()

    def draw_p4(self, tab="    "):
        ll = " "
        for i in range(self.largeur):
            ll += f" {i+1}"
        print(tab+ll)
        for j in range(self.hauteur):
            ll = "|"
            for i in range(self.largeur):
                symb = self.symbols[self.plateau[i][self.hauteur-j-1]]
                ll += " " + symb
            ll += " |"
            print(tab+ll)
        print(tab+seq_car("=", 2*self.largeur+3))


jeu = Puissance4()
print(jeu.info())
ja = Joueur("Alain")
jb = Joueur("Bernard", True, "B")
j0 = Joueur("AuHasard", False, "H")
jeu.new_partie((ja, j0))
