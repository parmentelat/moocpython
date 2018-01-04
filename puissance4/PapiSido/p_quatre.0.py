# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:06:15 2018
@author: franc
"""


class Joueur:
    nom = ""

    def __init__(self, nom):
        self.nom = nom


largeur = 7
hauteur = 6
symbols = ['.', 'X', '@']
partie = ""


def seq_car(c, n):
    "renvoie une chaine de n fois le caractére c ou éventuellemnt un chaine )"
    s = ""
    for i in range(n):
        s += c
    return s


def init():
    plateau = []
    plancher = []
    for i in range(largeur):
        colonne = []
        plancher.append(0)
        for j in range(hauteur):
            colonne.append(0)
        plateau.append(colonne)
    print(plateau)
    print(plancher)
    return(plateau, plancher)


def nouvelle_partie():
    pass


def draw_p4(plateau, tab="    "):
    ll = " "
    for i in range(largeur):
        ll += f" {i+1}"
    print(tab+ll)
    for j in range(hauteur):
        ll = "|"
        for i in range(largeur):
            ll += " " + symbols[plateau[i][hauteur-j-1]]
        ll += " |"
        print(tab+ll)
    print(tab+seq_car("=", 2*largeur+3))
    # print(f"plancher ={plancher}")


def coup_valide(col):
    if (col < 0) or (col >= largeur):
        return False
    elif plancher[col] >= hauteur:
        return False
    return True


def coup_joueur(nj):
    ok = False
    col = -1
    msg = "à toi de jouer"
    while not ok:
        s1 = f"{msg} {joueurs[nj].nom}:".strip()
        scol = input(s1 + "\nquelle colonne ? (A pour abandonner) ").strip()
        if scol == "A":
            return "A"
        if scol.isdigit() and len(scol) == 1:
            col = int(scol)-1
            if coup_valide(col):
                return col
        msg = "colonne non valide,"


def do_coup(col):
    # case = (col, plancher[col])
    plateau[col][plancher[col]] = 1 + len(partie) % 2
    plancher[col] += 1


def conclusion(res, joueurs, msg):
    if res == 0:
        return "partie nulle"
    if res in (1, 2):
        return f"Bravo {joueurs[res-1].nom} vainqueur par {msg}"


plateau, plancher = init()
draw_p4(plateau)
res = 3  # 0: partie nulle, 1,2 si vainqueur, 3 si encours
joueurs = (Joueur("Astucieux"), Joueur("Balourd"),)
while res == 3:
    coup = coup_joueur(len(partie) % 2)
    if coup == "A":
        res = 2 - len(partie) % 2
        msg = "abandon"
    else:
        do_coup(coup)
        draw_p4(plateau)
        partie += str(coup)
        print(f"partie: {partie}    plancher= {plancher}")
    if len(partie) >= hauteur * largeur:
        res = 0
        msg = "terminé"
print(conclusion(res, joueurs, msg))
