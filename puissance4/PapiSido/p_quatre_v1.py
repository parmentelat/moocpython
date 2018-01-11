# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:06:15 2018
@author: françois Sidoroff
"""
import random

verbose = False


def seq_car(c, n):
    "renvoie une chaine de n fois le caractére c ou éventuellemnt un chaine )"
    s = ""
    for i in range(n):
        s += c
    return s


class P4error(Exception):
    pass


class Joueur:
    """
    un joueur, humain ou robot
    """

    def __init__(self, nom, humain=True, symbol=""):
        """ humain = True pour un joueur humain, False pour un robot
        dans ce cas nom doit être le nom d'un robot existant,
        un seul pour l'instant
        "AuHasard" qui joue au hasard, là où il trouve de la place
        > pas très difficile à battre
        symbol = caractére choisi pour l'affichege, 
        si "" on prend la valeus par défaut ( "X" et "@" )
        """
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


class Ligne_p4:
    vecdir = ((1, 0), (0, 1), (1, 1), (-1, 1))
    typhow = ("xxxx", "xxx-", "xx-x", "xx--", "-xx-",
              "x-x-", "x--x", "x---", "-x--")
    cnthow = (4, 3, 3, 2, 2, 2, 2, 1, 1)  # améliorable avec un dictionnaire

    def idschem(self, nj):
        sch = ""
        for case in self.coord():
            sch += str(self.p4.plateau[case[0]][case[1]])
        # strsch = sch
        sch = sch.replace("0", "-").replace(str(nj), "x")
        # print(f"ligne {self}: {strsch} pour {nj} > {sch} ou {sch[::-1]}")
        # print(str(self) + strsch + sch)
        for i in range(9):
            sts = self.typhow[i]
            if (sch == sts) or (sch[::-1] == sts):
                return i
        raise(P4error)

    def __init__(self, p4, c0, l0, typ):
        self.p4 = p4
        self.c0 = c0
        self.l0 = l0
        self.typ = typ
        self.owner = 192

    def __str__(self):
        sret = self.id() + ":"
        if self.owner == 3*64:
            return sret + "void"
        elif self.owner == 0:
            return sret + "none"
        else:
            return sret + f"{self.owner//64}({self.owner%64})"

    def id(self):
        strsig = "HVZN"
        return strsig[self.typ]+str(self.c0)+str(self.l0)

    def coord(self):
        ligne = ()
        for i in range(4):
            cc = self.c0 + i * self.vecdir[self.typ][0]
            ll = self.l0 + i * self.vecdir[self.typ][1]
            ligne = ligne + ((cc, ll),)
        return ligne

    def inligne(self, c, l):
        if (c, l) in self.coord():
            return True
        return False

    def draw(self):
        graph = Puissance4(self.p4.largeur, self.p4.hauteur, symbols=".*.")
        graph.ini_plateau()
        cligne = self.coord()
        print(cligne)
        for cl in cligne:
            # print("cl ="+ cl)
            print(cl, cl[0], cl[1])
            graph.plateau[cl[0]][cl[1]] = 1
        graph.draw_p4()


class Analyse_p4:

    def ini_lignes(self):
        self.lignes = []
        for l in range(self.p4.hauteur):
            for c in range(self.p4.largeur-3):
                ligne = Ligne_p4(self.p4, c, l, 0)
                self.lignes.append(ligne)
        for c in range(self.p4.largeur):
            for l in range(self.p4.hauteur-3):
                ligne = Ligne_p4(self.p4, c, l, 1)
                self.lignes.append(ligne)
        for l in range(self.p4.hauteur-3):
            for c in range(self.p4.largeur-3):
                ligne = Ligne_p4(self.p4, c, l, 2)
                self.lignes.append(ligne)
        for l in range(self.p4.hauteur-3):
            for c in range(self.p4.largeur-3):
                ligne = Ligne_p4(self.p4, c+3, l, 3)
                self.lignes.append(ligne)
        if verbose:
            self.dump_lignes()

    def dump_lignes(self):
        journal.write(f"=> {len(self.lignes)} lignes")
        for li in self.lignes:
            journal.write(str(li))
        journal.write("-----------------------------")

    def __init__(self, p4):
        self.p4 = p4
        self.ini_lignes()
        if verbose:
            print(f"p4 {p4.largeur}x{p4.hauteur} > {len(self.lignes)} lignes")

    def vasy(self, cj, lj, nj):
        for li in self.lignes:
            ownedby = li.owner // 64
            if li.inligne(cj, lj) and ownedby > 0:
                strli = str(li)
                if ownedby == 3 - nj:
                    li.owner = 0
                else:
                    li.owner = 64*nj + li.idschem(nj)
                if verbose:
                    print(strli+" > "+str(li))

    def diagnostic(self):
        print('--------------------- diagnostic')
        self.cntown = [0, 0, 0, 0]
        l90 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cntsch = [l90[:], l90[:]]
        for li in self.lignes:
            #            own = self.cntown[li.owner//64]
            #            sch = self.cntown[li.owner % 64]
            own = li.owner // 64
            sch = li.owner % 64
            self.cntown[own] += 1
            if own in (1, 2):
                self.cntsch[own-1][sch] += 1
        if verbose:
            print("bilan: ", self.cntown, self.cntsch)

    def gagne(self):
        if self.cntown[0] == len(self.lignes):
            return 0
        for nj in (1, 2):
            if self.cntsch[nj-1][0] > 0:
                self.p4.msg = "KO"
                return nj
        return 3


class Puissance4:
    """ La classe principale
    utilise 3 classes: Joueur, Ligne_p4, et Analyse_p4
    """

    def __init__(self, ll=7, hh=6, symbols='.X@'):
        " initialise le plateau  ll colonses <=9 et hh lignes(<=10)"
        self.largeur = min(ll, 9)
        self.hauteur = min(hh, 10)
        self.symbols = [symbols[0], symbols[1], symbols[2]]
        journal.write(self.info())

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
        nj = 1 + len(self.partie) % 2
        self.plateau[col][self.plancher[col]] = nj
        self.analyse.vasy(col, self.plancher[col], nj)
        self.analyse.diagnostic()
        self.plancher[col] += 1

    def new_partie(self, joueurs):
        """ joue une partie entre 2 joueurs
        joueurs est un tuple des deux joueurs (joueur1 et joueur2)
        Attention: joueur1 = joueurs[0] et joueur2 = joueurs[1]
        """
        self.ini_partie(joueurs)
        self.res = 3  # 0: partie nulle, 1,2 si vainqueur, 3 si encours
        self.analyse = Analyse_p4(self)
        while self.res == 3:
            coup = self.coup_joueur(len(self.partie) % 2)
            if coup == "A":
                self.res = 2 - len(self.partie) % 2
                self.msg = "abandon"
            else:
                self.do_coup(coup)
                self.draw_p4()
                self.partie += str(coup)
                self.res = self.analyse.gagne()
                if verbose:
                    print(f"partie: {self.partie} > plancher={self.plancher}")
            if len(self.partie) > self.hauteur * self.largeur + 3:
                self.res = 0
                self.msg = "terminé"
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


if __name__ == "__main__":
    with open("p_quatre.jnl", "w", encoding='utf-8')as journal:
        journal.write("p_quatre journal\n")
        jeu = Puissance4()
        print(jeu.info())
        ja = Joueur("Alain")
        jb = Joueur("Bernard", True, "B")
        j0 = Joueur("AuHasard", False, "H")
        jeu.new_partie((j0, jb))
