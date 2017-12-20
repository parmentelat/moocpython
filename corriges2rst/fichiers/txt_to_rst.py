#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Parse fichiers correction.txt en rst pour generer pdf dan sphinx
#
#----------------------- Imports ------------------------------

import os.path

import shutil


#-------------------------- Fonctions -------------------------

def file_to_add():
    """
       Liste les fichiers à assembler
    """

    file_liste = []
    test = True

    while test:

        fichier = input("Entrez le nom du fichier : > ")

        if os.path.isfile(fichier):
            file_liste.append(fichier)

        else:

            print(f"Je ne trouve pas '{fichier}' !")

        if input("Un autre fichier ? (O/N) :") in "Nn":

            test = False

    return file_liste


def assemble(chaine):
    """
       Assemble les fichiers lister par 'file_to_add' et crée un fichier temporaire
    """

    with open('temp_file.txt', 'w', encoding = 'utf8') as sortie:
        for entree in ma_liste:
            with open(entree, 'r', encoding = 'utf8') as en_cours:
                shutil.copyfileobj(en_cours, sortie)


def file_to_string(fichier):
    """
       Ouvre le fichier créé par 'assemble' en lecture et le stock dans une chaine
    """
    try:
        monFichier = open(fichier, 'r', encoding = 'utf8').read()
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


def to_rst(chaine):
    """
       Traite la chaine créé par 'file_to_string'
    """

    temp_list = chaine.split("\n")

    for num_ligne, ligne in enumerate(temp_list):

        # Si une ligne contient coding on l'enléve
        if "coding" in ligne:

            temp_list[num_ligne] = ""

        # Si une ligne contient Corrigés faire un titre de niveau 2 et enlever les # de la ligne precedente et suivante
        elif "Corrigés" in ligne:

            temp_list[num_ligne] = ligne[2:] + "\n" + "-" * len(ligne[2:])
            temp_list[num_ligne + 1] = ""
            temp_list[num_ligne - 1] = ""

        # Si une ligne contient Semaine oter les deux premiers carateres et faire un titre de niveau 3
        # les lignes suivante sont du code donc ajouter .. code:: ipython3
        elif "Semaine" in ligne:

            temp_list[num_ligne] = ligne[2:] + "\n" + "~" * len(ligne[2:]) + "\n" + "\n.. code:: ipython3\n"

        # Si une ligne contient plusieurs # mettre une ligne vide
        elif "#######" in ligne:

            temp_list[num_ligne] = ""


        # indenter les autres lignes
        else:

            temp_list[num_ligne] = "    " + ligne

    return "\n".join(temp_list)



#--------------------- Main -----------------------------------

ma_liste = file_to_add()

assemble(ma_liste)

monFichier = file_to_string('temp_file.txt')

new_fichier = to_rst(monFichier)

mon_titre = "Corrigés\n========\n"

new_fichier = mon_titre + new_fichier

sauve_fichier('corriges_all.rst', new_fichier)









