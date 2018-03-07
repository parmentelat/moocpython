# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:06:15 2018
@author: françois Sidoroff
"""
import random
import numpy as np

verbose = False


def str2lico(s):
    li = ord(s[0])-65
    co = int(s[1])-1
    # print (f"{s} -> {(li,co)}")
    return (li, co)


def lico2str(lico):
    return chr(65+lico[0])+str(lico[1]+1)


class JTerror(Exception):
    pass


class Ligne_ttt:
    vecdir = ((1, 0), (0, 1), (1, 1), (-1, 1))
    typhow = ("xxx", "xx-", "x-x", "x--", "-x-")
    cnthow = (3, 2, 2, 1, 1)  # améliorable avec un dictionnaire

    def idschem(self, nj):
        sch = ""
        for case in self.coord():
            sch += str(self.ttt.plateau[case[0]][case[1]])
        # strsch = sch
        sch = sch.replace("0", "-").replace(str(nj + 1), "x")
        # print(f"ligne {self}: {strsch} pour {nj} > {sch} ou {sch[::-1]}")
        # print(str(self) + strsch + sch)
        for i in range(5):
            sts = self.typhow[i]
            if (sch == sts) or (sch[::-1] == sts):
                return i
        print(f"ERROR idschem: {sch}")
        raise(JTerror)

    def __init__(self, journal, ttt, l0, c0, typ):
        self.jnl = journal
        self.ttt = ttt
        self.c0 = c0
        self.l0 = l0
        self.typ = typ
        self.owner = 192
        # print(f"{self}\n")
        # self.draw()

    def __str__(self):
        sret = self.id() + ":"
        if self.owner == 3*64:
            return sret + "void"
        elif self.owner == 0:
            return sret + "none"
        else:
            return sret + f"{self.owner//64}({self.owner%64})"

    def id(self):
        strsig = "VHNZ"
        return strsig[self.typ]+str(self.l0)+str(self.c0)

    def coord(self):
        ligne = ()
        for i in range(-1, 2):
            cc = self.c0 + i * self.vecdir[self.typ][1]
            ll = self.l0 + i * self.vecdir[self.typ][0]
            ligne = ligne + ((ll, cc),)
        return ligne

    def inligne(self, lico):
        if lico in self.coord():
            return True
        return False

    def draw(self):
        graph = TicTacToe(self.ttt.largeur, self.ttt.hauteur, symbols=".*.")
        graph.ini_plateau()
        graph.partie = ""
        cligne = self.coord()
        print(cligne)
        for cl in cligne:
            # print("cl ="+ cl)
            print(cl, cl[0], cl[1])
            graph.plateau[cl[0]][cl[1]] = 1
        graph.draw_ttt()


class Analyse_ttt:

    def ini_lignes(self):
        self.lignes = []
        for l in range(1, self.ttt.hauteur - 1):
            for c in range(self.ttt.largeur):
                ligne = Ligne_ttt(self.jnl, self.ttt, l, c, 0)
                self.lignes.append(ligne)
        for c in range(1, self.ttt.largeur - 1):
            for l in range(self.ttt.hauteur):
                ligne = Ligne_ttt(self.jnl, self.ttt, l, c, 1)
                self.lignes.append(ligne)
        for l in range(1, self.ttt.hauteur-1):
            for c in range(1, self.ttt.largeur-1):
                ligne = Ligne_ttt(self.jnl, self.ttt, l, c, 2)
                self.lignes.append(ligne)
                ligne = Ligne_ttt(self.jnl, self.ttt, l, c, 3)
                self.lignes.append(ligne)
        if verbose:
            self.dump_lignes()

    def dump_lignes(self):
        self.jnl.write(f"=> {len(self.lignes)} lignes\n")
        for li in self.lignes:
            self.jnl.write(str(li)+"\n")
        self.jnl.write("-----------------------------")

    def __init__(self, journal, ttt):
        self.jnl = journal
        self.ttt = ttt
        self.ini_lignes()
        if verbose:
            print(f"ttt {ttt.largeur}x{ttt.hauteur} \
                  > {len(self.lignes)} lignes")

    def vasy(self, coup, nj):
        #  print("vasy", coup, nj)
        for li in self.lignes:
            ownedby = li.owner // 64
            if li.inligne(coup) and ownedby > 0:
                strli = str(li)
                if ownedby == 2 - nj:
                    li.owner = 0
                else:
                    li.owner = 64*(nj+1) + li.idschem(nj)
                if verbose:
                    print(strli+" > "+str(li))
        self.dump_lignes()

    def diagnostic(self):
        # print('--------------------- diagnostic')
        self.cntown = [0, 0, 0, 0]
        l50 = [0, 0, 0, 0, 0]
        self.cntsch = [l50[:], l50[:]]
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
                self.ttt.msg = "KO"
                return nj
        return 3


class TicTacToe:
    """ La classe principale
    utilise 2 classes: Ligne_ttt et Analyse_ttt
    """

    def __init__(self, journal, ll=3, hh=3, symbols='.XO'):
        " initialise le plateau  ll colonses <=9 et hh lignes(<=10)"
        self.jnl = journal
        self.largeur = min(ll, 9)
        self.hauteur = min(hh, 10)
        self.symbols = [symbols[0], symbols[1], symbols[2]]
        self.jnl.write(self.info()+"\n")

    def info(self):
        s = f"TicTacToe taille {self.largeur}x{self.hauteur} "
        return s + f" symbols: {self.symbols}"

    def ini_partie(self, joueurs):
        self.joueurs = joueurs
        self.partie = str(self.largeur - 1) + str(self.hauteur - 1) + "##"
        print(f"new_partie: {joueurs[0]} vs {joueurs[1]}")
        self.ini_plateau()
        self.draw_ttt()

    def conclusion(self):
        if self.res == 0:
            return "partie nulle"
        if self.res in (1, 2):
            sres = f"Bravo joueur {self.res}, "
            return sres + f"vainqueur par {self.msg}"
        return f"ERREUR res={self.res}"

    def coup_valide(self, licol):
        if licol[0] < 0 or licol[0] >= self.hauteur:
            return False
        if licol[1] < 0 or licol[1] >= self.largeur:
            return False
        if self.plateau[licol[0], licol[1]] != 0:
            return False
        return True

    def coup_joueur(self, nj):
        ok = False
        if self.joueurs[nj] == 0:
            msg = f"joueur {nj + 1} ({self.symbols[nj+1]})"
            invite = "quelle case ? (A1 par exemple, R pour abandonner) "
        while not ok:
            if self.joueurs[nj] == 0:
                scoup = input(msg + "\n" + invite).strip()
                if scoup.strip() == "R":
                    return "R"
                lcoup = str2lico(scoup)
            else:
                lcoup = (random.randrange(self.hauteur),
                         random.randrange(self.largeur))
            if self.coup_valide(lcoup):
                ok = True
        if self.joueurs[nj] > 0:
            print(f"L'ordinateur joue en {lico2str(lcoup)}")
        return lcoup

    def do_coup(self, lcoup, nj):
        self.plateau[lcoup[0], lcoup[1]] = nj + 1

    def new_partie(self, joueurs=(0, 0)):
        """ joue une partie entre 2 joueurs (a,b), a commence
        si a,b = 0 utilisateur
        si a,b = 1 ordinateur
        donc par défaut 2 joueurs humains
        """
        self.ini_partie(joueurs)
        self.res = 3  # 0: partie nulle, 1,2 si vainqueur, 3 si encours
        self.analyse = Analyse_ttt(self.jnl, self)
        while self.res == 3:
            nj = (len(self.partie)//2) % 2
            coup = self.coup_joueur(nj)
            if coup == "R":
                self.res = 2 - nj
                self.msg = "abandon"
            else:
                self.do_coup(coup, nj)
                self.partie += lico2str(coup)
                self.draw_ttt()
                self.analyse.vasy(coup, nj)
                self.analyse.diagnostic()
                self.res = self.analyse.gagne()
            if len(self.partie) > 2*(self.hauteur * self.largeur) + 3:
                if self.res == 3:
                    self.res = 0
                    self.msg = "terminé"
        print(self.conclusion())

    def ini_plateau(self):
        lableau = np.zeros(self.largeur*self.hauteur, dtype=np.uint8)
        self.plateau = lableau.reshape((self.hauteur, self.largeur))

    def draw_ttt(self, tab="    "):
        ll = "  "
        for i in range(self.largeur):
            ll += f" {i+1}"
        print(tab+ll)
        for j in range(self.hauteur):
            ll = chr(65+j) + " "
            for i in range(self.largeur):
                symb = self.symbols[self.plateau[j][i]]
                ll += " " + symb
            # ll += " |"
            print(tab+ll)
        if verbose:
            print(f"{self.partie}  plateau\n {self.plateau}")


if __name__ == "__main__":
    with open("tictactoe.jnl", "w", encoding='utf-8')as journal:
        journal.write("tictactoe\n")
        jeu = TicTacToe(journal, 3, 3)
        print(jeu.info()+"\n")
        jeu.new_partie((1, 0 ))
