#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Parse fichiers correction.txt en rst pour generer pdf dan sphinx
#
#----------------------- Imports ------------------------------
import re


#-------------------------- Fonctions -------------------------

def file_to_string(fichier):
    """
       Ouvre un fichier en lecture et le stock dans une chaine
    """
    try:
        monFichier = open(fichier, 'r', encoding = 'ansi').read()
    except FileNotFoundError:
        print(f"Je ne trouve pas '{fichier}' !")
    else:
        return monFichier

def sauve_fichier(file_out, chaine):
    """
       Sauvegarde du nouveau fichier
    """
    with open(file_out, 'w', encoding = 'utf8') as fichier:
        fichier.write(chaine)

def exo_title(chaine):
    """
        Recherche dans la chaine la présence de
        ##################################################
        # Titre de l'exercice
        ##################################################
    """
    regexp1 = "#(.)*Semaine"  #test pas tres concluant

    matches = re.finditer(regexp1, monFichier, re.S)

    for objet in matches:

        print(f"{objet.start()}-{objet.end()} {objet.group(0)}")


#--------------------- Main -----------------------------------


fichier = input("Traiter quel fichier ? ")

monFichier = file_to_string(fichier)

if monFichier != None:

    """ Inserer les tratement ici"""

    exo_title(monFichier)









