#!/usr/bin/env python3
#!python3

"""
Created on Wed Dec 13 17:33:12 2017
@author: jg

Script "artisanal" mais appliqué dont le point de départ est adapté
d'un modèle mis à dispo sur le Mooc Python 3

Objectif : regrouper les fichiers txt des corrigés par semaine sur un seul fichier rst
Hypothèse de départ : tous les fichiers y compris le script sont dans le même dossier
Option choisie : traitement par lignes et regroupement dans un seul objet
avant écriture finale dans le fihcier "corriges.rst"

Le script fonctionne très bien mais doit pouvoir être optimisé
Remarques, suggestions bienvenus...
"""
import os # gestion des dossier et des fichiers
import glob # trouve les chemins d'accès par motif
import re # Opérations à base d’expressions rationnelles
import textwrap # comme indiqué en titre du module ;)

# Vérification préalable pour le dossier et chaque fichier à traiter
def test(*args):
    #print(os.listdir("/home/jg/"))
    #print(len(args))
    if len(args):
        response = input(f"fichier => {args} ... à traiter ? (Entrée pour oui) :")
    else:
        path = os.path.dirname(os.path.abspath(__file__))
        response = input(f"dossier => {path} ... à traiter ? (Entrée pour oui) :")

    # validation ou non en réponse
    if len(str(response)):
        print("non")
        return False
    else:
        print("oui")
        return True
    
def launch_script(ext):
    # Récupération dans une liste de tous les fichiers.txt du dossier
    if test():
        txt_list = glob.glob(ext) 
        # demande de sélection par fichier trouvé
        file_list = [file for file in txt_list if test(file)]
        file_list.sort()
        print(file_list)
    
        if len(file_list):
            # lance la lecture des fichiers txt et le regroupement des données
            read(file_list)
        else:
            print("Oups! Apparemment aucun fichier à traiter...")
    else:
        print("Oups! Apparemment ce n'est pas le bon dossier...")

def read(corriges_list):
    # Création liste vide regroupant le contenu de tous les corriges.txt
    txt_fullcontents = []
    # récupération des données, regroupement et mise en forme pour Sphinx
    for titre_semaine in corriges_list:
        # gestionnaire de contexte qui ouvre en lecture
        # et ferme chaque fichier corriges.txt
        with open(titre_semaine, encoding='utf-8') as entree:
            prepareData(entree, txt_fullcontents)

    # lance l'écriture dans le fichier de regroupement rst
    write("".join(txt_fullcontents))

def prepareData(entree, txt_fullcontents):
    for line in entree:
        #suppression de lignes avec #### et autres... à optimiser ?
        line = re.sub(r"^#*[\n]", "\n", line)
        line = re.sub(r"(\# -\*- coding: utf-8 -\*-)", '', line)
        line = re.sub(r"^(#*\s{1})$", '', line)

        # titre 2
        if re.search(r"\w*(Corrigés de la semaine \d)\n", line):
            titre2 = re.search(r"\w*(Corrigés de la semaine \d)\n", line)[0]
            line = "\n\n" + titre2 + ("-" * len(titre2.strip())) + "\n\n"

        # titre 3
        elif re.search(r"\w*(Semaine \d Séquence \d\n)", line):
            titre3 = re.sub(r"^(#{1}\s{1})", '', line)
            line = "\n" + titre3 + ("~" * len(titre3.strip())) + "\n\n" + ".. code:: ipython3" + "\n\n"

        # indentation de 4 espaces les lignes "bloc de code" qui suivent les titres 3
        else:
            line = textwrap.indent(line,'    ')
            
        # regroupement de tous les corrigés dans un seul objet
        txt_fullcontents.append(f"{line}")

    return txt_fullcontents

def write(txt_fullcontents):
    titre = "Corrigés"
    titre = titre + "\n" + ("=" * len(titre))
    # gestionnaire de contexte qui ouvre en écriture
    # et ferme le fichier.rst (regroupement)
    with open('corriges.rst', "w", encoding='utf-8') as sortie:
        sortie.write(titre)
        sortie.write(f"{txt_fullcontents}")

# Lance la procédure pour les fichiers txt du dossier
launch_script("*.txt")
